import pytest
from src.utils.randoms import random_string
from src.utils.constants.messages import UserMessage
from src.models.game_controller import GameFactory
import allure


@allure.feature("Register user")
class TestRegisterUser:
    @allure.title("Register new user with login and password")
    def test_register_new_user(self, user_controller):
        login = random_string(20, 20)
        password = random_string(20, 20)
        resp = user_controller.post_api_signup(login=login, password=password,
                                               status_code=201, exp_msg=UserMessage.user_created.value)

        assert resp.register_data.login == login, "Invalid login"
        assert resp.register_data.password == password, "Invalid password"
        assert resp.register_data.games == [], "Invalid games list"

    @allure.title("Register user that exist")
    def test_register_user_that_exist(self, user_controller_without_deleting):
        user_controller_without_deleting.post_api_signup(login="admin", password=random_string(),
                                                         status_code=400, exp_msg=UserMessage.login_exist.value)

    @allure.title("Register user without login")
    def test_register_user_without_login(self, user_controller_without_deleting):
        user_controller_without_deleting.post_api_signup(login=None, password=random_string(),
                                                         status_code=400, exp_msg=UserMessage.miss.value)

    @allure.title("Register user without password")
    def test_register_user_without_password(self, user_controller_without_deleting):
        user_controller_without_deleting.post_api_signup(login=random_string(), password=None,
                                                         status_code=400, exp_msg=UserMessage.miss.value)

    @allure.title("Register user without login and password")
    def test_register_user_without_login_and_password(self, user_controller_without_deleting):
        user_controller_without_deleting.post_api_signup(login=None, password=None,
                                                         status_code=400, exp_msg=UserMessage.miss.value)

    @allure.title("Register user with list of games")
    @pytest.mark.skip(reason="Always causes 500 Internal server error")
    def test_register_new_user_with_games(self, user_controller):
        login = random_string(20, 20)
        password = random_string(20, 20)
        game = GameFactory().model_dump(by_alias=True)
        resp = user_controller.post_api_signup(login=login, password=password, games=[game],
                                               status_code=201, exp_msg=UserMessage.user_created.value)

        assert resp.register_data.login == login, "Invalid login"
        assert resp.register_data.password == password, "Invalid password"
        assert resp.register_data.games == [game], "Invalid games list"
