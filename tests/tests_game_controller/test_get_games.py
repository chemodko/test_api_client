from src.models.game_controller import UnauthorizedError
from src.models.game_controller import GameFactory, Game
import pytest


class TestGetGamesList:
    def test_get_games_empty_list(self, game_controller_auth):
        resp = game_controller_auth.get_games_list(status_code=200)
        assert resp == []

    @pytest.mark.skip(reason="Wrong game id, required age")
    def test_get_games_list(self, game_controller_auth_delete):
        game = GameFactory().model_dump(by_alias=True)
        game_controller_auth_delete.post_add_game(game)
        resp = game_controller_auth_delete.get_games_list(status_code=200)
        assert resp == [Game(**game)]  # game_id, req_age

    def test_get_games_list_unauthorized(self, game_controller):
        game_controller.get_games_list(status_code=401, model=UnauthorizedError)







