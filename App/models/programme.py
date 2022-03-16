from App.database import db

class Programme(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(120), nullable=False)
    degree = db.Column('degree', db.String(120), nullable=False)
    department = db.Column('department', db.String(120), nullable=False)
    faculty = db.Column('faculty', db.String(120), nullable=False)
    profiles = db.relationship('Profile', backref='programme', lazy=True)

    def toDict(self):
        return{
            'id': self.id,
            'name': self.name,
            'degree': self.degree,
            'department': self.department,
            'faculty': self.faculty,
            'profiles': self.profiles
        }
