from flask_restful import Resource, reqparse
from flask import jsonify, abort
from gardenama.gardenama.models.user import User
import datetime
import json

class UserListAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type = str, location = 'json')
        self.reqparse.add_argument('password', type = str, location = 'json')
        self.reqparse.add_argument('email', type = str, location = 'json')
        super(UserListAPI, self).__init__()

    def get(self):
        users = User.select()
        ret = []

        for user in users:
            ret.append(user.to_dict())

        return jsonify(ret)

    def post(self):
        args = self.reqparse.parse_args()
        args.join_date = datetime.datetime.now()
        args.delete_date = None
        args.enabled = False

        User.create(**args).save()

        return 201  



class UserAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type = str, location = 'json')
        self.reqparse.add_argument('password', type = str, location = 'json')
        self.reqparse.add_argument('email', type = str, location = 'json')
        super(UserAPI, self).__init__()

    def get(self, id):
        ret = [user for user in User.select().where(User.id == id)]

        if(len(ret) == 0):
            # User not found
            abort(404)

        return jsonify(ret[0].to_dict())

    def put(self, id):
        user = User.select().where(User.id == id)
        args = self.reqparse.parse_args()
        
        if(len(list(user)) == 0):
            args.join_date = datetime.datetime.now()
            args.enabled = False
        
        User.create(**args).save()
    
        return 200

    def delete(self, id):
        pass