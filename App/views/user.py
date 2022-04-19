from flask import Blueprint, render_template, jsonify, request, send_from_directory,redirect,flash
from flask_jwt import jwt_required
from flask_login import login_required
from App.forms import *
from App.models import *
from werkzeug.utils import secure_filename
from App.controllers import (
    create_user, 
    get_user,
    get_programmes,
    get_all_users,
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

@user_views.errorhandler(404)
def page_not_found(error):
    flash('Invalid route')
    redirect('/')

@user_views.route('/', methods=['POST','GET'])
@login_required
def file():
    users = Profile.query.all()[-3:]
    if request.method == 'POST':
        form = request.form
        if not form['searchbar']:
            flash('Please enter a name')
            return redirect('/')
             
        name = form['searchbar']
        print(name)
        results = user_search(name)

        if results == 'Invalid':
            flash('Invalid search item!')
            return redirect('/')
        
        if results == None:
            flash('No results found')
            return redirect('/')
        
        return render_template('users.html',results=results) # add results page here
    return render_template('home.html',users=users)



@user_views.route('/signup', methods=['POST','GET'])
def post_signup_info():
    form = SignUp()
    form.programme.choices = get_programmes()
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
        return render_template('login.html',form=form)

@user_views.route('/logout', methods=['GET'])
@login_required
def account_logout():
    logoutuser()
    flash('Logout successful')
    return redirect('/login')

@user_views.route('/advsearch', methods=['GET','POST'])
@login_required
def advsearch():
    form = AdvSearch()
    if request.method == 'POST':
        data = request.form
        print(data)
        results = adv_search(data)
        return render_template('users.html', results=results)
    else:
        programmes = get_programmes()
        degrees = ['B.Sc.', 'M.Sc.']
        years = ['2020', '2021', '2022']
        return render_template('advsearch.html', form = form, programmes = programmes, degrees = degrees, years = years)

@user_views.route('/profile/<pid>', methods=['GET'])
@login_required
def get_profile(pid):
    user = Profile.query.filter_by(pid = pid).first()
    prog = Programme.query.filter_by(id = user.programme_id).first()
    return render_template('user.html', user=user, prog=prog)
    #anchor this route on to the student card to fetch profile details


# @user_views.route('/search/<fname>+<lname>', methods=['GET'])
# @login_required # to change
# def user_search(fname, lname):
#     #search by first name , last name or both
#     result = user_search(fname,lname)
#     return result

@user_views.route('/users', methods=['GET'])
def list_users():
    users = Profile.query.limit(25).all()
    return render_template('users.html', results=users)