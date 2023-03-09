import json
import time

import requests
from flask import Blueprint, jsonify, make_response
from flask_restful import Api, Resource

import classified
from exts import db
from models.article import ArticleModel
from datetime import datetime

article_bp = Blueprint("article", __name__)
api = Api(article_bp)


class CrawlArticles(Resource):
    def get(self, num):
        """
        获取微信公众号文章

        参考文章：https://www.mianshigee.com/note/detail/38130ncd/

        :param cookie: 从浏览器里复制过来的cookie
        :param token: 从浏览器里复制过来的token
        :param num: 需要的文章数量
        :return:
        """
        url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
        headers = {
            "Cookie": classified.COOKIE,
            "User-Agent": 'Mozilla/5.0 (Linux; Android 10; YAL-AL00 Build/HUAWEIYAL-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.64 HuaweiBrowser/10.0.1.335 Mobile Safari/537.36'
        }

        # 公众号名字：可自定义
        keyword = 'UCSD中国学生学者联合会'
        search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?action=search_biz&begin=0&count=5&query={}&token={}&lang=zh_CN&f=json&ajax=1'.format(
            keyword, classified.TOKEN
        )
        doc = requests.get(search_url, headers=headers).text
        jstext = json.loads(doc)
        fakeid = jstext['list'][0]['fakeid']

        data = {
            "token": classified.TOKEN,
            "lang": "zh_CN",
            "f": "json",
            "ajax": "1",
            "action": "list_ex",
            "begin": 0,
            "count": "5",
            "query": "",
            "fakeid": fakeid,
            "type": "9",
        }
        article_list = []
        # 获取文章
        for i in range(0, num, 5):
            data['begin'] = i
            response_json = requests.get(url, headers=headers, params=data).text
            articles = [{
                "aid": article['aid'],
                "title": article['title'],
                "link": article['link'],
                "cover": article['cover'],
                "create_time": article['create_time']
            } for article in json.loads(response_json)['app_msg_list']]
            article_list += articles
            time.sleep(5)

        # 加入数据库
        for article in article_list:
            if ArticleModel.query.get(article["aid"]):
                continue
            article_instance = ArticleModel(id=article["aid"], title=article["title"], link=article["link"],
                                            cover=article["cover"],
                                            create_time=datetime.fromtimestamp(article["create_time"]))
            db.session.add(article_instance)
        db.session.commit()

        # 这里返回使用make_response是因为直接返回中文字符串会显示乱码。
        return make_response("文章获取成功", 200)


class Articles(Resource):
    def get(self, offset_num, category):
        if category == "全部":
            return jsonify(
                ArticleModel.query.order_by(ArticleModel.create_time.desc()).limit(20).offset(offset_num).all())
        else:
            return jsonify(ArticleModel.query.filter(ArticleModel.categories.contains(category)).order_by(
                ArticleModel.create_time.desc()).limit(20).offset(offset_num).all())


class Headlines(Resource):
    def get(self):
        return jsonify(ArticleModel.query.filter(ArticleModel.headline_index.isnot(None)).order_by(
            ArticleModel.headline_index).all())


api.add_resource(CrawlArticles, "/crawl-articles/<int:num>")
api.add_resource(Articles, "/articles/<int:offset_num>/<string:category>")
api.add_resource(Headlines, "/headlines")
