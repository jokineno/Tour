from flask_wtf import FlaskForm
from wtforms import StringField,TimeField,DateField,SelectField,BooleanField, validators,ValidationError
from wtforms.fields.html5 import DateField, TimeField



class GigForm(FlaskForm):
    name = StringField("Venue",[validators.InputRequired(),validators.Length(min=2, max=30, message="Must be within 2-30 characters")])
    place = StringField("City", [validators.InputRequired(),validators.Length(min=2, max=30, message="Must be within 2-30 characters")])
    pvm = DateField("Date",format='%Y-%m-%d')
    showtime = TimeField("Showtime:", format='%H:%M')
    status = SelectField("Status", choices=[("Tulossa","Tulossa"),("Mennyt","Mennyt"),("Peruttu","Peruttu")], option_widget=None)
    tour_id = SelectField("Tour", choices=[], coerce=int)
    
    class Meta:
        csrf = False

    