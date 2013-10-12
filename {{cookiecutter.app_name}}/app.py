import werkzeug
import gevent
import os
from flask import Flask
from flask.ext.restful import Api
from {{cookiecutter.package_namespace}}.{{cookiecutter.app_name}}.users import User, Users

app = Flask(__name__)
api = Api(app, prefix='/v1', catch_all_404s=True)

# routing
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
