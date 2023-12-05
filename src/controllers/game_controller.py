from typing import Union

from src.models.game_controller import *
from src.utils.clients.http_api_client import HttpApiClient


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

    def post_add_game(self, json_data: dict, status_code: int = 201) -> Union[GameAddedResponse, UnauthorizedError]:
        resp = self.post(f"{self.base_url}/user/games", json=json_data, status_code=status_code)
        if status_code == 201 or status_code == 400:
            return GameAddedResponse(**resp)
        elif status_code == 401:
            return UnauthorizedError(**resp)

    def get_game_info(self, game_id: int, status_code: int = 200) -> Union[Game, InfoResponse, UnauthorizedError]:
        resp = self.get(f"{self.base_url}/user/games/{game_id}", status_code=status_code)
        if status_code == 200:
            return Game(**resp)
        elif status_code == 400:
            return InfoResponse(**resp)
        elif status_code == 401:
            return UnauthorizedError(**resp)

    def delete_game(self, game_id: int, status_code: int = 200) -> Union[InfoResponse, UnauthorizedError]:
        resp = self.delete(f"{self.base_url}/user/games/{game_id}", status_code=status_code)
        if status_code == 200 or status_code == 400:
            return InfoResponse(**resp)
        elif status_code == 401:
            return UnauthorizedError(**resp)


