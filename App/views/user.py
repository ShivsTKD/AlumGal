from flask import Blueprint, render_template, jsonify, request, send_from_directory,redirect,flash
from flask_jwt import jwt_required
from flask_login import login_required
from App.forms import *
from App.models import *

from App.controllers import (
    create_user, 
    get_user,
    get_all_users,
    get_all_users_json,
    loginuser,
    logoutuser,
    authenticate,
    user_search,
    adv_search,
    login_manager,
    load_user,
    user_profile_create
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@login_manager.unauthorized_handler
def no_auth():
    return redirect('/login')


@user_views.route('/')
@login_required
def home():
    return render_template('home.html')

@user_views.route('/signup', methods=['POST','GET'])
def post_signup_info(): 
    form = SignUp()
    form.programme.choices = [(p.name, p.name) for p in Programme.query.all()]
    form.degree.choices = [(p.degree,p.degree) for p in Programme.query.with_entities(Programme.degree).distinct()]
        
    if request.method == 'POST':
        fdata = SignUp(request.form)
        done = user_profile_create(fdata.data) 
        print (done)
        if done:
            flash("User profile created")
            return redirect('/login')
        else:
            flash("User profile not created")
            return redirect('/signup')
    else:
        
        return render_template('signup.html',form=form) 

@user_views.route('/login', methods = ['GET','POST'])
def account_login(): 
    if request.method == 'POST':
        form = Login(request.form)
        user = authenticate(username = form.username.data, password = form.password.data)
        if user:
            flash('Login successful')
            loginuser(user,remember = True)
            return redirect('/')
        else:
            flash('Wrong username or password')
    else:
        form = Login()
        return render_template('login.html',form=form)

@user_views.route('/logout', methods=['GET'])
@login_required
def account_logout():
    logoutuser()
    flash('Logout successful')
    return redirect('/login')

@user_views.route('/advsearch', methods=['GET'])
@login_required
def advsearch():
    
    form = AdvSearch()
    data = request.form.to_dict()
    results = adv_search(data)
    return results


@user_views.route('/search/<fname>+<lname>', methods=['GET'])
@login_required # to change
def user_search(fname, lname):
    #search by first name , last name or both
    result = user_search(fname,lname)
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