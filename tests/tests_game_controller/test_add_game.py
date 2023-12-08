import allure
from src.models.game_controller import GameFactory, UnauthorizedError
from src.utils.constants.messages import GameMessage
import pytest


@allure.feature("Adding new game")
class TestAddGame:
    @allure.title("Add new game")
    def test_add_game(self, game_controller_auth_delete):
        game = GameFactory().model_dump(by_alias=True)
        game_controller_auth_delete.post_add_game(game, status_code=201,
                                                  exp_msg=GameMessage.game_created.value)

    @allure.title("Add new game without authorization")
    def test_add_game_unauthorized(self, game_controller):
        game = GameFactory().model_dump(by_alias=True)
        game_controller.post_add_game(game, status_code=401, model=UnauthorizedError)

    @allure.title("Add new game with wrong fields")
    @pytest.mark.skip(reason="Always causes Internal server error 500")
    def test_add_game_wrong_game_fields(self, game_controller_auth_delete):
        game = {"title": "GTA66"}
        game_controller_auth_delete.post_add_game(game_data=game, status_code=400)

    @allure.title("Adding a game that exceeds the 20-game limit")
    def test_add_game_cant_add_more_than_20(self, game_controller_auth_delete):
        game = GameFactory().model_dump(by_alias=True)
        games_num = len(game_controller_auth_delete.get_games_list())
        for i in range(21 - games_num):
            game_controller_auth_delete.post_add_game(game, status_code=201,
                                                      exp_msg=GameMessage.game_created.value)
        game_controller_auth_delete.post_add_game(game, status_code=400,
                                                  exp_msg=GameMessage.games_limit.value)


