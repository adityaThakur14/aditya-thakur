import re
import pytest
import requests
from fixtures.constants import ResponseText
from fixtures.UserInfo import UserPage
from faker import Faker


class TestUserEndpoints():

    userInfo = UserPage()
    Responses = ResponseText()

    @pytest.mark.dependency()
    def test_create_user(self, create_user):
        """Test user creation."""
        response = self.userInfo.add_user_api(create_user)
        assert response.status_code == 200
        assert response.json()["username"] == create_user["username"]

    def test_create_user_list(self, create_user_list):
        """Test user creation from a list"""

        response = self.userInfo.add_user_from_list(create_user_list)

        assert response.status_code == 200
        assert response.json() == create_user_list

    def test_login_user(self, create_user):
        """Test user login."""
        self.userInfo.add_user_api(create_user)
        username = create_user["username"]
        password = create_user["password"]
        response = self.userInfo.verify_userLogin(username,password)
        assert response.status_code == 200
        rmatch = re.search(self.Responses.MESSAGE_USER_LOGIN_SUCCESS,response.text)
        assert rmatch is not None

    def test_logout_user(self):
        """Test user logout."""
        response = self.userInfo.verify_userLogout()
        assert response.status_code == 200
        assert self.Responses.MESSAGE_USER_LOGOUT in response.text

    def test_get_user(self, create_user):
        """Test fetching user by username."""
        self.userInfo.add_user_api(create_user)
        username = create_user["username"]
        response = self.userInfo.get_user(username)
        assert response.status_code == 200
        assert response.json()["username"] == username
        assert response.json()["id"] == create_user["id"]

    def test_update_user(self, create_user):
        """Test updating user information."""
        username = create_user["username"]
        self.userInfo.add_user_api(create_user)
        username = create_user["username"]
        password = create_user["password"]
        response = self.userInfo.verify_userLogin(username,password)
        assert response.status_code == 200
        updated_data = create_user.copy()
        updated_data["firstName"] = "Aditya"

        response = self.userInfo.update_user(updated_data)
        assert response.status_code == 200

        """Verify User Update"""
        response = self.userInfo.get_user(username)
        assert response.status_code == 200
        assert response.json()["firstName"] == "Aditya"

    def test_delete_user(self, create_user):
        """Test deleting a user."""
        self.userInfo.add_user_api(create_user)
        username = create_user["username"]
        password = create_user["password"]
        response = self.userInfo.verify_userLogin(username,password)
        assert response.status_code == 200
        """Delete the user"""
        response = self.userInfo.delete_user(username)
        assert response.status_code == 200

        """Verify User Delete"""
        response = self.userInfo.get_user(username)
        assert response.status_code == 404

    """NEGATIVE TEST CASES"""

    @pytest.mark.negative
    def test_invalid_login(self, create_user):
        """Test user login."""
        self.userInfo.add_user_api(create_user)
        username = "myUsername"
        password = "myPassword"
        response = self.userInfo.verify_userLogin(username, password)
        assert response.status_code == 400
        rmatch = re.search(self.Responses.MESSAGE_USER_LOGIN_SUCCESS, response.text)
        assert rmatch is not None

    @pytest.mark.negative
    def test_fetch_invalid_user(self, create_user):
        """Test fetching user by username."""
        self.userInfo.add_user_api(create_user)
        fake = Faker()
        username = fake.user_name()
        response = self.userInfo.get_user(username)
        assert response.status_code == 404

    @pytest.mark.negative
    def test_invalid_delete(self, create_user):
        """Test deleting a user."""
        self.userInfo.add_user_api(create_user)
        username = create_user["username"]

        """Logout Users"""
        response = self.userInfo.verify_userLogout()
        assert response.status_code == 200
        """Delete the user"""

        response = self.userInfo.delete_user(username)
        assert response.status_code == 400, "User got deleted without login"

        """Verify User Delete"""
        response = self.userInfo.get_user(username)
        assert response.status_code == 200