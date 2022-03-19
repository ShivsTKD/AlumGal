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
    authenticate
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/login', methods=['GET'])
def get_login_page():
    form = Login()
    return render_template('login.html', form=form)

@user_views.route('/signup', methods=['GET'])
def get_signup_page():
    form = SignUp()
    options = Programme.query.all()
    programmes = ['Comp Sci', 'Mathematics']
    degrees = ['B.Sc.', 'M.Sc.']
    grad_years = ['2020', '2021', '2022']
    for option in options:
        if option['name'] not in programmes:
            programmes.append(option['name'])
    form.programme.choices = programmes
    form.degree.choices = degrees
    form.grad_year.choices = grad_years
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
    fields = dict()
    form = AdvSearch()
    #need to add choice for each select field
    data = request.form()
    results=[]
    for key in data:
        if data[key] != None:
            fields[key] = data[key]

    profiles = db.session.query(
        Profile.first_name, 
        Profile.last_name,
        Programme.name,
        Programme.department,
        Profile.graduation_year
    ).join(Profile).join(Programme).all()

    for attr, value in fields.items():
        profiles = profiles.filter(getattr(form, attr).like("%%%s%%" % value))

    for item in profiles:
        results.append(item.__dict__())
    return  results

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