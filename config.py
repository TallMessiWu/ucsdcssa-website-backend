import os
import secretes

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

JSON_AS_ASCII = False

# mysql数据库
DB_USERNAME = "root"
DB_PASSWORD = secretes.DB_PASSWORD
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "ucsdcssa_website"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

# SQLALCHEMY配置
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# redis数据库
CAPTCHA_URL = "redis://@localhost:6379/0"
TOKEN_URL = "redis://@localhost:6379/1"

# 邮件配置
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = False
MAIL_USERNAME = secretes.MAIL_USERNAME
MAIL_PASSWORD = secretes.MAIL_PASSWORD
MAIL_DEFAULT_SENDER = secretes.MAIL_DEFAULT_SENDER