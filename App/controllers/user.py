from App.models import User,Profile,Programme
from App.database import db


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

def create_profile(id,profile_data):
    pid = Programme.query.filter_by(name = profile_data.programme).first()
    newProfile = Profile(
    uid = id ,
    first_name = profile_data.first_name,
    last_name = profile_data.last_name ,
    programme_id = pid.id ,
    graduation_year = profile_data.grad_year,
    facebook = profile_data.fb,
    instagram = profile_data.ig,
    linkedin = profile_data.l_in,
    #url = 
    
    )
    try:
        db.session.add(newProfile)
        db.session.commit()
        return True
    except DatabaseError:
        return False



def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users