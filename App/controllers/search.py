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
        print(parts)
        user = Profile.query.filter_by(first_name=parts[0], last_name = parts[1])
        if len(user.all()) != 0:
            print('check') 
            return user.all()  
        else:
            user = Profile.query.filter_by(first_name=parts[1], last_name = parts[0])
            if len(user.all()) != 0:
                print('check') 
                return user.all()
            return None
    else:
         return 'Invalid'

def adv_search(fields):
    valid_fields = dict()
    results = []
    profile = db.session.query(Profile)
    for key in fields:
        if fields[key] is not None and fields[key] != '':
            valid_fields[key] = fields[key]
    
    print(valid_fields)

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
    print(obj)

    for  i in obj:
        print( i.first_name, i.last_name)

    
    
    # for attr,key in valid_fields.items():
    #     if key == 'graduation_year':
    #         profiles = Profile.query.filter_by(graduation_year=int(key))
    #     else:
    #         profiles = profiles.filter(getattr(Profile, attr).like("%%%s%%" % key)).all()

    #     if key == 'name' or key == 'degree':
    #         progs = Programme.query.filter(getattr(Programme, "%").like("%%%s%%" % valid_fields[key])).all()

    # if progs:
    #     for p in progs:
    #         results.append(p.profiles)
        

    # for profile in profiles:
    #     results.append(profile.toDict())

    return None
    