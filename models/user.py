from dataclasses import dataclass
from datetime import datetime
import shortuuid
from werkzeug.security import generate_password_hash
from exts import db


# 将ORM模型映射到数据库三部曲
# 0. migrate = Migrate(app, db)
# 1. 初始化迁移仓库：flask db init
# 2. 将orm模型生成迁移脚本：flask db migrate
# 3. 运行迁移脚本，生成表：flask db upgrade

@dataclass
class UserModel(db.Model):
    id: str
    email: str
    username: str
    password: str
    real_name: str
    avatar: str
    signature: str
    purchased: str
    card_number: str
    join_time: str

    __tablename__ = "users"
    id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(200), nullable=False)
    real_name = db.Column(db.String(50))
    avatar = db.Column(db.String(100))
    signature = db.Column(db.String(100))
    purchased = db.Column(db.Boolean, default=False)
    card_number = db.Column(db.String(16))
    join_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        if "password" in kwargs:
            self.password = kwargs["password"]
            kwargs.pop("password")
        super(UserModel, self).__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = generate_password_hash(new_password)
