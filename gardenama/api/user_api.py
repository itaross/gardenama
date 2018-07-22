from flask import jsonify, request, Response
from flask_restful import Resource
from app import db
from models import User, Role
from werkzeug.security import generate_password_hash
from peewee import IntegrityError
from playhouse.shortcuts import model_to_dict

class UsersApi(Resource):
    def post(self):
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        try:
            role = Role.create(name='Unverified')
        except Exception as e:
            response = Response(
                response=jsonify(dict(err="Cannot create role: %s" % e)),
                status = 400,
                mimetype='application/json'
            )
            return (response.response, response.status, response.headers.items())

        try:
            user = User.create(email=email, username=email, password=password, role=role)
        except Exception as e:
            response = Response(
                response=jsonify(dict(err="Cannot create role: %s" % e)),
                status = 400,
                mimetype='application/json'
            )
            
            return (response.response, response.status, response.headers.items())


        response = Response(
                response=jsonify(dict(res="User crated.")),
                status = 201,
                mimetype='application/json'
            )
        
        return (response.response, response.status, response.headers.items())


class UserApi(Resource):
    def get(self, user_id):
        try:
            user = User.get(User.id == user_id)
        except:
            respose = Response(
                response=jsonify(dict(err="User not found: %s" % e)),
                status = 404,
                mimetype='application/json'
            )
            
            return (response.response, response.status, response.headers.items())


        print(jsonify(model_to_dict(user)))

        response = Response(
                response=jsonify(model_to_dict(user)),
                status = 200,
                mimetype='application/json'
            )
        print(response)

        return (response.response, response.status, response.headers.items())
