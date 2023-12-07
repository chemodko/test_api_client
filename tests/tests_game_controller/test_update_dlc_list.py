from src.utils.randoms import random_number
from src.models.game_controller import UnauthorizedError, DLCFactory, DLC
from src.utils.constants.messages import GameMessage
import pytest


class TestUpdateDLCList:
    @pytest.mark.skip(reason="Old DLCs doesn't deleted")
    def test_update_dlc_list(self, game_controller_auth_post_game_delete):
        game_id = game_controller_auth_post_game_delete.get_games_list()[0].game_id
        dlcs = [DLCFactory().model_dump(by_alias=True) for _ in range(2)]
        game_controller_auth_post_game_delete.put_update_dlc_list(game_id=game_id, dlc_list=dlcs, status_code=200,
                                                                  exp_msg=GameMessage.dlc_changed.value)
        dlcs_models = [DLC(**dlcs[i]) for i in range(len(dlcs))]
        assert game_controller_auth_post_game_delete.get_games_list()[0].dlcs == dlcs_models

    def test_update_dlc_list_game_not_exist(self, game_controller_auth):
        dlcs = [DLCFactory().model_dump(by_alias=True) for _ in range(2)]
        game_controller_auth.put_update_dlc_list(game_id=random_number(10 ** 3, 10 ** 6), dlc_list=dlcs,
                                                 status_code=400,
                                                 exp_msg=GameMessage.game_not_exist.value)

    @pytest.mark.skip(reason="DLC successfully changed, but it shouldn't")
    def test_update_dlc_list_wrong_dlc_fields(self, game_controller_auth_post_game_delete):
        game_id = game_controller_auth_post_game_delete.get_games_list()[0].game_id
        dlc_list = [{"something": "Cars dlc"}]
        game_controller_auth_post_game_delete.put_update_dlc_list(game_id=game_id, dlc_list=dlc_list, status_code=400)

    def test_update_dlc_list_unauthorized(self, game_controller_auth_post_game_delete):
        game_id = game_controller_auth_post_game_delete.get_games_list()[0].game_id
        game_controller_auth_post_game_delete.logout()
        dlcs = [DLCFactory().model_dump(by_alias=True) for _ in range(2)]
        game_controller_auth_post_game_delete.put_update_dlc_list(game_id=game_id, dlc_list=dlcs, status_code=401,
                                                                  model=UnauthorizedError)
