import pytest
from src.controllers.game_controller import GameControllerApiClient


@pytest.fixture
def game_controller():
    game_controller = GameControllerApiClient("chemodko2", "password")
    yield game_controller
    game_controller.auth()
    for game in game_controller.get_games_list(status_code=200):
        game_id = game.game_id
        game_controller.delete_game(game_id=game_id)

        