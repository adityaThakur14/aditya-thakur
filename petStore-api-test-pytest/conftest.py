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








