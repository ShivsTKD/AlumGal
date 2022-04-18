from App.models import Profile
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




        
            
    # else:

    # elif fname != None and lname == None :
    #     #search by first name
    #     user = Profile.query.filter_by(first_name=fname).all
        
    # else:
    #     #search by both first and last names
    #     user = Profile.query.filter_by(first_name = fname,last_name=lname).all()
    
    # if user == None:
    #     return None

    # for u in user:
    #     results.append(u.toDict)
    # return results

def adv_search(fields):
    valid_fields = dict()
    results = []
    profiles = Profile.query.all()
    for key in fields:
        if fields[key] != None:
            vaild_fields[key] = fields[key]
    
    for key, value in valid_fields.items:
        profiles = profiles.filter(getattr(form, attr).like("%%%s%%" % value))
    
    for profile in profiles:
        results.append(profile.toDict)

    return results
    