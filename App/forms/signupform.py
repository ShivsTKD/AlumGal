from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, EqualTo, Email

class SignUp(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    first_name = StringField('first_name', validators=[InputRequired()])
    last_name = StringField('last_name', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired(), EqualTo('confirmpwd', message='Passwords must match')])
    confirmpwd  = PasswordField('Repeat Password')
    programme = SelectField('programme', validators=[InputRequired()])
    degree = SelectField('degree', validators=[InputRequired()])
    department = SelectField('department', validators=[InputRequired()])
    faculty = SelectField('faculty', validators=[InputRequired()])
    grad_year = SelectField('grad_year', validators=[InputRequired()])
    submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light'})