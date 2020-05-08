from agc_app import mail, db
from flask_mail import Message
from flask import (
    render_template, redirect, url_for, flash, Blueprint
)
from agc_app.models import User
from config import Config
import gc
from agc_app.auth.forms import RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm
from flask_login import current_user, login_user, logout_user, login_required


auth = Blueprint('auth', __name__)


@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    gc.collect()
    return redirect(url_for('auth.login'))


@auth.route('/register/', methods=["GET", "POST"])
def register():
    error = ' '
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('admin.admin_main'))
    try:
        if form.validate_on_submit():
            user = User(
                firstname=form.firstname.data,
                lastname=form.lastname.data,
                email=form.email.data,
                phonenumber=form.phonenumber.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            gc.collect()
            flash("Congratulations, Registration was successful", 'success')
            return redirect(url_for('auth.login'))
        return render_template('register.html', form=form, error=error, title='Register')
    except Exception as e:
        return render_template('register.html', form=form, title="Register")


@auth.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    error = ' '
    try:
        if current_user.is_authenticated:
            flash("you are already logged in", 'info')
            return redirect(url_for('admin.admin_main'))
        if form.validate_on_submit():

            user = User.query.filter_by(email=form.email.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password', 'warning')
                return redirect(url_for('auth.login', form=form, title="Login to your account"))
            login_user(user)
            flash("you have been successfully logged in", 'success')
            gc.collect()

            return redirect(url_for('admin.admin_main'))

        return render_template('login.html', form=form, title="Login to your account")
    except Exception as e:
        flash(e)
        return render_template('login.html', form=form, error=error, title="Login to your account")


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        'Password Reset Request',
        sender=Config.MAIL_SENDER,
        recipients=[user.email]
    )
    msg.body = f'''To reset your password, visit the following link:
    { url_for('auth.reset_token', token = token, _external =True) }
    If you did not make this request simply ignore this request and no changes will be made.
    '''
    mail.send(msg)


@auth.route('/reset_password/', methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('admin.admin_main'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset you password', 'info')
        return redirect(url_for('auth.login'))
    return render_template(
        'reset_request.html',
        title='Reset password',
        form=form
    )


@auth.route('/reset_password/<token>/', methods=["GET", "POST"])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('admin.admin_main'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('auth.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # user.password_hash = user.set_password(form.password.data)
        user.set_password(form.password.data)
        db.session.commit()
        gc.collect()
        flash('Your password has been successfully updated', 'success')
        return redirect(url_for('auth.login'))
    return render_template(
        'change-password.html',
        title='Reset password',
        form=form
    )
