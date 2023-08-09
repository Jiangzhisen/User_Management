from user_controller import *
from conftest import *


@pytest.mark.api
class TestUserCreate():
    email = "12345@gmail.com"
    password = "12345"
    priority = "7" 
    url = "/user/create"

    def test_user_create_one(self, client):
        data = {
            "email": self.email,
            "password": self.password,
            "priority": self.priority
        }
        response = client.post(self.url, json=data)
        assert response.status_code == 200

    def test_user_create_two(self, client):
        data = {
            "email": "",
            "password": "",
            "priority": ""
        }
        response = client.post(self.url, json=data)
        assert response.status_code == 400
        assert response.json == {'result' : "please input complete!!"}


@pytest.mark.api
class TestUserDetail():
    email = "12345@gmail.com"
    priority = "7" 
    url = "/user/detail"

    def test_user_detail_one(self, client):
        data = {
            "email": self.email, 
            "priority": self.priority
        }
        response = client.post(self.url, json=data)
        assert response.status_code == 200
        assert response.json == [{'user_email': "12345@gmail.com", 'user_password': '12345', 'user_priority': 7}]

    
    def test_user_detail_two(self, client):
        data = {
            "email": self.email
        }
        response = client.post(self.url, json=data)
        assert response.status_code == 200
        assert response.json == [{'user_email': "12345@gmail.com", 'user_password': '12345', 'user_priority': 7}]

    
    def test_user_detail_three(self, client):
        data = {
            "priority": self.priority
        }
        response = client.post(self.url, json=data)
        assert response.status_code == 200
        assert response.json == [{'user_email': "12345@gmail.com", 'user_password': '12345', 'user_priority': 7}]


    def test_user_detail_four(self, client):
        data = {
            "email": "",
            "priority": ""
        }
        response = client.post(self.url, json=data)
        assert response.status_code == 400
        assert response.json == {'result' : "this is fail!!"}


@pytest.mark.api
class TestUserUpdate():
    email = "12345@gmail.com"
    email1 = "54321@gmail.com"
    password = "54321"
    priority = "9" 
    url = "/user/update"

    def test_user_update_one(self, client):
        data = {
            "email": self.email,
            "password": self.password,
            "priority": self.priority
        }
        response = client.post(self.url, json=data)
        assert response.status_code == 200

    def test_user_update_two(self, client):
        data = {
            "email": self.email1,
            "password": self.password,
            "priority": self.priority
        }
        response = client.post(self.url, json=data)
        assert response.status_code == 400
        assert response.json == {'result' : "Can't find this user!!"}


@pytest.mark.api
class TestUserDelete():
    email = "12345@gmail.com"
    email1 = "54321@gmail.com"
    url = "/user/delete"

    def test_user_delete_one(self, client):
        data = {
            "email": self.email
        }
        response = client.post(self.url, json=data)
        assert response.status_code == 200

    def test_user_delete_two(self, client):
        data = {
            "email": self.email1
        }
        response = client.post(self.url, json=data)
        assert response.status_code == 400
        assert response.json == {'result' : "Can't find this user!!"}