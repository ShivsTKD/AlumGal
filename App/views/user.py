from flask import Blueprint, render_template, jsonify, request, send_from_directory,redirect,flash
from flask_jwt import jwt_required
from flask_login import login_required
from App.forms import *
from App.models import *
from werkzeug.utils import secure_filename
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
    user_profile_create,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@login_manager.unauthorized_handler
def no_auth():
    return redirect('/login')


@user_views.route('/')
@login_required
def file():
    users = Profile.query.all()[-3:]
    for user in users:
        print(user.pid, user.first_name)
    return render_template('home.html',users=users)



@user_views.route('/signup', methods=['POST','GET'])
def post_signup_info(): ##unfinished but still renders as intended post no fully implemented
    form = SignUp()
    programmeList = []
    programmes = Programme.query.all()
    for p in programmes:
        if p.name not in programmeList:
            programmeList.append(p.name)
    form.programme.choices = programmeList
    form.degree.choices = ['B.Sc.', 'M.Sc.']
    form.grad_year.choices = ['2020', '2021', '2022']
    if request.method == 'POST':
        fdata = SignUp(request.form)
        image = request.files['img']
        filename = secure_filename(image.filename)
        image.save(f'images\{filename}')
        done = user_profile_create(fdata.data,filename) 
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
            return redirect('/login')
    else:
        form = Login()
        return render_template('login.html',form=form)#change page to whatever template

@user_views.route('/logout', methods=['GET'])
@login_required
def account_logout():
    logoutuser()
    flash('Logout successful')
    return redirect('/login')

# @user_views.route('/advsearch', methods=['GET','POST'])
# @login_required
# def advsearch():
#     form = AdvSearch()
#     if request.method == 'POST':
#         data = request.form.data
#         results = adv_search(data)
#         return results
#     else:
#         # return render_template('',form = form)

@user_views.route('/profile/<pid>', methods=['GET'])
def get_profile(pid):
    pro = Profile.query.filter_by(pid = pid).first()
    return render_template('profile.html', profile=pro)
    #anchor this route on to the student card to fetch profile details


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