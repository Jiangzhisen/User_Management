from flask import Flask,Blueprint,render_template, current_app
from extension import db
from user_controller import *
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os
from auth import login_manager


views_bp = Blueprint('views', __name__)


@views_bp.route("/")
@login_required
def index1():
    return render_template("index.html")


@views_bp.route("/userlist")
@login_required
def user_list():
    user_list = list_users()
    return render_template("user_list.html", users=user_list)


@views_bp.route("/getuser")
@login_required
def get_user():
    return render_template("get_user.html")


@views_bp.route("/createuser")
@login_required
def create_user():
    return render_template("create_user.html")


@views_bp.route("/updateuser")
@login_required
def update_user():
    return render_template("update_user.html")


@views_bp.route("/deleteuser")
@login_required
def delete_user():
    return render_template("delete_user.html")


@views_bp.route("/register")
def register():
    return render_template("register.html")


class User1(UserMixin):  
    pass  


@login_manager.user_loader  
def user_loader(email):  
    users = db.session.execute(db.select(User).order_by(User.id)).scalars()
    users_email = []
    for user in users:
        users_email.append(user.email)
    
    if email not in users_email:
        return 

    user = User1()          
    user.id = email             
    return user                                                         


@views_bp.route('/login', methods=['GET', 'POST'])  
def login():  
    if request.method == 'GET':  
        # return render_template(current_app.config['LOGIN_TEMPLATE'])
        return render_template('login.html')
    email = request.form['user_email']
    password = request.form['password']
    user1 = User.query.filter_by(email=email, password=password).first()
    print(user1)
    if user1:
        user = User1()
        user.id = email
        login_user(user)
        return redirect(url_for('views.index1'))  
    
    return 'Bad login'  


@views_bp.route('/protected')  
@login_required  
def protected():   
    print(current_user)
    if current_user.is_active:  
        return 'Logged in as: ' + current_user.id + 'Login is_active:True'
    else:
        return 'Not logged in'


@views_bp.route('/logout')  
def logout():  
    logout_user()
    return redirect(url_for('views.login'))  