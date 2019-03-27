from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,BooleanField, validators,ValidationError
from wtforms.fields.html5 import DateField, TimeField

class GigForm(FlaskForm):
    name = StringField("Venue", [validators.Length(min=2, max=30, message="Must be within 2-30 characters")])
    place = StringField("City", [validators.Length(min=2, max=30, message="Must be within 2-30 characters")])
    pvm = DateField("Date",format='%Y-%m-%d')
    showtime = TimeField("Showtime:", format='%H:%M')
    status = SelectField("Status", choices=[("Tulossa","Tulossa"),("Mennyt","Mennyt"),("Peruttu","Peruttu")], option_widget=None)
    
    class Meta:
        csrf = False