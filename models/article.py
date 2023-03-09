from dataclasses import dataclass
from exts import db
from datetime import datetime


@dataclass
class ArticleModel(db.Model):
    id: str
    title: str
    link: str
    cover: str
    create_time: datetime
    categories: str
    # 这个决定文章在头条的顺序，值越小越靠前
    headline_index: int

    __tablename__ = "articles"
    id = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(200), nullable=False)
    cover = db.Column(db.String(200), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    categories = db.Column(db.String(100), nullable=True)
    headline_index = db.Column(db.Integer, nullable=True)

    def __init__(self, *args, **kwargs):
        super(ArticleModel, self).__init__(*args, **kwargs)
