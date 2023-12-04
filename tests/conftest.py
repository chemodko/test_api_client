import pytest
from src.controllers.user_controller import UserControllerApiClient
import time


@pytest.fixture
def user_controller():
    user_controller = UserControllerApiClient()
    yield user_controller
    if user_controller.login in user_controller.get_users_info().info:
        if user_controller.can_auth():
            user_controller.auth()
            user_controller.delete_user()
