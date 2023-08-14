import os
import tempfile
import pytest
from app1 import create_app
from extension import db
from flask_sqlalchemy import SQLAlchemy


# @pytest.fixture()
@pytest.fixture(scope="session")
def app():
    config_name = "testing"
    app = create_app(config_name)

    return app


# @pytest.fixture(scope="session")
# def _db(app):
#     db.app = app
#     db.create_all()

#     yield db

#     db.drop_all()


# @pytest.fixture(scope="session")
# def db(app):
#     db = SQLAlchemy(app)
#     return db


# @pytest.fixture(scope="function")
# def session(database):
#     connection = database.engine.connect()
#     transaction = connection.begin()
#     options = dict(bind=connection, binds={})
#     session = database.create_scoped_session(options=options)
#     database.session = session

#     yield session

#     transaction.rollback()
#     connection.close()
#     session.remove()


# @pytest.fixture(scope="function")
# def init_data(_db):
#     pass  


# @pytest.fixture()
@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


# @pytest.fixture()
@pytest.fixture(scope="session")
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(scope="session")
def init_database(app):
    with app.app_context():
        db.create_all()
    
    yield

    with app.app_context():
        db.session.remove()
        db.drop_all()