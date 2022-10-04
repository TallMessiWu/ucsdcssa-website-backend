from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

db = SQLAlchemy()
redis_captcha = FlaskRedis(config_prefix="CAPTCHA")
redis_token = FlaskRedis(config_prefix="TOKEN")
redis_email_limit = FlaskRedis(config_prefix="EMAIL_LIMIT")
mail = Mail()
