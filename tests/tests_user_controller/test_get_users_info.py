import allure


@allure.title("Get all users logins")
def test_get_all_users_logins(user_controller_without_deleting):
    resp = user_controller_without_deleting.get_users_info(status_code=200)
    assert "admin" in resp.info
