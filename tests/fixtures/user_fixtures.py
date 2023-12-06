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
def user_controller_post_user_auth():
    user_controller_post_user_auth = UserControllerApiClient()
    user_controller_post_user_auth.post_api_signup(user_controller_post_user_auth.login, user_controller_post_user_auth.password)
    user_controller_post_user_auth.auth()
    yield user_controller_post_user_auth
    user_controller_post_user_auth.delete_user()


@pytest.fixture
def user_controller_post_user():
    user_controller_post_user = UserControllerApiClient()
    user_controller_post_user.post_api_signup(user_controller_post_user.login, user_controller_post_user.password)
    yield user_controller_post_user
    user_controller_post_user.auth()
    user_controller_post_user.delete_user()


@pytest.fixture
def user_controller_without_deleting():
    user_controller_without_deleting = UserControllerApiClient()
    yield user_controller_without_deleting


@pytest.fixture
def user_controller_post_user_auth_without_deleting():
    user_controller_post_user_auth_without_deleting = UserControllerApiClient()
    user_controller_post_user_auth_without_deleting.post_api_signup(user_controller_post_user_auth_without_deleting.login,
                                                                    user_controller_post_user_auth_without_deleting.password)
    user_controller_post_user_auth_without_deleting.auth()
    yield user_controller_post_user_auth_without_deleting


