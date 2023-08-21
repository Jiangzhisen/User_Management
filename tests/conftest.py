import tempfile
import pytest
from app1 import create_app
from extension import db


# @pytest.fixture()
@pytest.fixture(scope="session")
def app():
    db_fd, db_path = tempfile.mkstemp()
    config_name = "testing"
    app = create_app(config_name, path=db_path)
    return app


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

    # 創建所有表
    with app.app_context():
        db.create_all()
        
        yield db

        # 清理數據庫
        db.drop_all()
