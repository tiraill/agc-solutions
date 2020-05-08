from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

from wtforms.validators import ValidationError, DataRequired, Email

from agc_app.models import User


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', [validators.DataRequired()])
    lastname = StringField('Last Name')
    email = StringField('Email Address', [validators.Email()])
    phonenumber = StringField('Phone Number')
    password = PasswordField('Password', [validators.DataRequired()])
    confirm = PasswordField('Repeat Password', [validators.EqualTo('password', message="Passwords must match. ")])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email already in use. ")


# general login form
class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Sign In')


class RequestResetForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("There is no account with that email. You must register first")


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', [validators.DataRequired()])
    confirm = PasswordField('Repeat Password', [validators.EqualTo('password', message="Passwords must match. ")])
    submit = SubmitField('Reset Password')
