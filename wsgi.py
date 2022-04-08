import click
from flask import Flask
from flask.cli import with_appcontext
import csv

from App.database import create_db
from App.main import app, migrate
from App.controllers import ( create_user, get_all_users_json )
from App.database import db
from App.models import Programme

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

@app.cli.command("populate-db")
def populate(): 
    with open('App\programs.csv') as file:
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

@app.cli.command("create-profile")
@click.argument('first_name')
@click.argument('last_name')
@click.argument('programme_id')
@click.argument('grad_year')
def create_profile():
    pass # to finish