from .base import BaseModel
from peewee import CharField, DateTimeField, BooleanField
import datetime

class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField(unique=True)
    join_date = DateTimeField()
    confirm_date = DateTimeField(null=True)
    delete_date = DateTimeField(null=True)
    enabled = BooleanField()

    def to_dict(self):
        return {
            "id" : self.get_id(),
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "join_date": str(self.join_date),
            "delete_date": str(self.delete_date),
            "enabled": self.enabled
        }