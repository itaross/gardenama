from flask import Flask
from peewee import SqliteDatabase
from conf import DB_NAME

app = Flask(__name__)
db = SqliteDatabase(DB_NAME)
