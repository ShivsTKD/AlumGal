from flask_login import login_user, logout_user, LoginManager
from flask_jwt import JWT
from App.models import User


login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user

def identity(payload):
    return User.query.get(payload['identity'])

def loginuser(user, remember):
    return login_user(user, remember=remember)

def logoutuser():
    logout_user()

def setup_jwt(app):
    return JWT(app, authenticate, identity)