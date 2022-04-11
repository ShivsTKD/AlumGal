import click
from flask import Flask
from flask.cli import with_appcontext
import csv

from App.database import create_db
from App.main import app, migrate
from App.controllers import ( create_user, get_all_users_json )
from App.database import db
from App.models import Programme,User,Profile

@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

@app.cli.command("create-user")
@click.argument("username")
@click.argument("password")
@click.argument("email")
def create_user_command(username, password, email):
    done = create_user(username, password, email)
    if done == False:
        print('create user failed!')
    else:
        print(f'{username} created!')

@app.cli.command("get-users")
def get_users():
    print(get_all_users_json())

@app.cli.command("populate-programme")
def populate(): 
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
        print( 'populated Programme table')

@app.cli.command("populate-profile")
def populate():
    with open(r'App\user.csv') as file:
        fieldnames = ['Username','First Name','Last Name','Full Name','Email','Password','Programme','Degree','Department','Faculty','Graduation Year','Facebook','Instagram','LinkedIn']
        reader = csv.DictReader(file,fieldnames = fieldnames)
        for row in reader:
            newUser = create_user(row['Username'],row['Password'], row['Email'])
            if newUser:
                user = User.query.filter_by(email = row['Email']).first()
                pro = Programme.query.filter_by(name = row['Programme'], degree = row['Degree']).first()
                newProfile = Profile(
                    uid = user.id,
                    first_name = row['First Name'],
                    last_name = row['Last Name'],
                    programme_id = pro.id,
                    graduation_year = row['Graduation Year'],
                    facebook = row['Facebook'],
                    instagram =row['Instagram'] ,
                    linkedin = row['LinkedIn'] ,
                    #this is a default profile image feel free to change it
                    url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngitem.com%2Fmiddle%2FmJiimi_my-profile-icon-blank-profile-picture-circle-hd%2F&psig=AOvVaw0tbLmV-hhBSTm92wB8ecUb&ust=1649787437823000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCNjcjqPPjPcCFQAAAAAdAAAAABAD"

                )
                db.session.add(newProfile)
                db.session.commit()
    print("users profiles created successfully")

