from App.database import db

class Programme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def toDict(self):
        return{
            id: self.id,
            name: self.name
        }