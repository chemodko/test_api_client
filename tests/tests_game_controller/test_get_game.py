from src.utils.randoms import random_number
from src.models.game_controller import GameFactory, Game, UnauthorizedError, InfoResponse
from src.utils.constants.messages import GameMessage
import pytest


class TestGetGame:
    @pytest.mark.skip(reason="Wrong game id, required age")
    def test_get_game_info(self, game_controller_auth_delete):
        game = GameFactory().model_dump(by_alias=True)
        game_controller_auth_delete.post_add_game(game)
        game_id = game_controller_auth_delete.get_games_list()[0].game_id
        resp = game_controller_auth_delete.get_game_info(game_id=game_id, status_code=200)
        assert resp == Game(**game)

    def test_get_game_info_unauthorized(self, game_controller_auth_delete):
        game = GameFactory().model_dump(by_alias=True)
        game_controller_auth_delete.post_add_game(game)
        game_id = game_controller_auth_delete.get_games_list()[0].game_id
        game_controller_auth_delete.logout()
        game_controller_auth_delete.get_game_info(game_id=game_id, status_code=401, model=UnauthorizedError)

    def test_get_game_info_that_not_exist(self, game_controller_auth):
        game_controller_auth.get_game_info(game_id=random_number(10**3, 10**6), status_code=400,
                                           exp_msg=GameMessage.game_not_exist.value, model=InfoResponse)


