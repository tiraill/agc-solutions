from datetime import datetime
from agc_app import db, login_manager, app
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as serializer
from flask_login import UserMixin
from config import Config


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(25))
    lastname = db.Column(db.String(25))
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String)
    phonenumber = db.Column(db.String(25))
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_token(self, expires_secs=600):
        s = serializer(app.config['SECRET_KEY'], expires_secs)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return '<User {}>'.format(self.email)


@login_manager.user_loader
def load_user(_id):
    return User.query.get(int(_id))


class CallBackHistory(db.Model):
    __tablename__ = 'call_back_history'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phonenumber = db.Column(db.String)
    data_time = db.Column(db.TIMESTAMP, default=datetime.utcnow())


class Snippets(db.Model):
    __tablename__ = 'snippets'
    id = db.Column(db.Integer, primary_key=True)
    attribute_name = db.Column(db.String)
    attribute_value = db.Column(db.String)


class ImageStorage(db.Model):
    __tablename__ = 'image_storage'
    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String)
    static_path = db.Column(db.String)
    path = db.Column(db.String)


if Config.CLEAR_DATABASE:
    db.drop_all()
    db.create_all()
    db.session.commit()


if Config.CREATE_ADMIN:
    user = User.query.filter_by(email=Config.ADMIN_MAIL).first()
    if user:
        user.is_admin = True
    else:
        admin = User(
            firstname='admin',
            lastname='admin',
            email=Config.ADMIN_MAIL,
            is_admin=True
        )
        admin.set_password(Config.ADMIN_PASS)
        db.session.add(admin)
    db.session.commit()
