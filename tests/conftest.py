import os
import tempfile
import pytest
from pytest_mysql import factories
from app1 import create_app
from extension import db
from flask_sqlalchemy import SQLAlchemy



# @pytest.fixture()
@pytest.fixture(scope="session")
def app():
    config_name = "testing"
    app = create_app(config_name)
    return app


# @pytest.fixture()
@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


# @pytest.fixture()
@pytest.fixture(scope="session")
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(scope="function")
def init_database(app):

    # 創建所有表
    with app.app_context():
        db.create_all()
        yield db

        # 清理數據庫
        db.drop_all()




# @pytest.fixture(scope="session")
# def init_database(app):
#     with app.app_context():
#         db.create_all()
    
#     yield

#     with app.app_context():
#         db.session.remove()
#         db.drop_all()