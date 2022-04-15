from App.models import User,Profile,Programme
from App.database import db
from sqlalchemy.exc import IntegrityError

def get_all_users():
    return User.query.all()

def get_user(username):
    return User.query.filter_by(username=username).first()

def create_user(username, password, email):
    newuser = User(username=username, password=password, email=email)
    try:
        db.session.add(newuser)
        db.session.commit()
        return True
    except IntegrityError:
        print("test")
        return False


def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

def create_profile(email,profile_data):
    try:
        user = User.query.filter_by(email = email).first()
        prog = Programme.query.filter_by(name = profile_data['Programme'], degree = profile_data['Degree']).first()
        profile = Profile(
                uid = user.id,
                first_name = profile_data['First Name'],
                last_name = profile_data['Last Name'],
                programme_id = prog.id,
                graduation_year = profile_data['Graduation Year'],
                facebook = profile_data['Facebook'],
                instagram =profile_data['Instagram'],
                linkedin = profile_data['LinkedIn']
        )
        db.session.add(profile)
        db.session.commit()
        return True
    except(Exception):
        return False