# from flask import Flask, render_template, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager, current_user, login_user, logout_user, login_required
# from flask_bootstrap import Bootstrap
# import gc
#
# from agc_app.utils.forms import LoginForm, RegistrationForm
# from agc_app.utils import User
# from agc_app.utils.config import Config
#
#
# app = Flask(__name__)
# app.config.from_object(Config)
#
# db = SQLAlchemy(app)
#
# # db.drop_all()
# # db.create_all()
# migrate = Migrate(app, db)
#
#
# login_manager = LoginManager(app)
# login_manager.login_view = 'auth.login'
#
# bootstrap = Bootstrap(app)
# # mail = Mail(app)
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# if __name__ == '__main__':
#     app.run()
from agc_app import app

if __name__ == "__main__":
	app.run()
