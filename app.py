from flask import Flask
from exts import db, redis_captcha, mail, redis_token, redis_email_limit
from flask_migrate import Migrate
from blueprints.course_blueprint import class_bp
from blueprints.user_blueprint import login_bp
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
app.register_blueprint(login_bp)
app.register_blueprint(class_bp)


@app.route('/')
def hello_world():
    return "HELLO WORLD"


if __name__ == '__main__':
    app.run(port=667)
