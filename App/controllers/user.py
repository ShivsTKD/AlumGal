from App.models import User
from App.database import db


def get_all_users():
    return User.query.all()

def create_user(username, password, email):
    newuser = User(username=username, password=password, email=email)
    try:
        db.session.add(newuser)
        db.session.commit()
        return True
    except IntegrityError:
        return False


def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users