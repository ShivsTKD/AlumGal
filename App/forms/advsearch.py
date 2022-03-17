from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField,IntegerField

class AdvSearch(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    programme = SelectField()
    department = SelectField()
    faculty = SelectField()
    grad_year = IntegerField()