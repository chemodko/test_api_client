import pytest
from src.utils.randoms import random_string
from src.utils.constants.messages import UserMessage
from src.models.game_controller import GameFactory


class TestRegisterUser:
    def test_register_new_user(self, user_controller):
        login = random_string(20, 20)
        password = random_string(20, 20)
        resp = user_controller.post_api_signup(login, password, status_code=201)
        assert resp.info.message == UserMessage.user_created, "Invalid message"
        assert resp.register_data.login == login, "Invalid login"
        assert resp.register_data.password == password, "Invalid password"
        assert resp.register_data.games == [], "Invalid games list"

    def test_register_user_that_exist(self, user_controller_without_deleting):
        resp = user_controller_without_deleting.post_api_signup("admin", random_string(), status_code=400)
        assert resp.info.message == UserMessage.login_exist, "Invalid message"

    def test_register_user_without_login(self, user_controller_without_deleting):
        resp = user_controller_without_deleting.post_api_signup(None, random_string(), status_code=400)
        assert resp.info.message == UserMessage.miss, "Invalid message"

    def test_register_user_without_password(self, user_controller_without_deleting):
        resp = user_controller_without_deleting.post_api_signup(random_string(), None, status_code=400)
        assert resp.info.message == UserMessage.miss, "Invalid message"

    def test_register_user_without_login_and_password(self, user_controller_without_deleting):
        resp = user_controller_without_deleting.post_api_signup(None, None, status_code=400)
        assert resp.info.message == UserMessage.miss, "Invalid message"

    @pytest.mark.skip(reason="Always causes 500 Internal server error")
    def test_register_new_user_with_games(self, user_controller):
        login = random_string(20, 20)
        password = random_string(20, 20)
        game = GameFactory().model_dump(by_alias=True)
        resp = user_controller.post_api_signup(login=login, password=password, games=[game], status_code=201)
        assert resp.info.message == UserMessage.user_created, "Invalid message"
        assert resp.register_data.login == login, "Invalid login"
        assert resp.register_data.password == password, "Invalid password"
        assert resp.register_data.games == [game], "Invalid games list"
