from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_uploads import configure_uploads, UploadSet, IMAGES
from flask_mail import Mail
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


'''
creating an object instantiated by uploadedset
which takes 'photos' as name of the file and IMAGES as the type of 
file we wanna accept
'''
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


db = SQLAlchemy(app)

#db.create_all
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap(app)
mail = Mail(app)

from agc_app import models

from agc_app.admin.routes import admin
from agc_app.auth.routes import auth
from agc_app.home.routes import home

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(auth)
app.register_blueprint(home)


@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', title = 'Forbidden'),403


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', title = 'Page Not Found'),404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html', title = 'Forbidden'),500

