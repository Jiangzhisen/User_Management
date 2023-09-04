from user_controller import *

from flask_restful import Resource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields

class UserAuthRequestSchema(Schema):
    Authorization = fields.Str(required=True, description="User's authorization code")

class UserGetRequestSchema(Schema):
    Authorization = fields.Str(required=True, description="User's authorization code")
    email = fields.Email(description="User's email")
    priority = fields.Integer(description="User's priority")

class UserSchema(Schema):
    user_email = fields.Str(default='')
    user_password = fields.Str(default='')
    user_priority = fields.Int(default=0)

class UserGetResponseSchema(Schema):
    users = fields.List(fields.Nested(UserSchema))

class UserCreateRequestSchema(Schema):
    email = fields.Email(required=True, description="User's email")
    password = fields.Str(required=True, description="User's password")
    priority = fields.Int(required=True, description="User's priority")

class UserCreateResponseSchema(Schema):
    result = fields.Str(default='')

class UserUpdateRequestSchema(Schema):
    email = fields.Email(required=True, description="User's email")
    password = fields.Str(description="User's password")
    priority = fields.Int(description="User's priority")

class UserUpdateResponseSchema(Schema):
    result = fields.Str(default='')

class UserDeleteRequestSchema(Schema):
    email = fields.Email(required=True, description="User's email")

class UserDeleteResponseSchema(Schema):
    result = fields.Str(default='')

# Member authorization code
authorizationCode = "34Y9Pdkc1euB5Z7"

class UserApi(MethodResource, Resource):
    @doc(description='This API can allow you to query users.', tags=['Query User'])
    @use_kwargs(UserGetRequestSchema, location=('query'))
    # @marshal_with(UserGetResponseSchema)
    def get(self, **kwargs):
        try:
            authorization = kwargs.get('Authorization', None)
            email = kwargs.get('email', None)
            priority = kwargs.get('priority', None)
            if authorization == authorizationCode:
                user_list = get_user_(email=email, priority=priority)
                if len(user_list) > 0:
                    return {'users': user_list}
                else:
                    return {'result' : "Can't find this user!!"}
            else:
                return {'result' : "Invalid authorization code!!"}
        except Exception as e:
            print(e)
            return {'result' : "this is fail!!"}

    @doc(description='This API can allow you to create users.', tags=['Create User'])
    @use_kwargs(UserAuthRequestSchema, location=('query'))
    @use_kwargs(UserCreateRequestSchema, location=('json'))
    @marshal_with(UserCreateResponseSchema)
    def post(self, **kwargs):
        try:
            authorization = kwargs.get('Authorization', None)
            email = kwargs.get('email', None)
            password = kwargs.get('password', None)
            priority = kwargs.get('priority', None)
            if authorization == authorizationCode:
                if email and password and priority:
                    create_user(email, password, priority)
                    return {'result' : "this is success!!"}
                else:
                    return {'result' : "please input complete!!"}
            else:
                return {'result' : "Invalid authorization code!!"}
        except:
            return {'result' : "this is fail!!"}

    @doc(description="This API can allow you to update user's infomation.", tags=['Update User'])
    @use_kwargs(UserAuthRequestSchema, location=('query'))
    @use_kwargs(UserUpdateRequestSchema, location=('json'))
    @marshal_with(UserUpdateResponseSchema)
    def put(self, **kwargs):
        try:
            authorization = kwargs.get('Authorization', None)
            email = kwargs.get('email', None)
            password = kwargs.get('password', None)
            priority = kwargs.get('priority', None)
            if authorization == authorizationCode:
                if email and password or priority:
                    result = update_user(email, password=password, priority=priority)
                    return result
                else:
                    return {'result' : "please input complete!!"}
            else:
                return {'result' : "Invalid authorization code!!"}
        except:
            return {'result' : "this user no exist!!"}

    @doc(description='This API can allow you to delete user.', tags=['Delete User'])
    @use_kwargs(UserAuthRequestSchema, location=('query'))
    @use_kwargs(UserDeleteRequestSchema, location=('json'))
    @marshal_with(UserDeleteResponseSchema)
    def delete(self, email, **kwargs):
        try:
            authorization = kwargs.get('Authorization', None)
            if authorization == authorizationCode:
                if email:
                    result = delete_user(email)
                    return result
                else:
                    return {'result' : "please input complete!!"}
            else:
                return {'result' : "Invalid authorization code!!"}
        except:
            return {'result' : "this user no exist!!"}
