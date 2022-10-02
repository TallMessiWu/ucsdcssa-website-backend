import json
import os

from flask import Blueprint, send_file
from flask_restful import Api, Resource, reqparse

from config import SITE_ROOT
from exts import redis_token

class_bp = Blueprint("class", __name__)
api = Api(class_bp)


class CourseList(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str, location="headers", required=True)
        parser.add_argument('id', type=str, location="headers", required=True)
        args = parser.parse_args()
        print(args)
        # token验证
        input_token = args.token
        token = redis_token.get(args.id)
        if input_token is None or token is None or input_token != token.decode("utf8"):
            return "登录过期，请重新登录", 403

        json_url = os.path.join(SITE_ROOT, 'assets', 'courses_grouped.json')
        print(json_url)
        with open(json_url, encoding="utf8") as f:
            courses_grouped = json.load(f)
        return courses_grouped


class CourseQRCode(Resource):
    def get(self, class_name):
        return send_file(os.path.join(SITE_ROOT, 'assets/courses-qr-codes', '{}.jpg'.format(class_name)))


class AssistantQRCode(Resource):
    def get(self, id):
        return send_file(os.path.join(SITE_ROOT, 'assets', '小助手{}.jpg'.format(id)))


api.add_resource(CourseList, "/courses")
api.add_resource(CourseQRCode, "/courses/<string:class_name>")
api.add_resource(AssistantQRCode, "/assistants/<int:id>")
