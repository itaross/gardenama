from peewee import Model
from peewee import SqliteDatabase
from gardenama.gardenama.config import DB_NAME

database = SqliteDatabase(DB_NAME)

class BaseModel(Model):
    class Meta:
        database = database