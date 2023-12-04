import pytest
from src.utils.randoms import random_string


def test_register_user_positive(user_controller):
    test_login = random_string()
    while test_login in user_controller.get_users_info().info:
        test_login = random_string()
    user_controller.post_new_user(test_login, "password", status_code=201)


@pytest.mark.parametrize("login,password", [("admin", "string"),
                                            (None, "password"),
                                            (None, None),
                                            (random_string(), None)])
def test_register_user_negative(user_controller, login, password):
    user_controller.post_new_user(login, password, status_code=400)


def test_get_user_info(user_controller):
    user_controller.post_new_user(user_controller.login, user_controller.password)
    user_controller.auth()
    user_controller.get_user_info()


def test_put_new_user_password(user_controller):
    user_controller.post_new_user(user_controller.login, user_controller.password)
    user_controller.auth()
    user_controller.put_user_password("newpassword")


def test_delete_user(user_controller):
    if user_controller.login in user_controller.get_users_info().info:
        if user_controller.can_auth():
            user_controller.auth()
            user_controller.delete_user()
        else:
            print("---User can't auth---")
    else:
        print("---User doesn't exist---")


def test_get_all_users_logins(user_controller):
    user_controller.get_users_info()
