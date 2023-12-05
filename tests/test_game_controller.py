from src.utils.randoms import random_number
from tests.games import games
import pytest


def test_get_games_list_positive(game_controller):
    game_controller.auth()
    game_controller.get_games_list(status_code=200)


def test_get_games_list_unauthorized(game_controller):
    game_controller.get_games_list(status_code=401)


def test_add_game_positive(game_controller):
    game_controller.auth()
    game = games[0]
    game_controller.post_add_game(game, status_code=201)


# @pytest.mark.skip(reason="Causes Internal server error 500")
def test_add_game_cant_add_more(game_controller):
    game_controller.auth()
    game = games[0]
    games_num = len(game_controller.get_games_list(status_code=200))
    for i in range(21 - games_num):
        game_controller.post_add_game(game, status_code=201)
    game_controller.post_add_game(game, status_code=400)


def test_get_game_info_positive(game_controller):
    game_controller.auth()
    game = games[0]
    game_controller.post_add_game(game, status_code=201)
    game_id = game_controller.get_games_list(status_code=200)[0].game_id
    game_controller.get_game_info(game_id=game_id, status_code=200)


def test_get_game_info_unauthorized(game_controller):
    game_controller.auth()
    game = games[0]
    game_controller.post_add_game(game, status_code=201)
    game_id = game_controller.get_games_list(status_code=200)[0].game_id
    game_controller.de_auth()
    game_controller.get_game_info(game_id=game_id, status_code=401)


def test_get_game_info_wrong(game_controller):
    game_controller.auth()
    game_controller.get_game_info(game_id=random_number(), status_code=400)


def test_delete_game_positive(game_controller):
    game_controller.auth()
    game = games[0]
    game_controller.post_add_game(game, status_code=201)
    game_id = game_controller.get_games_list(status_code=200)[0].game_id
    game_controller.delete_game(game_id=game_id, status_code=200)


def test_delete_game_unauthorized(game_controller):
    game_controller.auth()
    game = games[0]
    game_controller.post_add_game(game, status_code=201)
    game_id = game_controller.get_games_list(status_code=200)[0].game_id
    game_controller.de_auth()
    game_controller.delete_game(game_id=game_id, status_code=401)


def test_delete_game_that_not_exist(game_controller):
    game_controller.auth()
    game_controller.delete_game(game_id=random_number(), status_code=400)




