from typing import Union

from src.models.game_controller import *
from src.http_api_client import HttpApiClient


class GameControllerApiClient(HttpApiClient):
    def __init__(self, login: str = None, password: str = None):
        super().__init__()
        if login is not None:
            self.login = login
        if password is not None:
            self.password = password

    def get_games_list(self, status_code: int = 200) -> Union[list[Game], UnauthorizedError]:
        """Getting games list of the user (must be authorized with a token)."""
        resp = self.get(f"{self.base_url}/user/games", status_code=status_code)
        if status_code == 200:
            games = []
            for r in resp:
                games.append(Game(**r))
            return games
        elif status_code == 401:
            return UnauthorizedError(**resp)

    def post_add_game(self, game_data: dict, status_code: int = 201) -> Union[GameAddedResponse, UnauthorizedError]:
        """Adds a game for the user (must be authorized with a token)."""
        resp = self.post(f"{self.base_url}/user/games", json=game_data, status_code=status_code)
        if status_code == 201 or status_code == 400:
            return GameAddedResponse(**resp)
        elif status_code == 401:
            return UnauthorizedError(**resp)

    def get_game_info(self, game_id: int, status_code: int = 200) -> Union[Game, InfoResponse, UnauthorizedError]:
        """Gets information about the game (must be authorized with a token)."""
        resp = self.get(f"{self.base_url}/user/games/{game_id}", status_code=status_code)
        if status_code == 200:
            return Game(**resp)
        elif status_code == 400:
            return InfoResponse(**resp)
        elif status_code == 401:
            return UnauthorizedError(**resp)

    def delete_game(self, game_id: int, status_code: int = 200) -> Union[InfoResponse, UnauthorizedError]:
        """Deletes the user's game (must be authorized with a token)."""
        resp = self.delete(f"{self.base_url}/user/games/{game_id}", status_code=status_code)
        if status_code == 200 or status_code == 400:
            return InfoResponse(**resp)
        elif status_code == 401:
            return UnauthorizedError(**resp)

    def put_update_dlc_list(self, game_id: int, dlc_list: list, status_code: int = 200) -> Union[InfoResponse, UnauthorizedError]:
        """Updates the game's DLC list (must be authorized with a token)."""
        resp = self.put(f"{self.base_url}/user/games/{game_id}", json=dlc_list, status_code=status_code)
        if status_code == 200 or status_code == 400:
            return InfoResponse(**resp)
        elif status_code == 401:
            return UnauthorizedError(**resp)

    def delete_dlc(self, game_id: int, dlc_list: list, status_code: int = 200) -> Union[InfoResponse, UnauthorizedError]:
        """Deletes the user's game's DLC (must be authorized with a token)."""
        resp = self.delete(f"{self.base_url}/user/games/{game_id}/dlc", json=dlc_list, status_code=status_code)
        if status_code == 200 or status_code == 400:
            return InfoResponse(**resp)
        elif status_code == 401:
            return UnauthorizedError(**resp)

    def put_update_game_field(self, game_id: int, field_data: dict, status_code: int = 200) -> Union[InfoResponse, UnauthorizedError]:
        """Update's the user's game field (must be authorized with a token)."""
        resp = self.put(f"{self.base_url}/user/games/{game_id}/updateField", json=field_data, status_code=status_code)
        if status_code == 200 or status_code == 400:
            return InfoResponse(**resp)
        elif status_code == 401:
            return UnauthorizedError(**resp)

