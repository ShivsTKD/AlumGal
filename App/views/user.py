from flask import Blueprint, render_template, jsonify, request, send_from_directory,flash,redirect
#from flask_jwt import jwt_required
from flask_login import login_required
from App.forms import *
from App.models import *

from App.controllers import (
    create_user, 
    create_profile,
    get_user,
    get_all_users,
    get_all_users_json,
    userlogin,
    logoutuser,
    authenticate,
    user_search,
    adv_search,
    login_manager
)

login_manager.login_view = "user_views.account_login"



user_views = Blueprint('user_views', __name__, template_folder='../templates')

@login_manager.unauthorized_handler
def no_auth():
    return redirect('/login')


@user_views.route('/signup', methods=['POST','GET'])
def post_signup_info():
    form = SignUp(request.form)
    if request.method == 'POST':
        image = request.files['img']
        filename = photos.save(image, name=f"{1}.jpg")
        #return filename
        if form.validate_on_submit():
            data = request.form
            user = create_user(username = data['username'], password = data['password'],email = data['email'])
            pdata= []
            for k,v in form:
                if k != 'username' or k != 'password' or k != 'email':
                    pdata[k] = v
            if user:
                flash('Signup successful')
                redirect('/login')
                # uid = get_user(data['username'])
                # profile = create_profile(uid,pdata)
                # if profile:
                #     flash('Signup successful')
                #     redirect('/login')
            else:
                flash('username or email already in use')
    else:
        form = SignUp()
        return render_template('signup.html', form=form)


@user_views.route('/login', methods = ['POST','GET'])
def account_login():
    form = Login(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = authenticate(username = form['username'], password = form['password'])
            if user:
                userlogin(user)
                flash('Login successful')
            else:
                flash('Invalid credentials')
    else:
        form = Login()
        return render_template('login.html', form=form)

    

@user_views.route('/logout', methods=['GET'])
@login_required
def account_logout():
    logoutuser()
    flash('Logout successful')
    return redirect('/login')

@user_views.route('/advsearch', methods=['GET'])
@login_required
def advsearch():
    form = AdvSearch(request.form)
    if form.validate_on_submit():
        data = request.form.to_dict()
        results = adv_search(data)
        return results
        #something to render results
    else:
        form = AdvSearch()
        #render form

#home route

@user_views.route('/')
@login_required
def home():
    return render_template('home.html')
    # query handlers to be added


@user_views.route('/search', methods=['GET'])
@login_required
def user_search():
    fname = request.args('fname')
    lname = request.args('lname')
    #search by first name , last name or both
    result = user_search(fname,lname)
    return result

@user_views.route('/users', methods=['GET'])
def list_users():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/users', methods=['GET'])
def get_user_page():
    args = request.args
    username = args.get('username')
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