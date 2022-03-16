from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, URLField
from wtforms.validators import InputRequired, EqualTo, Email, Regexp

class SignUp(FlaskForm):
    username = StringField(validators=[InputRequired()])
    first_name = StringField(validators=[InputRequired()])
    last_name = StringField(validators=[InputRequired()])
    email = StringField(validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired(), EqualTo('confirmpwd', message='Passwords must match')])
    confirmpwd  = PasswordField()
    programme = SelectField(validators=[InputRequired()])
    degree = SelectField(validators=[InputRequired()])
    department = SelectField(validators=[InputRequired()])
    faculty = SelectField(validators=[InputRequired()])
    grad_year = SelectField(validators=[InputRequired()])
    fb = URLField()
    ig = URLField()
    l_in = URLField()
    submit = SubmitField(render_kw={'class': 'btn waves-effect waves-light green'})
