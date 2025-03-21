import logging

import pytest
import random


from fixtures.base import BaseClass
from fixtures.UserInfo import UserPage


logger = logging.getLogger("api")

BASE_URL = "http://localhost:8080/api/v3"
USER_ENDPOINT = f"{BASE_URL}/user"



@pytest.fixture
def create_user():
    """Fixture to create a user before running a test."""
    uInfo = UserPage()
    user_payload = uInfo.add_user_info()
    yield user_payload

@pytest.fixture
def create_user_list():
    """Fixture to create a user from a list"""
    uInfo = UserPage()
    user_payload = []
    user_payload.append(uInfo.add_user_info())
    user_payload.append(uInfo.add_user_info())
    yield user_payload

def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="http://localhost:8080/api/v3",
    ),




'''
@pytest.fixture
def register_user(app) -> UserStore:
    """
    Register new user
    """
    data = RegisterUser.random()
    res = app.register.register(data=data, type_response=RegisterUserResponse)
    data = UserStore(user=data, user_uuid=res.data.uuid)
    return data


@pytest.fixture
def auth_user(app, register_user) -> UserStore:
    """
    Login user
    """
    res = app.auth.login(data=register_user.user, type_response=AuthUserResponse)
    token = res.data.access_token
    header = {"Authorization": f"JWT {token}"}
    data = UserStore(**register_user.to_dict())
    data.header = header
    return data


@pytest.fixture
def user_info_(app, auth_user) -> UserStore:
    """
    Add user info
    """
    data = AddUserInfo.random()
    app.user_info.add_user_info(
        user_id=auth_user.user_uuid, data=data, header=auth_user.header
    )
    data_user = UserStore(**auth_user.to_dict())
    data_user.user_info = data
    return data_user

'''





