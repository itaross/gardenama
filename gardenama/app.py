from flask import Flask
from peewee import SqliteDatabase
from gardenama.gardenama.conf import *

app = Flask(__name__)
db = SqliteDatabase(DB_NAME)