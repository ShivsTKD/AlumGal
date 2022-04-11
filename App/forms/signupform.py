from flask_wtf import FlaskForm
from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, SelectField, URLField,IntegerField
from wtforms.validators import InputRequired, EqualTo, Email
from App.models import Programme
from App.database import db
photos = UploadSet('photos', IMAGES)

class SignUp(FlaskForm):
    username = StringField(validators=[InputRequired()])
    first_name = StringField(validators=[InputRequired()])
    last_name = StringField(validators=[InputRequired()])
    email = StringField(validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired(), EqualTo('confirmpwd', message='Passwords must match')])
    confirmpwd  = PasswordField(validators=[InputRequired(), EqualTo('password')])
    programme = SelectField(validators=[InputRequired()])
    #degree = SelectField(validators=[InputRequired()]) 
    grad_year = IntegerField(validators=[InputRequired()])
    fb = URLField()
    ig = URLField()
    l_in = URLField()
    img = FileField(validators=[FileRequired(), FileAllowed(photos, message='Images Only!')])

    def __init(self):
        self.programme.choices = [(p.id, p.name) for p in Programme.query.all()]
        #self.degree.choices = [(p.degree,p.degree) for p in Programme.query.with_entities(degree).distinct()]
        