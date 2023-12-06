from src.models.user_controller import UnauthorizedError
from src.utils.constants.messages import UserMessage


class TestPutNewPassword:
    def test_put_new_user_password(self, user_controller_post_user_auth):
        newpassword = "newpassword"
        user_controller_post_user_auth.put_user_password(new_password=newpassword, status_code=200,
                                                         exp_msg=UserMessage.pass_changed.value)
        assert newpassword == user_controller_post_user_auth.get_user_info().password

    def test_put_new_user_password_unauthorized(self, user_controller_post_user):
        user_controller_post_user.put_user_password(new_password="newpassword", status_code=401,
                                                    model=UnauthorizedError)

    def test_put_new_user_password_wrong(self, user_controller_post_user_auth):
        user_controller_post_user_auth.put_user_password(new_password=None, status_code=400,
                                                         exp_msg=UserMessage.empty_pass.value)

    def test_check_authorize_after_password_change(self, user_controller_post_user_auth):
        old_password = user_controller_post_user_auth.password
        new_password = "newpassword"
        user_controller_post_user_auth.put_user_password(new_password=new_password, status_code=200,
                                                         exp_msg=UserMessage.pass_changed.value)
        log_in_data = {
            "username": user_controller_post_user_auth.login,
            "password": old_password
        }
        token_resp = user_controller_post_user_auth.post(f"{user_controller_post_user_auth.base_url}/login",
                                                         json=log_in_data, status_code=401)
        assert token_resp["status"] == 401


