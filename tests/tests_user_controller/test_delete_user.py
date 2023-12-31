import allure
from src.models.user_controller import UnauthorizedError
from src.utils.constants.messages import UserMessage


@allure.feature("Delete user")
class TestDeleteUser:
    @allure.title("Delete user")
    def test_delete_user(self, user_controller_post_user_auth_without_deleting):
        user_controller_post_user_auth_without_deleting.delete_user(status_code=200,
                                                                    exp_msg=UserMessage.user_deleted.value)
        assert user_controller_post_user_auth_without_deleting.login not in \
               user_controller_post_user_auth_without_deleting.get_users_info().info

    @allure.title("Delete user without authentication")
    def test_delete_user_unauthorized(self, user_controller_post_user):
        user_controller_post_user.delete_user(status_code=401, model=UnauthorizedError)

    @allure.title("Checking that user cannot authenticate after deleting")
    def test_check_authorize_after_user_deleted(self, user_controller_post_user_auth_without_deleting):
        user_controller_post_user_auth_without_deleting.delete_user(status_code=200,
                                                                    exp_msg=UserMessage.user_deleted.value)
        log_in_data = {
            "username": user_controller_post_user_auth_without_deleting.login,
            "password": user_controller_post_user_auth_without_deleting.password
        }
        token_resp = user_controller_post_user_auth_without_deleting.post(
            f"{user_controller_post_user_auth_without_deleting.base_url}/login",
            json=log_in_data, status_code=401)
        assert token_resp["status"] == 401
