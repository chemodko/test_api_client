from src.utils.randoms import random_number
from src.models.game_controller import UnauthorizedError
from src.utils.constants.messages import GameMessage
import pytest


class TestDeleteDLC:
    @pytest.mark.skip("DLCs are not deleted")
    def test_delete_dlc(self, game_controller_auth_post_game_delete):
        game_id = game_controller_auth_post_game_delete.get_games_list()[0].game_id
        dlcs = [d.model_dump() for d in game_controller_auth_post_game_delete.get_game_info(game_id=game_id).dlcs]
        game_controller_auth_post_game_delete.delete_dlc(game_id=game_id, dlc_list=dlcs, status_code=200,
                                                         exp_msg=GameMessage.dlc_deleted.value)
        assert len(game_controller_auth_post_game_delete.get_game_info(game_id=game_id).dlcs) == 0

    def test_delete_dlc_game_not_exist(self, game_controller_auth):
        game_controller_auth.delete_dlc(game_id=random_number(10**3, 10**6), dlc_list=[], status_code=400,
                                        exp_msg=GameMessage.game_not_exist.value)

    def test_delete_dlc_empty_dlc_list(self, game_controller_auth_post_game_delete):
        game_id = game_controller_auth_post_game_delete.get_games_list()[0].game_id
        game_controller_auth_post_game_delete.delete_dlc(game_id=game_id, dlc_list=[], status_code=400,
                                                         exp_msg=GameMessage.empty_dlc_list.value)

    def test_delete_dlc_unauthorized(self, game_controller_auth_post_game_delete):
        game_id = game_controller_auth_post_game_delete.get_games_list()[0].game_id
        dlcs = [d.model_dump() for d in game_controller_auth_post_game_delete.get_game_info(game_id=game_id).dlcs]
        game_controller_auth_post_game_delete.logout()
        game_controller_auth_post_game_delete.delete_dlc(game_id=game_id, dlc_list=dlcs, status_code=401,
                                                         model=UnauthorizedError)

    @pytest.mark.skip(reason="DLC successfully deleted, but it shouldn't")
    def test_delete_dlc_wrong_dlc(self, game_controller_auth_post_game_delete):
        game_id = game_controller_auth_post_game_delete.get_games_list()[0].game_id
        dlc_list = [{"something": "Cars dlc"}]
        game_controller_auth_post_game_delete.delete_dlc(game_id=game_id, dlc_list=dlc_list, status_code=400)


