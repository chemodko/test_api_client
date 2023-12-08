import allure
from src.models.game_controller import UnauthorizedError
from src.models.game_controller import GameFactory, Game
import pytest


@allure.feature("Getting list of all games")
class TestGetGamesList:
    @allure.title("Get empty list of games")
    def test_get_games_empty_list(self, game_controller_auth):
        resp = game_controller_auth.get_games_list(status_code=200)
        assert resp == []

    @allure.title("Getting list of games")
    @pytest.mark.skip(reason="Wrong game id, required age")
    def test_get_games_list(self, game_controller_auth_delete):
        game = GameFactory().model_dump(by_alias=True)
        game_controller_auth_delete.post_add_game(game)
        resp = game_controller_auth_delete.get_games_list(status_code=200)
        assert resp == [Game(**game)]  # game_id, req_age

    @allure.title("Getting list of games without authorization")
    def test_get_games_list_unauthorized(self, game_controller):
        game_controller.get_games_list(status_code=401, model=UnauthorizedError)







