from flask_restful import Api
from app import app
from conf import *
from .user_api import UsersApi, UserApi


api = Api(app)

api.add_resource(UsersApi, BASE_URL + 'users')
api.add_resource(UserApi, BASE_URL + 'user/<int:user_id>')
