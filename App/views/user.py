from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from App.forms import *

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    authenticate
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


# @user_views.route('/users', methods=['GET'])
# def get_user_page():
#     users = get_all_users()
#     return render_template('users.html', users=users)

@user_views.route('/login', methods=['GET'])
def get_login_page():
    return render_template('login.html')

@user_views.route('/signup', methods=['GET'])
def get_signup_page():
    form = ProfileForm()
    form.programme.choices = [(p.id,p.name)for p in Programme.query.order_by('name')]
    # programmes
    # degrees
    # departments
    return render_template('signup.html')

@user_views.route('/signup', methods=['POST'])
def post_signup_info():
    form = SignUp()
    if form.validate_on_submit():
        data = request.form
        done = create_user(username = data['username'], password = data['password'],email = data['email'])
        if done:
            alert('Signup successful')
        else:
            alert('username or email already in use')
    return render_template('page.html',form=form) #change page to whatever template

@user_views.route('/login', methods = ['POST'])
def account_login():
    form = LoginForm()
    if form.validate_on_submit():
        data = request.form
        user = authenticate(username = data['username'], password = data['password'])
        if user:
            login_user(user)
            alert('Login successful')
        else:
            alert('Wrong username or password')

    return render_template('page.html', form = form) #change page to whatever template

@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/lol')
def lol():
    return 'lol'

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')