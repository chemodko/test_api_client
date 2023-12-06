from src.models.user_controller import UserInfoResponse, UnauthorizedError


class TestGetUserInfo:
    def test_get_user_info(self, user_controller_post_user_auth):
        resp = user_controller_post_user_auth.get_user_info(status_code=200, model=UserInfoResponse)

        assert resp.login == user_controller_post_user_auth.login, "Invalid login"
        assert resp.password == user_controller_post_user_auth.password, "Invalid password"
        assert resp.games == [], "Invalid games list"

    def test_get_user_info_unauthorized(self, user_controller_post_user):
        user_controller_post_user.get_user_info(status_code=401, model=UnauthorizedError)

