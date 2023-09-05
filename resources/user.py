from user_controller import *

from flask_restful import Resource, reqparse
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from functools import wraps

# class UserAuthRequestSchema(Schema):
#     Authorization = fields.Str(required=True, description="User's authorization code")

class UserAuthResponseSchema(Schema):
    message = fields.Str(default='')

class UserGetRequestSchema(Schema):
    email = fields.Email(description="User's email")
    priority = fields.Integer(description="User's priority")

class UserSchema(Schema):
    user_email = fields.Str(default='')
    user_password = fields.Str(default='')
    user_priority = fields.Int(default=0)

class UserGetResponseSchema(Schema):
    users = fields.List(fields.Nested(UserSchema))

class UserGetFailSchema(Schema):
    result = fields.Str(default='')

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
# authorizationCode = "34Y9Pdkc1euB5Z7"

# Create a parser to parse the 'X-API-Key' header
api_key_parser = reqparse.RequestParser()
api_key_parser.add_argument('X-API-Key', location='headers')

@doc(security=[{"api_key": []}])  # Specify the security requirement for this endpoint
class UserApi(MethodResource, Resource):
    @doc(description='This API can allow you to query users.', tags=['User Management'], summary="Get the specific users infomation")
    @use_kwargs(UserGetRequestSchema, location=('query'))
    @marshal_with(UserGetResponseSchema, code=200)
    @marshal_with(UserAuthResponseSchema, code=401)
    @marshal_with(UserGetFailSchema, code=404)
    @marshal_with(UserGetFailSchema, code=500)
    def get(self, **kwargs):
        try:
            args = api_key_parser.parse_args()
            api_key = args['X-API-Key']
            if api_key == '1f892a4a-9a23-4c2e-a185-4f35ffd0b2e6':
                # Authorized, perform your action here
                email = kwargs.get('email', None)
                priority = kwargs.get('priority', None)
                user_list = get_user_(email=email, priority=priority)
                if len(user_list) > 0:
                    return {'users': user_list}, 200
                else:
                    return {'result' : "Can't find this user!!"}, 404
            else:
                # Unauthorized
                return {'message': 'Unauthorized'}, 401
        except Exception as e:
            print(e)
            return {'result' : "this is fail!!"}, 500

    @doc(description='This API can allow you to create users.', tags=['User Management'], summary="Create a new user")
    @use_kwargs(UserCreateRequestSchema, location=('json'))
    @marshal_with(UserCreateResponseSchema, code=200)
    @marshal_with(UserCreateResponseSchema, code=400)
    @marshal_with(UserAuthResponseSchema, code=401)
    @marshal_with(UserCreateResponseSchema, code=500)
    def post(self, **kwargs):
        try:
            args = api_key_parser.parse_args()
            api_key = args['X-API-Key']
            if api_key == '1f892a4a-9a23-4c2e-a185-4f35ffd0b2e6':
                email = kwargs.get('email', None)
                password = kwargs.get('password', None)
                priority = kwargs.get('priority', None)
                if email and password and priority:
                    create_user(email, password, priority)
                    return {'result' : "this is success!!"}, 200
                else:
                    return {'result' : "please input complete!!"}, 400
            else:
                return {'message': 'Unauthorized'}, 401
        except:
            return {'result' : "this is fail!!"}, 500

    @doc(description="This API can allow you to update user's infomation.", tags=['User Management'], summary="Update user infomation")
    @use_kwargs(UserUpdateRequestSchema, location=('json'))
    @marshal_with(UserUpdateResponseSchema, code=200)
    @marshal_with(UserUpdateResponseSchema, code=400)
    @marshal_with(UserAuthResponseSchema, code=401)
    @marshal_with(UserUpdateResponseSchema, code=404)
    def patch(self, **kwargs):
        try:
            args = api_key_parser.parse_args()
            api_key = args['X-API-Key']
            if api_key == '1f892a4a-9a23-4c2e-a185-4f35ffd0b2e6':
                email = kwargs.get('email', None)
                password = kwargs.get('password', None)
                priority = kwargs.get('priority', None)
                if email and password or priority:
                    result = update_user(email, password=password, priority=priority)
                    return result
                else:
                    return {'result' : "please input complete!!"}, 400
            else:
                return {'message': 'Unauthorized'}, 401
        except:
            return {'result' : "this user no exist!!"}, 404

    @doc(description='This API can allow you to delete user.', tags=['User Management'], summary="Delete a specific user")
    @use_kwargs(UserDeleteRequestSchema, location=('json'))
    @marshal_with(UserUpdateResponseSchema, code=200)
    @marshal_with(UserUpdateResponseSchema, code=400)
    @marshal_with(UserAuthResponseSchema, code=401)
    @marshal_with(UserUpdateResponseSchema, code=404)
    def delete(self, email, **kwargs):
        try:
            args = api_key_parser.parse_args()
            api_key = args['X-API-Key']
            if api_key == '1f892a4a-9a23-4c2e-a185-4f35ffd0b2e6':
                if email:
                    result = delete_user(email)
                    return result
                else:
                    return {'result' : "please input complete!!"}, 400
            else:
                return {'message': 'Unauthorized'}, 401
        except:
            return {'result' : "this user no exist!!"}, 404
