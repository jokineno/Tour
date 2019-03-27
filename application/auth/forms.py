from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField,IntegerField, validators, ValidationError


from application.auth.models import User

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

def uniqueUsernameRequired(form, field):
    if User.query.filter_by(username=form.username.data).first():
        raise ValidationError("Käyttäjätunnus on jo käytössä")

class RegistrationForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired()])
    username = StringField("Username", [validators.InputRequired(), uniqueUsernameRequired])
    password = PasswordField("Password", [validators.InputRequired()])

    class Meta:
        csrf = False

class ProfileForm(FlaskForm):
    #read only
    name = StringField("Name: ")
    username = StringField("Username: ")
    gigs_played = StringField("Gigs played: ")
    upcoming_gigs = IntegerField("Upcoming Gigs: ")

    class Meta:
        csrf = False