from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from App.models import Programme,Profile
from App.database import db
class AdvSearch(FlaskForm):
    
    first_name = StringField()
    last_name = StringField()
    programme = SelectField()
    graduation_year = SelectField()
    degree = SelectField()

    def __init__(self):
        self.programme.choices = [(p.id, p.name) for p in Programme.query.all()]
        self.graduation_year.choices = [(y.graduation_year,y.graduation_year) for y in Profile.query.with_entities(graduation_year).distinct()]
        self.degree.choices = [(y.degree,y.degree) for y in Profile.query.with_entities('degree').distinct()]