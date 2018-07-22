from app import app, db

from models import *

def create_tables():
    with db:
        db.create_tables([User, Roles])


if __name__ == '__main__':
    create_tables()
    app.run()