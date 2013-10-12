"""
/v1/users/ endpoint
"""
from flask import request
from flask.ext.restful import Resource


class BaseUser(Resource):
    db = 'some shared functionality'


class Users(BaseUser):
    def get(self):

        return 'get ok!'

    def post(self):
        data = request.json

        return data


class User(BaseUser):
    def get(self, user_id):

        return {"a user ": user_id}
