from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, IntegerField, validators, ValidationError


from application.auth.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
  
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
    name = StringField("Name: ", [validators.Length(min=2, max=30, message="Must be within 2-30 characters")])
    username = StringField("Username: ", [validators.Length(min=2, max=30, message="Must be within 2-30 characters")])
    role = SelectField("Role: ", choices=[("Musician","Musician"),("Production Manager","Production Manager"),("Bus Driver","Bus Driver")], option_widget=None)
    #gigs_played = IntegerField("Gigs played: ")
    #upcoming_gigs = IntegerField("Upcoming Gigs: ")

    class Meta:
        csrf = False