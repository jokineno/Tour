from flask_wtf import FlaskForm
from wtforms import StringField,TimeField,DateField,SelectField,BooleanField, validators,ValidationError
from wtforms.fields.html5 import DateField, TimeField

class TourForm(FlaskForm):
    name = StringField("Name of the Tour", [validators.InputRequired(),validators.Length(min=2, max=30, message="Must be within 2-30 characters")])
    start_date = DateField("Tour Starts at: ",format='%Y-%m-%d', validators=[validators.InputRequired()])
    end_date = DateField("Tour Ends at: ",format='%Y-%m-%d',validators=[validators.InputRequired()])
    
    class Meta:
        csrf = False