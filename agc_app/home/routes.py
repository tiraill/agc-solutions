from typing import List
from agc_app import mail, db
from flask_mail import Message

from flask import (
    render_template, redirect, url_for, Blueprint
)
from agc_app.home.forms import CallBackForm
from agc_app.models import CallBackHistory, User, ImageStorage
from config import Config

home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
def index():
    form = CallBackForm()
    images: List[ImageStorage] = ImageStorage.query.all()
    images_dict = {image.image_name: image.static_path for image in images}
    if form.validate_on_submit():
        send_email_notification(form)

        call = CallBackHistory(
            name=form.name.data,
            email=form.email.data,
            phonenumber=form.phonenumber.data
        )
        db.session.add(call)
        db.session.commit()
        return redirect(url_for('home.index'))
    return render_template('index.html', form=form, images=images_dict)


def send_email_notification(form: CallBackForm):
    admins: List[User] = User.query.filter_by(is_admin=True).all()
    msg = Message(
        'Новая заявка',
        sender=Config.MAIL_SENDER,
        recipients=[admin.email for admin in admins]
        )
    msg.body = f'''Поступила новая заявка:
    Имя: {form.name.data}
    Email: {form.email.data}
    Телефон: {form.phonenumber.data}
    '''
    try:
        mail.send(msg)
    except Exception as exc:
        print(exc)
        return False
    else:
        return True
