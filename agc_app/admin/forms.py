from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField,
                     validators
                     )
from flask_wtf.file import FileField, FileAllowed, FileRequired
from agc_app import photos
# from agc_app.utils.forms import RegistrationForm


class ImageStorageForm(FlaskForm):

    image_name = StringField('Name', [validators.DataRequired()])
    path = FileField('Image File', validators=[FileRequired(), FileAllowed(photos, "images only")])
    submit = SubmitField('Submit')


class Users(FlaskForm):
    firstname = StringField('First Name', [validators.Length(min=4, max=20)])
    lastname = StringField('Last Name', [validators.Length(min=4, max=20)])
    email = StringField('Email Address', [validators.Length(min=10, max=50,
                                                            message="Email address must be 10 to 50 characters Long"),
                                          validators.Email()])
    phonenumber = StringField('Phone Number', [validators.Length(min=7, max=12), validators.DataRequired()])
    is_admin = BooleanField('Is Admin', [validators.DataRequired()])
    submit = SubmitField('Register')


