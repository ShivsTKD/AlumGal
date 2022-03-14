
from App.database import db
class User(db.Model):
    p_id = db.Column('pid',db.Integer,primary_key=True)
    u_id = db.Column('uid',db.Integer, ForeignKey('user.id'),nullable=False)
    first_name = db.Column('first_name',db.String,nullable=False)
    last_name = db.Column('last_name',db.String,nullable=False)
    programme_id = db.Column('programme',db.Integer,ForeignKey('programme.id'),nullable=False)
    graduation_year = db.Column('graduation_year',db.Integer,nullable=False)

    def toDict(self):
        return{
                'p_id' :self.p_id,
                'u_id ':self.u_id,
                'first_name' :self.first_name,
                'last_name' :self.last_name,
                'programme_id':self.programme_id,
                'graduation_year':self.graduation_year
        }
