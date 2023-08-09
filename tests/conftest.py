import os
import tempfile
import pytest
from app1 import create_app
from extension import db


# @pytest.fixture()
@pytest.fixture(scope="session")
def app():
    config_name = "testing"
    db_fd, db_path = tempfile.mkstemp()
    app = create_app(config_name, path=db_path)

    # with app.app_context():
    #     db.create_all()

    yield app

    os.close(db_fd)
    os.unlink(db_path)


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