#!flask/bin/python
from flask import Flask
from flask_restful import Api, Resource
from .api.user import UserAPI, UserListAPI
from .models.base import database
from .models.user import User

app = Flask(__name__)
api = Api(app)

def create_tables():
    with database:
        database.create_tables([User]) 

create_tables()
api.add_resource(UserListAPI,'/users/')
api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user') 