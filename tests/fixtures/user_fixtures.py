import pytest
from src.controllers.user_controller import UserControllerApiClient


@pytest.fixture
def user_controller():
    user_controller = UserControllerApiClient()
    yield user_controller
    user_controller.auth()
    user_controller.delete_user()


@pytest.fixture
def user_controller_auth():
    user_controller_auth = UserControllerApiClient()
    user_controller_auth.auth()
    yield user_controller_auth
    user_controller_auth.delete_user()


@pytest.fixture
def user_controller_without_deleting():
    user_controller_without_deleting = UserControllerApiClient()
    yield user_controller_without_deleting


