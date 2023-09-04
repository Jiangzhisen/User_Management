# from flask import Flask, render_template, request, jsonify, app, redirect, url_for, Blueprint, flash
# from flask import g, current_app
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from extension import db
# from view import views_bp
# from api import api
# import os
# import sqlite3
# from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
# from user_model import *
# from auth import login_manager


# app = Flask(__name__)
# # app.secret_key = os.urandom(16).hex() 
# app.config['SECRET_KEY'] = '3a3a89634143107e59dcb4a983150cab'


# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# login_manager.init_app(app)
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'views.login'


# app.register_blueprint(views_bp)
# app.register_blueprint(api)


# if __name__ =="__main__":
#     db.init_app(app)
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)





from app1 import create_app


app, api = create_app('development')
app.run(host="0.0.0.0", port=5000)
