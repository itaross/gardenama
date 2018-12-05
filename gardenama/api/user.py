from flask_restful import Resource, reqparse
from flask import jsonify, abort
from gardenama.gardenama.models.user import User
from gardenama.gardenama.api import utils
import datetime
import json
import peewee

def creatBasicUserParser():
    parser = reqparse.RequestParser()
    parser.add_argument('username', type = str, location = 'json', required=True)
    parser.add_argument('password', type = str, location = 'json', required=True)
    parser.add_argument('email', type = str, location = 'json', required=True)
    return parser


class UserListAPI(Resource):
    def __init__(self):
        self.parser = creatBasicUserParser()
        super(UserListAPI, self).__init__()

    def get(self):
        users = User.select()
        ret = []

        for user in users:
            ret.append(user.to_dict())

        return utils.make_api_response(200, ret)


    def post(self):
        # creating a new user
        args = self.parser.parse_args()
        args.join_date = datetime.datetime.now()
        args.enabled = False

        try: 
            user = User.create(**args)
            user.save()
            # remove password to returned object
            user.password = ""
            ret = user.to_dict()
            code = 201
        except peewee.IntegrityError as error:
            ret = {"message": str(error)} 
            code = 400

        return utils.make_api_response(code, ret)  


class UserAPI(Resource):

    def __init__(self):
        super(UserAPI, self).__init__()

    def get(self, id):
        ret = [user for user in User.select().where(User.id == id)]

        if(len(ret) == 0):
            ret = utils.make_api_response(400, {"message": "User not found."}) # User not found
        else:
            ret = utils.make_api_response(201, jsonify(ret[0].to_dict()))
        
        return ret

    def put(self, id):
        parser = creatBasicUserParser()
        user = User.select().where(User.id == id)

        if(len(list(user)) == 0):
            # we are creating a new resource with the given id 
            args = parser.parse_args()
            args.join_date = datetime.datetime.now()
            args.enabled = False
        else:
            # we are changing the entire existing resource, so request more required fields
            parser.add_argument('join_date', type = str, location = 'json', required=True)
            parser.add_argument('enabled', type=bool, location ='json', required=True)
            # this is already returning a 400 status code with message, if the are parsing problems
            args = parser.parse_args()

        try:
            user = User.create(**args)
            user.save()
            user.password = ""
            ret = user.to_dict()
            code = 201
        except peewee.IntegrityError as error:
            ret = {"message": str(error)} 
            code = 400

        return utils.make_api_response(code, ret)

    def delete(self, id):
        # retrieve the selected user if existing
        user = User.delete().where(User.id == id).execute()

        # user not found
        if(user == 0):
            ret = utils.make_api_response(400, {"message": "User not found."}) # User not found
        else:
            ret = utils.make_api_response(200, {"message": "User deleted"})

        return ret