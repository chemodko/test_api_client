import allure
from src.models.game_controller import UnauthorizedError
from src.utils.constants.messages import GameMessage


@allure.feature("Updating of game field")
class TestUpdateGameField:
    @allure.title("Update game field")
    def test_update_game_field(self, game_controller_auth_post_game_delete):
        game_id = game_controller_auth_post_game_delete.get_games_list()[0].game_id
        field_data = {
            "fieldName": "description",
            "value": "NEW DESCRIPTION"
        }
        game_controller_auth_post_game_delete.put_update_game_field(game_id=game_id, field_data=field_data,
                                                                    status_code=200,
                                                                    exp_msg=GameMessage.field_updated.value)
        assert game_controller_auth_post_game_delete.get_game_info(game_id=game_id).description == field_data["value"]

    @allure.title("Update wrong(non-existing) game field")
    def test_update_game_field_that_not_exist(self, game_controller_auth_post_game_delete):
        game_id = game_controller_auth_post_game_delete.get_games_list()[0].game_id
        field_data = {
            "fieldName": "something",
            "value": "NEW DESCRIPTION"
        }
        game_controller_auth_post_game_delete.put_update_game_field(game_id=game_id, field_data=field_data,
                                                                    status_code=400,
                                                                    exp_msg=GameMessage.cant_find_field.value)

    @allure.title("Update game field with wrong type")
    def test_update_game_field_wrong_field_type(self, game_controller_auth_post_game_delete):
        game_id = game_controller_auth_post_game_delete.get_games_list()[0].game_id
        field_data = {
            "fieldName": "description",
            "value": 1234
        }
        game_controller_auth_post_game_delete.put_update_game_field(game_id=game_id, field_data=field_data,
                                                                    status_code=400,
                                                                    exp_msg=GameMessage.incorrect_field_type.value)
        assert game_controller_auth_post_game_delete.get_game_info(game_id=game_id).description != field_data["value"]

    @allure.title("Update game field without authorization")
    def test_update_game_field_unauthorized(self, game_controller_auth_post_game_delete):
        game_id = game_controller_auth_post_game_delete.get_games_list()[0].game_id
        field_data = {
            "fieldName": "description",
            "value": "NEW DESCRIPTION"
        }
        game_controller_auth_post_game_delete.logout()
        game_controller_auth_post_game_delete.put_update_game_field(game_id=game_id, field_data=field_data,
                                                                    status_code=401, model=UnauthorizedError)


