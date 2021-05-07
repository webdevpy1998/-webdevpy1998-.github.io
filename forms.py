from flask_wtf import FlaskForm  
from wtforms import StringField,IntegerField,SubmitField

class AddData(FlaskForm):
    name = StringField('Enter your name')
    number = IntegerField('Enter you mobile number')
    submit = SubmitField('Submit')