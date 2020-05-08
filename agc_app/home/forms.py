from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, validators


class CallBackForm(FlaskForm):
    name = StringField('First Name', [validators.DataRequired()])
    email = StringField('Email Address', [validators.DataRequired()])
    phonenumber = StringField('Phone Number', [validators.DataRequired()])
    success_checkbox = BooleanField('Agree?', [validators.DataRequired()])
    submit = SubmitField('Рассчитать стоимость')
