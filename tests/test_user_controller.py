from user_controller import *
from conftest import *


@pytest.mark.fun1
class TestCreateUser():
    email = "12345@example.com"
    password = "12345"
    priority = "7"
    def test_create_user_one(self, app):
        with app.app_context():
            response, status_code = create_user(self.email, self.password, self.priority)
            assert status_code == 200
            assert response.json == {'result': "this is success!!"}


@pytest.mark.fun
class TestGetUser():
    email = "12345@example.com"
    password = "12345"
    priority = "7"
    def test_get_user_one(self, app):
        with app.app_context():
            response = get_user_(self.email, self.priority)
            assert response == [{'user_email': self.email, 'user_password': self.password, 'user_priority': 7}]


@pytest.mark.fun
class TestUpdateUser():
    email = "12345@example.com"
    password = "12345"
    priority = "9"
    def test_update_user(self, app):
        with app.app_context():
            response, status_code = update_user(self.email, self.password, self.priority)
            assert status_code == 200
            assert response.json == {'result' : "this is success!!"}


@pytest.mark.fun
class TestDeleteUser():
    email = "12345@example.com"
    def test_delete_user(self, app):
        with app.app_context():
            response, status_code = delete_user(self.email)
            assert status_code == 200
            assert response.json == {'result' : "this is success!!"}

