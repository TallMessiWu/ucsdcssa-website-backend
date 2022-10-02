import random
import string
from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from flask_mail import Message
from exts import db, redis_captcha, mail, redis_token
from models.user import UserModel
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash

login_bp = Blueprint("user", __name__)
api = Api(login_bp)


class Register(Resource):
    # 注册用户
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, location="form", required=True)
        parser.add_argument('username', type=str, location="form", required=True)
        parser.add_argument('password', type=str, location="form", required=True)
        parser.add_argument('captcha', type=str, location="form", required=True)
        args = parser.parse_args()
        print(args)

        # 校验验证码
        captcha = redis_captcha.get(args.email)
        if captcha is None or captcha.decode("utf8") != args.captcha:
            return "验证码错误", 409

        user = UserModel(email=args.email, username=args.username, password=args.password)
        db.session.add(user)

        try:
            db.session.commit()
        # 重复邮箱
        except IntegrityError as e:
            db.session.rollback()
            db.session.flush()
            return "邮箱已注册", 409

        token = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=20))
        redis_token.setex(user.id, 3600, token)
        return {"token": token, "id": user.id}


class Captcha(Resource):
    # 新增验证码
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, location="form", required=True)
        parser.add_argument('purpose', type=str, location="form", required=True)
        args = parser.parse_args()

        # 验证码6位数，有效期10分钟
        captcha = "".join([str(random.randint(0, 9)) for i in range(6)])
        redis_captcha.setex(args.email, 600, captcha)

        # 发送邮件
        message = Message(
            subject="您的UCSD CSSA{}验证码".format(args.purpose),
            recipients=[args.email],
            html=
            """
            <div>您好，您的验证码为：</div>
            <div><h2>{}</h2></div>
            <div>该验证码将于10分钟后过期。</div>
            """.format(captcha),
            charset="utf8"
        )
        try:
            mail.send(message)
        except Exception as e:
            return "请检查邮箱地址", 409


class Login(Resource):

    # 登录
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, location="form", required=True)
        parser.add_argument('password', type=str, location="form", required=True)
        args = parser.parse_args()

        user = UserModel.query.filter_by(email=args.email).first()
        if user is None:
            return "邮箱未注册", 409
        if not check_password_hash(user.password, args.password):
            return "密码不正确", 409

        token = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=20))
        redis_token.setex(user.id, 3600, token)
        return {"token": token, "id": user.id}


class ResetPassword(Resource):
    # 根据邮箱重置密码
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, location="form", required=True)
        parser.add_argument('password', type=str, location="form", required=True)
        parser.add_argument('captcha', type=str, location="form", required=True)
        args = parser.parse_args()

        captcha = redis_captcha.get(args.email)
        if captcha is None or captcha.decode("utf8") != args.captcha:
            return "验证码错误", 409

        user = UserModel.query.filter_by(email=args.email).first()
        if user is None:
            return "邮箱未注册", 409

        user.password = args.password
        db.session.commit()


class UserInfo(Resource):
    # 根据id查询
    def get(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str, location="headers")

        # token验证
        input_token = parser.parse_args().token
        token = redis_token.get(user_id)
        if input_token is None or token is None or input_token != token.decode("utf8"):
            return "登录过期，请重新登录", 403

        result = UserModel.query.get(user_id)
        if not result:
            return "用户id不存在", 404

        return jsonify(UserModel.query.get(user_id))

    # 根据id删除
    def delete(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str, location="headers")

        # token验证
        input_token = parser.parse_args().token
        token = redis_token.get(user_id)
        if input_token is None or token is None or input_token != token.decode("utf8"):
            return "登录过期，请重新登录", 403

        UserModel.query.filter_by(id=user_id).delete()
        db.session.commit()

    # 根据id修改除了邮箱和密码之外的属性
    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str, location="headers")
        parser.add_argument('username', type=str, location="form")
        parser.add_argument('real_name', type=str, location="form")
        parser.add_argument('avatar', type=str, location="form")
        parser.add_argument('purchased', type=str, location="form")
        parser.add_argument('card_number', type=str, location="form")

        # token验证
        input_token = parser.parse_args().token
        token = redis_token.get(user_id)
        if input_token is None or token is None or input_token != token.decode("utf8"):
            return "登录过期，请重新登录", 403

        user = UserModel.query.get(user_id)

        args = parser.parse_args()
        for k, v in args.items():
            if v is not None:
                setattr(user, k, v)
        db.session.commit()


api.add_resource(Register, "/register")
api.add_resource(Captcha, "/captcha")
api.add_resource(Login, "/login")
api.add_resource(ResetPassword, "/reset-password")
api.add_resource(UserInfo, "/users/<string:user_id>")
