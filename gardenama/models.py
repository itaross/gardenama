import datetime
from peewee import *
from app import db

class BaseModel(Model):
      class Meta():
        database = db

class Role(BaseModel):
    name = CharField()
    # this field is needed for an user to read data and check status of the system
    can_read = BooleanField(default=False)
    # this field is needed to enable operations on the gardening devices
    can_garden = BooleanField(default=False)

class User(BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    is_enabled = BooleanField(default=False)
    is_banned = BooleanField(default=True)
    role = ForeignKeyField(model=Role, backref='users')
    date_created = DateTimeField(default=datetime.datetime.now)
    last_login = DateTimeField(null=True)