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
    name = StringField("Name", [validators.Length(min=2, max=20), validators.Regexp(r'^\w*$')])
    username = StringField("Username", [validators.Length(min=2, max=20), validators.Regexp(r'^\w*$'), uniqueUsernameRequired])
    password = PasswordField("Password", [validators.Length(min=2, max=20), validators.Regexp(r'^\w*$')])

    class Meta:
        csrf = False

class ProfileForm(FlaskForm):
    
    name = StringField("Name: ", [validators.Length(min=2, max=30, message="Must be within 2-30 characters")])
    username = StringField("Username: ", [validators.Length(min=2, max=30, message="Must be within 2-30 characters")])
    
    class Meta:
        csrf = False