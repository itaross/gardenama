from app import app, db
from api import api

from models import *

def create_tables():
    with db:
        db.create_tables([Role, User])


if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
