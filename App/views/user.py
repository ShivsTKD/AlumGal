from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from App.forms import *
from App.models import *

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    login_user,
    logout_user,
    authenticate
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


# @user_views.route('/users', methods=['GET'])
# def get_user_page():
#     users = get_all_users()
#     return render_template('users.html', users=users)

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
    departments = ['DCIT', 'DM']
    faculties = ['FST', 'FSS']
    for option in options:
        if option['name'] not in programmes:
            programmes.append(option['name'])
        if option['degree'] not in programmes:
            degrees.append(option['degree'])
        if option['department'] not in programmes:
            departments.append(option['department'])
        if option['faculty'] not in programmes:
            faculties.append(option['faculty'])
    form.programme.choices = programmes
    form.degree.choices = degrees
    form.department.choices = departments
    form.faculty.choices = faculties
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
def acoount_logout():
    logout_user()
    alert('Logout successful')
    return redirect('/login')

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