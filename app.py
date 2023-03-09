from flask import Flask
from exts import db, redis_captcha, mail, redis_token, redis_email_limit
from flask_migrate import Migrate
from blueprints.course_blueprint import course_bp
from blueprints.user_blueprint import user_bp
from blueprints.department_blueprint import department_bp
from blueprints.article_blueprint import article_bp
from flask_cors import CORS

import config

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
redis_captcha.init_app(app)
redis_token.init_app(app)
redis_email_limit.init_app(app)

mail.init_app(app)
migrate = Migrate(app, db)
CORS(app)

# 注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(course_bp)
app.register_blueprint(department_bp)
app.register_blueprint(article_bp)


@app.route('/')
def hello_world():
    return '欢迎来到UCSD CSSA后端，具体接口请参考GitHub仓库里的README.md。'


if __name__ == '__main__':
    app.run(port=667)
