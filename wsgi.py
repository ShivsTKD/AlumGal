import click
from flask import Flask
from flask.cli import with_appcontext
import csv
from os import listdir
from App.database import create_db
from App.main import app, migrate
from App.controllers import ( create_user, get_all_users_json )
from App.database import db
from App.models import Programme,User,Profile
from App.controllers import storage

@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

@app.cli.command("create-user")
@click.argument("username")
@click.argument("password")
@click.argument("email")
def create_user_command(username, password, email):
    create_user(username, password, email)
    print(f'{username} created!')

@app.cli.command("get-users")
def get_users():
    print(get_all_users_json())


def programmes(): 
    with open(r'App\programs.csv') as file:
        fieldnames = ['Programme','Degree','Department','Faculty']
        reader = csv.DictReader(file,fieldnames=fieldnames)
        for row in reader:
            pro = Programme(
                name = row['Programme'] ,
                degree =row['Degree']  ,
                department =row['Department'] ,
                faculty =row['Faculty']
            )
            db.session.add(pro)
            db.session.commit()
        print( 'programmes added')

def  userprofile():
    with open(r'App\user.csv') as file:
        fieldnames = ['Username','First Name','Last Name','Full Name','Email','Password','Programme','Degree','Department','Faculty','Graduation Year','Facebook','Instagram','LinkedIn']
        reader = csv.DictReader(file,fieldnames=fieldnames)
        for row in reader:
            newUser = create_user(row['Username'],row['Password'],row['Email'])
            if newUser:
                user = User.query.filter_by(email = row['Email']).first()
                prog = Programme.query.filter_by(name = row['Programme'], degree = row['Degree']).first()
                profile = Profile(
                    uid = user.id,
                    first_name = row['First Name'],
                    last_name = row['Last Name'],
                    programme_id = prog.id,
                    graduation_year = row['Graduation Year'],
                    facebook = row['Facebook'],
                    instagram =row['Instagram'],
                    linkedin = row['LinkedIn']
                )
                db.session.add(profile)
                db.session.commit()
    print ("users added")

def propics():
    images = listdir('Userpics')
    names = []
    for image in images:
        names.append(image.strip('.jpg'))
    ids = []
    for name in names:
        parts = name.split()
        user = User.query.filter_by(first_name = parts[0], last_name = parts[1])
        ids.append(user.id)
    for id in ids:
        profile = Profile.query.filter_by(uid = id)
        profile.url = storage.child(f'Userpics\{names[id]}.jpg').add(f'{names[id]}.jpg',user[f'{id}'])
        db.session.commit()
    print("images added")

@app.cli.command("populate-db")
def populate():
    print("populating...")
    programmes()
    userprofile()
    propics()
    print("populating completed")


@app.cli.command("delete")
@click.argument("email")
def delete(email):
    User.query.filter_by(email = email).delete()
    db.session.commit()
    print ("deleted user")
