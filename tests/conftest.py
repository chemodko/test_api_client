import pytest
from src.controllers.user_controller import UserControllerApiClient
from src.controllers.game_controller import GameControllerApiClient
import time


@pytest.fixture
def user_controller():
    user_controller = UserControllerApiClient()
    yield user_controller
    if user_controller.login in user_controller.get_users_info().info:
        if user_controller.can_auth():
            user_controller.auth()
            user_controller.delete_user()


@pytest.fixture
def game_controller():
    game_controller = GameControllerApiClient("chemodko2", "password")
    yield game_controller
    game_controller.auth()
    for game in game_controller.get_games_list(status_code=200):
        game_id = game.game_id
        game_controller.delete_game(game_id=game_id)

