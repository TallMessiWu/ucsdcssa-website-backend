import json
import os

from flask import Blueprint, send_file
from flask_restful import Api, Resource
from config import SITE_ROOT

department_bp = Blueprint("department", __name__)
api = Api(department_bp)


class Department(Resource):
    def get(self, department_name):
        json_url = os.path.join(SITE_ROOT, 'assets', 'department.json')
        with open(json_url, encoding="utf8") as f:
            department = json.load(f)
        return department[department_name]


class Member(Resource):
    def get(self, department_name, member_name):
        json_url = os.path.join(SITE_ROOT, 'assets', 'department.json')
        with open(json_url, encoding="utf8") as f:
            department = json.load(f)
        return send_file(
            os.path.join(
                SITE_ROOT,
                "assets/members-photos",
                department[department_name]["members"][member_name]["photoSrc"]
            )
        )


class GroupPhoto(Resource):
    def get(self, department_name):
        return send_file(
            os.path.join(
                SITE_ROOT,
                "assets/departments-group-photos",
                "{}合照.jpg".format(department_name)
            )
        )


api.add_resource(Department, "/department/<string:department_name>")
api.add_resource(Member, "/member/<string:department_name>/<string:member_name>")
api.add_resource(GroupPhoto, "/group-photo/<string:department_name>")
