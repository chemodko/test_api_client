import pytest
from src.controllers.game_controller import GameControllerApiClient


@pytest.fixture
def game_controller():
    game_controller = GameControllerApiClient("chemodko2", "password")
    yield game_controller


@pytest.fixture
def game_controller_auth():
    game_controller_auth = GameControllerApiClient("chemodko2", "password")
    game_controller_auth.auth()
    yield game_controller_auth


@pytest.fixture
def game_controller_auth_delete():
    game_controller_auth_delete = GameControllerApiClient("chemodko2", "password")
    game_controller_auth_delete.auth()
    yield game_controller_auth_delete
    game_controller_auth_delete.auth()
    for game in game_controller_auth_delete.get_games_list():
        game_controller_auth_delete.delete_game(game_id=game.game_id)

        