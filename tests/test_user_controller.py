
def test_register_user_positive(user_controller):
    user_controller.post_new_user(user_controller.login, user_controller.password)


def test_get_user_info(user_controller):
    user_controller.post_new_user()
    user_controller.auth()
    user_controller.get_user_info()


def test_put_new_user_password(user_controller):
    user_controller.post_new_user()
    user_controller.auth()
    user_controller.put_user_password("newpassword")


def test_delete_user(user_controller):
    if user_controller.login in user_controller.get_users_info().response:
        user_controller.auth()
        user_controller.delete_user()
    else:
        print("---User doesn't exist---")


def test_get_all_users_logins(user_controller):
    user_controller.get_users_info()










