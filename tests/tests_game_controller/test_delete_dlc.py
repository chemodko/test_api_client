from src.utils.randoms import random_number
from src.models.game_controller import GameFactory, Game, UnauthorizedError, InfoResponse
from src.utils.constants.messages import GameMessage
import pytest


def test_delete_dlc_positive(game_controller):
    game_controller.auth()
    game = games[1]
    game_controller.post_add_game(game)
    game_id = game_controller.get_games_list()[0].game_id
    game_controller.delete_dlc(game_id=game_id, dlc_list=dlcs, status_code=200)


def test_delete_dlc_game_not_exist(game_controller):
    game_controller.auth()
    game_controller.delete_dlc(game_id=random_number(), dlc_list=dlcs, status_code=400)


def test_delete_dlc_empty_dlc_list(game_controller):
    game_controller.auth()
    game = games[1]
    game_controller.post_add_game(game)
    game_id = game_controller.get_games_list()[0].game_id
    game_controller.delete_dlc(game_id=game_id, dlc_list=[], status_code=400)


def test_delete_dlc_unauthorized(game_controller):
    game_controller.auth()
    game = games[1]
    game_controller.post_add_game(game)
    game_id = game_controller.get_games_list()[0].game_id
    game_controller.logout()
    game_controller.delete_dlc(game_id=game_id, dlc_list=dlcs, status_code=401)


@pytest.mark.skip(reason="Wrong response status code")
def test_delete_dlc_wrong_dlc(game_controller):
    game_controller.auth()
    game = games[1]
    game_controller.post_add_game(game)
    game_id = game_controller.get_games_list()[0].game_id
    dlc_list = [{"something": "Cars dlc"}]
    game_controller.delete_dlc(game_id=game_id, dlc_list=dlc_list, status_code=400)


def test_update_game_field_positive(game_controller):
    game_controller.auth()
    game = games[1]
    game_controller.post_add_game(game)
    game_id = game_controller.get_games_list()[0].game_id
    field_data = {
        "fieldName": "description",
        "value": "NEW DESCRIPTION"
    }
    game_controller.put_update_game_field(game_id=game_id, field_data=field_data, status_code=200)


def test_update_game_field_that_not_exist(game_controller):
    game_controller.auth()
    game = games[1]
    game_controller.post_add_game(game)
    game_id = game_controller.get_games_list()[0].game_id
    field_data = {
        "fieldName": "something",
        "value": "NEW DESCRIPTION"
    }
    game_controller.put_update_game_field(game_id=game_id, field_data=field_data, status_code=400)


def test_update_game_field_wrong_field_type(game_controller):
    game_controller.auth()
    game = games[1]
    game_controller.post_add_game(game)
    game_id = game_controller.get_games_list()[0].game_id
    field_data = {
        "fieldName": "description",
        "value": 1234
    }
    game_controller.put_update_game_field(game_id=game_id, field_data=field_data, status_code=400)


def test_update_game_field_unauthorized(game_controller):
    game_controller.auth()
    game = games[1]
    game_controller.post_add_game(game)
    game_id = game_controller.get_games_list()[0].game_id
    field_data = {
        "fieldName": "description",
        "value": "NEW DESCRIPTION"
    }
    game_controller.logout()
    game_controller.put_update_game_field(game_id=game_id, field_data=field_data, status_code=401)