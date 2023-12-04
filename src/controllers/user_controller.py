from src.models.user_controller import *
from src.utils.clients.http_api_client import HttpApiClient


class UserControllerApiClient(HttpApiClient):
    def post_new_user(self, login: str = None, password: str = None, status_code: int = 201) -> UserDTOResponse:
        """Registration of a new user in the system."""
        self.login = login
        self.password = password
        json_data = {
            "login": self.login,
            "pass": self.password
        }
        resp = self.post(f"{self.base_url}/signup", json=json_data, status_code=status_code)
        return UserDTOResponse(**resp)

    def get_user_info(self, status_code: int = 200) -> UserInfoResponse:
        """Getting information about the user (must be authorized with a token)."""
        resp = self.get(f"{self.base_url}/user", status_code=status_code)
        return UserInfoResponse(**resp)

    def put_user_password(self, new_password: str, status_code: int = 200) -> UserNewPasswordResponse:
        """Updating the user's password (must be authorized with a token)."""
        json_data = {
            "password": new_password
        }
        if status_code == 200:
            self.password = new_password
        resp = self.put(f"{self.base_url}/user", json=json_data, status_code=status_code)
        return UserNewPasswordResponse(**resp)

    def delete_user(self, status_code: int = 200) -> UserDeleteInfoResponse:
        """Deleting a user from the database (must be authorized with a token)."""
        resp = self.delete(f"{self.base_url}/user", status_code=status_code)
        if status_code == 200:
            self.headers = None
        return UserDeleteInfoResponse(**resp)

    def get_users_info(self, status_code: int = 200) -> UsersInfoResponse:
        """Show logins of all existing users."""
        resp = self.get(f"{self.base_url}/users", status_code=status_code)
        resp_dict = {"info": resp}
        return UsersInfoResponse(**resp_dict)
