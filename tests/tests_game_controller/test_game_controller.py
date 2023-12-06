from src.utils.randoms import random_number
from tests.games import games, dlcs
from src.models.game_controller import GameFactory
import pytest


def test_get_games_empty_list_positive(game_controller):
    game_controller.auth()
    game_controller.get_games_list(status_code=200)


def test_get_games_list_positive(game_controller):
    game_controller.auth()
    game = games[0]
    game_controller.post_add_game(game)
    game_controller.get_games_list(status_code=200)


def test_get_games_list_unauthorized(game_controller):
    game_controller.get_games_list(status_code=401)


def test_add_game_positive(game_controller):
    game_controller.auth()
    # game = games[0]
    game = GameFactory().model_dump(by_alias=True)
    game_controller.post_add_game(game, status_code=201)


def test_add_game_unauthorized(game_controller):
    game = games[0]
    game_controller.post_add_game(game, status_code=401)


@pytest.mark.skip(reason="Always causes Internal server error 500")
def test_add_game_wrong_game_fields(game_controller):
    game_controller.auth()
    game = {"title": "GTA66"}
    game_controller.post_add_game(game_data=game, status_code=400)


# @pytest.mark.skip(reason="Causes Internal server error 500")
def test_add_game_cant_add_more_than_20(game_controller):
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
    game_controller.logout()
    game_controller.get_game_info(game_id=game_id, status_code=401)


def test_get_game_info_that_not_exist(game_controller):
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
    game_controller.logout()
    game_controller.delete_game(game_id=game_id, status_code=401)


def test_delete_game_that_not_exist(game_controller):
    game_controller.auth()
    game_controller.delete_game(game_id=random_number(), status_code=400)


def test_update_dlc_list_positive(game_controller):
    game_controller.auth()
    game = games[0]
    game_controller.post_add_game(game)
    game_id = game_controller.get_games_list(status_code=200)[0].game_id
    game_controller.put_update_dlc_list(game_id=game_id, dlc_list=dlcs, status_code=200)


def test_update_dlc_list_game_not_exist(game_controller):
    game_controller.auth()
    game_controller.put_update_dlc_list(game_id=random_number(), dlc_list=dlcs, status_code=400)


@pytest.mark.skip(reason="Wrong response status code")
def test_update_dlc_list_wrong_dlc(game_controller):
    game_controller.auth()
    game = games[0]
    game_controller.post_add_game(game)
    game_id = game_controller.get_games_list()[-1].game_id
    dlc_list = [{"something": "Cars dlc"}]
    game_controller.put_update_dlc_list(game_id=game_id, dlc_list=dlc_list, status_code=400)
    print(game_controller.get_games_list())


def test_update_dlc_list_unauthorized(game_controller):
    game_controller.auth()
    game = games[0]
    game_controller.post_add_game(game)
    game_id = game_controller.get_games_list(status_code=200)[0].game_id
    game_controller.logout()
    game_controller.put_update_dlc_list(game_id=game_id, dlc_list=dlcs, status_code=401)


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




