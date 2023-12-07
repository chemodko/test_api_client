import pytest
from src.controllers.game_controller import GameControllerApiClient
from src.models.game_controller import GameFactory


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


@pytest.fixture
def game_controller_auth_post_game_delete():
    game_controller_auth_post_game_delete = GameControllerApiClient("chemodko2", "password")
    game_controller_auth_post_game_delete.auth()
    game = GameFactory().model_dump(by_alias=True)
    game_controller_auth_post_game_delete.post_add_game(game)
    yield game_controller_auth_post_game_delete
    game_controller_auth_post_game_delete.auth()
    for g in game_controller_auth_post_game_delete.get_games_list():
        game_controller_auth_post_game_delete.delete_game(game_id=g.game_id)

        