from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from flask_login import login_required
from App.forms import *
from App.models import *

from App.controllers import (
    create_user, 
    get_user,
    get_all_users,
    get_all_users_json,
    login_user,
    logout_user,
    authenticate,
    user_search,
    adv_search
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/login', methods=['GET'])
def get_login_page():
    form = Login()
    return render_template('login.html', form=form)

@user_views.route('/signup', methods=['GET'])
def get_signup_page():
    form = SignUp()
    return render_template('signup.html', form=form)

@user_views.route('/signup', methods=['POST'])
def post_signup_info():
    form = SignUp(request.form)
    image = request.files['img']
    filename = photos.save(image, name=f"{1}.jpg")
    return filename
    # if form.validate_on_submit():
    #     data = request.form
    #     done = create_user(username = data['username'], password = data['password'],email = data['email'])
    #     if done:
    #         alert('Signup successful')
    #     else:
    #         alert('username or email already in use')
    # return render_template('page.html',form=form) #change page to whatever template

@user_views.route('/login', methods = ['POST'])
def account_login():
    form = Login(request.form)
    if form.validate_on_submit():
        return 'This is it'
    return jsonify(form.data)
    # if form.validate_on_submit():
    #     data = request.form
    #     user = authenticate(username = data['username'], password = data['password'])
    #     if user:
    #         login_user(user, remember = True)
    #         alert('Login successful')
    #     else:
    #         alert('Wrong username or password')

    # return render_template('page.html', form = form) #change page to whatever template

@user_views.route('/logout', methods=['GET'])
@login_required
def account_logout():
    logout_user()
    alert('Logout successful')
    return redirect('/login')

@user_views.route('/advsearch', methods=['GET'])
@login_required
def advsearch():
    
    form = AdvSearch()
    data = request.form.to_dict()
    results = adv_search(data)
    return results


@user_views.route('/search/<fname>+<lname>', methods=['GET'])
@login_required
def user_search(fname, lname):
    #search by first name , last name or both
    result = search(fname,lname)
    return result

@user_views.route('/users', methods=['GET'])
def list_users():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/users/<username>', methods=['GET'])
def get_user_page(username):
    user = get_user(username)
    return render_template('user.html', user=user)

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