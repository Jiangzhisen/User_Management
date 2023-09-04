from .config.config import config
from extension import db, migrate
from view import views_bp
from api import api
from auth import login_manager
from resources.user import *

from flask import Flask
from flask_restful import Api
from flask_apispec.extension import FlaskApiSpec
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

def create_app(config_name, **kwargs):
 
    app = Flask(__name__)
    api1 = Api(app)
    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='User Management Project',
            version='v1',
            plugins=[MarshmallowPlugin()],
            openapi_version='2.0.0'
        ),
        'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON 
        'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
    })
    docs = FlaskApiSpec(app)
    app.config.from_object(config[config_name])
    path = kwargs.get("path")

    if path:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path

    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()
    
    login_manager.init_app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'views.login'

    app.register_blueprint(views_bp)
    app.register_blueprint(api)

    api1.add_resource(UserApi, '/user')
    # api1.add_resource(UserListAPI, '/users1')

    docs.register(UserApi)

    return app, api1