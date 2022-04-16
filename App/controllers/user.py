from App.models import User,Profile,Programme
from App.database import db
from sqlalchemy.exc import IntegrityError
from App.controllers import firebaseconfig
import os

def get_all_users():
    return User.query.all()

def get_user(username):
    return User.query.get(username)

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

def create_profile(email,profile_data,filename):
    try:
        prog = Programme.query.filter_by(name = profile_data['programme'], degree = profile_data['degree']).first()
        user = User.query.filter_by(email = email).first()
        token = firebaseconfig.storage.child(f'Userpics\{user.id}').put(f"images\{filename}")
        purl = firebaseconfig.storage.child(f'Userpics\{user.id}').get_url(token['downloadTokens'])
        profile = Profile(
                uid = user.id,
                first_name = profile_data['first_name'],
                last_name = profile_data['last_name'],
                programme_id = prog.id,
                graduation_year = profile_data['grad_year'],
                facebook = profile_data['fb'],
                instagram =profile_data['ig'],
                linkedin = profile_data['l_in'],
                url = f"{purl}"
                
        )
        db.session.add(profile)
        db.session.commit()
        os.remove(f"images\{filename}")
        return True
    except(Exception):
        User.query.filter_by(email = email).delete()
        db.session.commit()
        os.remove(f"images\{filename}")
        print ("deleted user")
        return False

def user_profile_create(form,filename):
    done = create_user(form["username"],form["password"],form["email"])
    
    if done:
        y = create_profile(form['email'],form,filename)
        
        if y:
            return True
        else:
            return False
    else:
        return False    
