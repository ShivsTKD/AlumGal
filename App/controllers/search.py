from App.models import Profile
from App.database import db

def search(fname,lname):
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

def advsearch():
    pass