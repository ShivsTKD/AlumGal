from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    username =  db.Column('username', db.String, nullable=False, unique=True)
    password = db.Column('password', db.String(120), nullable=False)
    email = db.Column('email', db.String, nullable=False, unique=True)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

