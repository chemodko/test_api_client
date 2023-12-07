import allure
from src.models.user_controller import *
from src.http_api_client import HttpApiClient


class UserControllerApiClient(HttpApiClient):
    @allure.step("Creating new user")
    def post_api_signup(self, login: str = None, password: str = None, games: list = None, status_code: int = 201,
                        exp_msg: str = None) -> UserDTOResponse:
        """Registration of a new user in the system."""
        if games is None:
            games = []
        self.login = login
        self.password = password
        json_data = {
            "login": self.login,
            "pass": self.password,
            "games": games
        }
        resp = self.post(f"{self.base_url}/signup", json=json_data, status_code=status_code, exp_msg=exp_msg)
        return UserDTOResponse(**resp)

    @allure.step("Getting user info")
    def get_user_info(self, status_code: int = 200, exp_msg: str = None, model=UserInfoResponse):
        """Getting information about the user (must be authorized with a token)."""
        resp = self.get(f"{self.base_url}/user", status_code=status_code, exp_msg=exp_msg)
        return model(**resp)

    @allure.step("Updating user password")
    def put_user_password(self, new_password: str, status_code: int = 200, exp_msg: str = None, model=InfoResponse):
        """Updating the user's password (must be authorized with a token)."""
        json_data = {"password": new_password}
        resp = self.put(f"{self.base_url}/user", json=json_data, status_code=status_code, exp_msg=exp_msg)
        if status_code == 200:
            self.password = new_password
        return model(**resp)

    @allure.step("Deleting user")
    def delete_user(self, status_code: int = 200, exp_msg: str = None, model=InfoResponse):
        """Deleting a user from the database (must be authorized with a token)."""
        resp = self.delete(f"{self.base_url}/user", status_code=status_code, exp_msg=exp_msg)
        if status_code == 200:
            self.logout()
        return model(**resp)

    @allure.step("Getting all users logins")
    def get_users_info(self, status_code: int = 200) -> UsersInfoResponse:
        """Show logins of all existing users."""
        resp = self.get(f"{self.base_url}/users", status_code=status_code)
        resp_dict = {"info": resp}
        return UsersInfoResponse(**resp_dict)
