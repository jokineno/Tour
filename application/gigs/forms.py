from flask_wtf import FlaskForm
from wtforms import StringField,TimeField,DateField,SelectField,BooleanField, validators

class GigForm(FlaskForm):
    name = StringField("Keikkapaikka", [validators.Length(min=2)])
    place = StringField("Kaupunki")
    pvm = DateField("Pvm",format='%Y-%m-%d')
    showtime = TimeField("Showtime", format='%H:%M')
    status = SelectField("Tila", choices=[("Tulossa","Tulossa"),("Mennyt","Mennyt"),("Peruttu","Peruttu")], option_widget=None)
    
    class Meta:
        csrf = False