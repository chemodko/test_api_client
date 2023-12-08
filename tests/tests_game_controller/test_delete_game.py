import allure
from src.utils.randoms import random_number
from src.models.game_controller import GameFactory, UnauthorizedError
from src.utils.constants.messages import GameMessage


@allure.feature("Deleting game")
class TestDeleteGame:
    @allure.title("Deleting of existing game")
    def test_delete_game(self, game_controller_auth):
        game = GameFactory().model_dump(by_alias=True)
        game_controller_auth.post_add_game(game)
        game_id = game_controller_auth.get_games_list()[0].game_id
        game_controller_auth.delete_game(game_id=game_id, status_code=200, exp_msg=GameMessage.game_deleted.value)
        assert len(game_controller_auth.get_games_list()) == 0

    @allure.title("Deleting of the game without authorization")
    def test_delete_game_unauthorized(self, game_controller_auth_delete):
        game = GameFactory().model_dump(by_alias=True)
        game_controller_auth_delete.post_add_game(game)
        game_id = game_controller_auth_delete.get_games_list()[0].game_id
        game_controller_auth_delete.logout()
        game_controller_auth_delete.delete_game(game_id=game_id, status_code=401, model=UnauthorizedError)

        game_controller_auth_delete.auth()
        assert len(game_controller_auth_delete.get_games_list()) == 1

    @allure.title("Deleting game that not exist")
    def test_delete_game_that_not_exist(self, game_controller_auth):
        game_controller_auth.delete_game(game_id=random_number(10**3, 10**6), status_code=400,
                                         exp_msg=GameMessage.game_not_exist.value)


