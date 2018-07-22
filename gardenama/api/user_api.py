from flask import jsonify, request, Response
from flask_restful import Resource
from app import db
from models import User, Role
from werkzeug.security import generate_password_hash
from peewee import IntegrityError
from playhouse.shortcuts import model_to_dict
import json


class UsersApi(Resource):
    def post(self):
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        try:
            role = Role.create(name='Unverified')
        except Exception as e:
            response = jsonify({"err": "Can\'t create role: %s" % e})
            response.status_code = 400
            return response

        try:
            user = User.create(email=email, username=email,
                               password=password, role=role)
        except Exception as e:
            response = jsonify({"err": "Can't create user: %s" % e})
            response.status_code = 400
            return response

        response = jsonify({"res": "User created:"})
        response.status_code = 201
        return response


class UserApi(Resource):
    def get(self, user_id):
        try:
            user = User.get(User.id == user_id)
        except Exception as e:
            response = jsonify({"err": "User not found"})
            response.status_code = 404
            return response

        response = jsonify(model_to_dict(user))
        response.status_code = 200

        return response
