from src.models.game_controller import *
from src.http_api_client import HttpApiClient


class GameControllerApiClient(HttpApiClient):
    def __init__(self, login: str = None, password: str = None):
        super().__init__()
        if login is not None:
            self.login = login
        if password is not None:
            self.password = password

    def get_games_list(self, status_code: int = 200, model=Game):
        """Getting games list of the user (must be authorized with a token)."""
        resp = self.get(f"{self.base_url}/user/games", status_code=status_code)
        if isinstance(resp, list):
            games = []
            for r in resp:
                games.append(model(**r))
            return games
        else:
            return model(**resp)

    def post_add_game(self, game_data: dict, status_code: int = 201, exp_msg: str = None, model=GameAddedResponse):
        """Adds a game for the user (must be authorized with a token)."""
        resp = self.post(f"{self.base_url}/user/games", json=game_data, status_code=status_code, exp_msg=exp_msg)
        return model(**resp)

    def get_game_info(self, game_id: int, status_code: int = 200, exp_msg: str = None, model=Game):
        """Gets information about the game (must be authorized with a token)."""
        resp = self.get(f"{self.base_url}/user/games/{game_id}", status_code=status_code, exp_msg=exp_msg)
        return model(**resp)

    def delete_game(self, game_id: int, status_code: int = 200, exp_msg: str = None, model=InfoResponse):
        """Deletes the user's game (must be authorized with a token)."""
        resp = self.delete(f"{self.base_url}/user/games/{game_id}", status_code=status_code, exp_msg=exp_msg)
        return model(**resp)

    def put_update_dlc_list(self, game_id: int, dlc_list: list, status_code: int = 200, exp_msg: str = None, model=InfoResponse):
        """Updates the game's DLC list (must be authorized with a token)."""
        resp = self.put(f"{self.base_url}/user/games/{game_id}", json=dlc_list, status_code=status_code, exp_msg=exp_msg)
        return model(**resp)

    def delete_dlc(self, game_id: int, dlc_list: list, status_code: int = 200, exp_msg: str = None, model=InfoResponse):
        """Deletes the user's game's DLC (must be authorized with a token)."""
        resp = self.delete(f"{self.base_url}/user/games/{game_id}/dlc", json=dlc_list, status_code=status_code, exp_msg=exp_msg)
        return model(**resp)

    def put_update_game_field(self, game_id: int, field_data: dict, status_code: int = 200, exp_msg: str = None, model=InfoResponse):
        """Update's the user's game field (must be authorized with a token)."""
        resp = self.put(f"{self.base_url}/user/games/{game_id}/updateField", json=field_data, status_code=status_code, exp_msg=exp_msg)
        # if status_code == 200 or status_code == 400:
        #     return InfoResponse(**resp)
        # elif status_code == 401:
        #     return UnauthorizedError(**resp)
        return model(**resp)


