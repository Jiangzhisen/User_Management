from flask import Flask, render_template, request, jsonify, app, redirect, url_for
from extension import db
from user_model import User


def list_users():
    users = db.session.execute(db.select(User).order_by(User.id)).scalars().all()
    user_list = []
    for user in users:
        user_list.append({'user_id': user.id, 'user_email': user.email, 'user_password': user.password, 'user_priority': user.priority})
    return user_list
    

def get_user_(**kwargs):
    email = kwargs.get('email', None)
    priority = kwargs.get('priority', None)
    user_list = []
    if email and priority:
        users = User.query.filter_by(email = email, priority = priority).all()
    elif email:
        users = User.query.filter_by(email = email).all()
    elif priority:
        users = User.query.filter_by(priority = priority).all()
    else:
        users = db.session.execute(db.select(User).order_by(User.id)).scalars().all()
    for user in users:
        user_list.append({'user_email': user.email, 'user_password': user.password, 'user_priority': user.priority})
    return user_list


def create_user(email, password, priority, **kwargs):
    try:
        user = User(
            email=email,
            password=password,
            priority=priority
        )
        db.session.add(user)
        db.session.commit()
        return {'result' : "this is success!!"}, 200
    except:
        return {'result' : "this is fail!!"}, 400


def update_user(email, **kwargs): 
    password = kwargs.get('password', None)
    priority = kwargs.get('priority', None)
    user = User.query.filter_by(email=email).first()
    if user:
        if password and priority:
            user.password = password
            user.priority = priority
        elif password:
            user.password = password
        elif priority:
            user.priority = priority
        db.session.commit()
        return {'result' : "this is success!!"}, 200
    else:
        return {'result' : "Can't find this user!!"}, 400


def delete_user(email, **kwargs):
    user = User.query.filter_by(email=email).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'result' : "this is success!!"}, 200
    else:
        return {'result' : "Can't find this user!!"}, 400

