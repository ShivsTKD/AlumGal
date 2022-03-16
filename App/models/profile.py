from App.database import db

class Profile(db.Model):
    pid = db.Column('pid',db.Integer,primary_key=True)
    uid = db.Column('uid',db.Integer, db.ForeignKey('user.id'),nullable=False)
    first_name = db.Column('first_name',db.String(60),nullable=False)
    last_name = db.Column('last_name',db.String(60),nullable=False)
    programme_id = db.Column('programme',db.Integer,db.ForeignKey('programme.id'),nullable=False)
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
