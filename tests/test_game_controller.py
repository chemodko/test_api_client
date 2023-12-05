from src.controllers.game_controller import GameControllerApiClient
from src.utils.randoms import random_string


def test_get_games_list_positive():
    game_controller = GameControllerApiClient("chemodko2", "password")
    game_controller.auth()
    game_controller.get_games_list(status_code=200)


def test_get_games_list_unauthorized():
    game_controller = GameControllerApiClient("chemodko2", "password")
    game_controller.get_games_list(status_code=401)



