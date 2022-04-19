from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField,IntegerField
from App.models import Programme,Profile
from App.database import db
class AdvSearch(FlaskForm):
    
    first_name = StringField()
    last_name = StringField()
    programme = SelectField()
    graduation_year = SelectField()
    degree = SelectField()