from App.models import Profile
from App.database import db

def user_search(fname,lname):
    results = []
    if fname == None and lname != None:
        #search by last name
        user = Profile.query.filter_by(last_name=lname).all()
        
    elif fname != None and lname == None :
        #search by first name
        user = Profile.query.filter_by(first_name=fname).all
        
    else:
        #search by both first and last names
        user = Profile.query.filter_by(first_name = fname,last_name=lname).all()
    
    for u in user:
        results.append(u.toDict)
    return results

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
    