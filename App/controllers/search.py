from App.models import Profile, Programme
from App.database import db

def user_search(name):
    if name.count(' ') == 0:
        if name[0].islower():
            name = name.capitalize()
        user = Profile.query.filter_by(last_name=name).all()
        if len(user) == 0:
            user = Profile.query.filter_by(first_name=name).all()
            if len(user) == 0:
                return None
            else:
                return user
        else:
            return user
    if name.count(' ')  == 1:
        parts = name.split()
        if parts[0].islower():
            parts[0] = parts[0].capitalize()
        if parts[1].islower():
            parts[1] = parts[1].capitalize()
        user = Profile.query.filter_by(first_name=parts[0], last_name = parts[1])
        if len(user.all()) != 0:
            return user.all()  
        else:
            user = Profile.query.filter_by(first_name=parts[1], last_name = parts[0])
            if len(user.all()) != 0:
                return user.all()
            return None
    else:
         return 'Invalid'

def adv_search(fields):
    valid_fields = dict()
    profile = db.session.query(Profile)
    for key in fields:
        if fields[key] is not None and fields[key] != '':
            valid_fields[key] = fields[key]

    if 'last_name' in valid_fields:
        profile = profile.filter_by(last_name = valid_fields['last_name'])
    if 'first_name' in valid_fields:
        profile = profile.filter_by(first_name = valid_fields['first_name'])   
    if 'graduation_year' in valid_fields:
        profile = profile.filter_by(graduation_year = valid_fields['graduation_year'])
    if 'degree' in valid_fields:
        profile = profile.filter(Profile.programme.has(degree = valid_fields['degree']))
    if 'name' in valid_fields:
        profile = profile.filter(Profile.programme.has(name = valid_fields['name']))

    obj = profile.all()
    return obj
    