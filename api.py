from flask import Flask,Blueprint,render_template
from extension import db
from user_controller import *


api = Blueprint('api', __name__)


@api.route("/users", methods=["GET"])
def get_user():
    user_list = list_users()
    return jsonify(user_list), 200


@api.route("/user/detail", methods=["POST"])
def user_detail():
    try:
        data = request.get_json()    
        email = data.get('email', None)
        priority = data.get('priority', None)
        user_list = get_user_(email, priority)
        if len(user_list) > 0:
            return jsonify(user_list)
        else:
            return jsonify({'result' : "Can't find this user!!"}), 400
    
    except Exception as e:
        print(e)
        return jsonify({'result' : "this is fail!!"}), 400


@api.route("/user/create", methods=["POST"])
def user_create():
    try:
        data = request.get_json()
        email = data.get('email', None)
        password = data.get('password', None)
        priority = data.get('priority', None)
        if email and password and priority:
            create_user(email, password, priority)
            return jsonify({'result' : "this is success!!"}), 200
        else:
            return jsonify({'result' : "please input complete!!"}), 400
    except:
        return jsonify({'result' : "this is fail!!"}), 400


@api.route("/user/update", methods=["POST"])
def user_update():
    try:
        data = request.get_json()
        email = data.get('email', None)
        password = data.get('password', None)
        priority = data.get('priority', None)
        if email and password or priority:
            result = update_user(email, password, priority)
            return result
        else:
            return jsonify({'result' : "please input complete!!"}), 200
    except:
        return jsonify({'result' : "this user no exist!!"}), 400


@api.route("/user/delete", methods=["POST"])
def user_delete():
    try:
        data = request.get_json()
        email = data.get('email', None)
        if email:
            result = delete_user(email)
            return result
        else:
            return jsonify({'result' : "please input complete!!"}), 200
    except:
        return jsonify({'result' : "this user no exist!!"}), 400