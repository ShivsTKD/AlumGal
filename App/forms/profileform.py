from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField,IntegerField
from wtforms.validators import InputRequired
#from App.database import db

class ProfileForm(FlaskForm):
    firstname = StringField('firstname', validators=[InputRequired()])
    lastname = StringField('lastname', validators=[InputRequired()])
    programme = SelectField('programme',validators=[InputRequired()])
    graduation_year = IntegerField('graduationyear', validators=[InputRequired()])
    facebook_id =  StringField('facebook link', validators=[InputRequired()])
    instagram_id = StringField('instagram link', validators=[InputRequired()])
    linkedin_id = StringField('linkedin link', validators=[InputRequired()])
    submit = SubmitField('Submit', render_kw={'class': 'btn waves-effect waves-light white-text'})