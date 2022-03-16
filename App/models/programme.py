from App.database import db

class Programme(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String, nullable=False)
    degree = db.Column('degree', db.String, nullable=False)
    department = db.Column('department', db.String, nullable=False)

    def toDict(self):
        return{
            'id': self.id,
            'name': self.name,
            'degree': self.degree,
            'department': self.department
        }
