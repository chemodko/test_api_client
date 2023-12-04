from src.models.user_controller import *
from src.utils.clients.http_api_client import HttpApiClient


class UserControllerApiClient(HttpApiClient):
    # Регистрация нового пользователя
    def post_new_user(self, login: str = None, password: str = None) -> UserDTOResponse:
        if login and password:
            self.login = login
            self.password = password
        json_data = {
            "login": self.login,
            "pass": self.password
        }
        resp = self.post(f"{self.base_url}/signup", json=json_data, status_code=201)
        return UserDTOResponse(**resp)

    # Получение информации о пользователе (должен быть авторизован с помощью токена)
    def get_user_info(self) -> UserInfoResponse:
        resp = self.get(f"{self.base_url}/user", status_code=200)
        return UserInfoResponse(**resp)

    # Обновление пароля у пользователя (должен быть авторизован с помощью токена)
    def put_user_password(self, new_password: str) -> UserNewPasswordResponse:
        json_data = {
            "password": new_password
        }
        resp = self.put(f"{self.base_url}/user", json=json_data, status_code=200)
        self.password = new_password
        return UserNewPasswordResponse(**resp)

    # Удаление пользователя из базы данных (должен быть авторизован с помощью токена)
    def delete_user(self) -> UserDeleteInfoResponse:
        resp = self.delete(f"{self.base_url}/user", status_code=200)
        return UserDeleteInfoResponse(**resp)

    # Показать логины всех существующих пользователей
    def get_users_info(self) -> UsersInfoResponse:
        resp = self.get(f"{self.base_url}/users", status_code=200)
        resp_dict = {"response": resp}
        return UsersInfoResponse(**resp_dict)
