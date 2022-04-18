from App.models import Profile
from App.database import db

def user_search(name):
    results = []
    if name.count(' ') == 0:
        user = Profile.query.filter_by(last_name=name).all()
        if user == None:
            user = Profile.query.filter_by(first_name=name).all()
            if user == None:
                return None
            else:
                for u in user:
                  results.append(u.toDict)
                return results
        else:
            for u in user:
                results.append(u.toDict)
            return results     
    if name.count(' ')  == 1:
        parts = name.split()
        user = Profile.query.filter_by(first_name=parts[0])
        if user == None:
            user = Profile.query.filter_by(first_name=parts[1])
            if user == None:
                return None
            user = user.filter_by(last_name=parts[0])
            if user == None:
                return None
            for u in user:
                results.append(u.toDict)
            return results    
        else:
            user = user.filter_by(last_name=parts[1])
            if user == None:
                return None
            for u in user:
                results.append(u.toDict)
            return results   
    else:
         return 'Invalid'




        
            
    else:

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
    