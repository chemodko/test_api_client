import requests
from settings import Settings


class ApiClient:
    def __init__(self, settings: Settings, headers: dict = None, token: str = None):
        self.settings = settings
        self.headers = headers or {}
        self.token = token
        self.session = requests.Session()

    def __log_in(self) -> None:
        """Gets token, logs in to the API and sets the obtained token."""
        log_in_data = {
            "username": self.settings.login,
            "password": self.settings.password
        }
        token_resp = self.post(f"{self.settings.base_url}/login", json=log_in_data, status_code=200)
        self.set_token(token_resp["token"])

    def auth(self) -> None:
        """Calls log_in method and sets the authorization headers."""
        self.__log_in()
        self.headers["Authorization"] = f"Bearer {self.token}"

    def __base_call(self, method: str, url: str, params: dict = None, data: dict = None, json: dict = None, status_code: int = 200) -> dict:
        """
        Makes an HTTP request using the provided method, url, and parameters.

        Args:
        method (str): The HTTP method to use.
        url (str): The URL for the request.
        params (dict, optional): The URL parameters for the request. Defaults to None.
        data (dict, optional): The body data for requests. Defaults to None.
        json (dict, optional): The JSON body for requests. Defaults to None.
        status_code (int, optional): The expected status code for the response. Defaults to 200.

        Returns:
        dict: The JSON response from the request.

        Raises:
        AssertionError: If the response status code is not the expected status_code.
        """
        resp = self.session.request(method, url, headers=self.headers, params=params, data=data, json=json)
        assert resp.status_code == status_code, f"Status code: {resp.status_code}"
        return resp.json()

    def set_token(self, token: str) -> None:
        """Sets the authentication token."""
        self.token = token

    def get_token(self) -> str:
        """Gets the authentication token."""
        return self.token

    def get(self, url: str, params: dict = None, status_code: int = 200) -> dict:
        """Makes a GET request."""
        return self.__base_call("get", url, params=params, status_code=status_code)

    def post(self, url: str, data: dict = None, json: dict = None, status_code: int = 201) -> dict:
        """Makes a POST request."""
        return self.__base_call("post", url, data=data, json=json, status_code=status_code)

    def put(self, url: str, data: dict = None, json: dict = None, status_code: int = 200) -> dict:
        """Makes a PUT request."""
        return self.__base_call("put", url, data=data, json=json, status_code=status_code)

    def delete(self, url: str, data: dict = None, json: dict = None, status_code: int = 200) -> dict:
        """Makes a DELETE request."""
        return self.__base_call("delete", url, data=data, json=json, status_code=status_code)


if __name__ == "__main__":
    login = "chemodko"
    password = "password"
    base_url = "http://85.192.34.140:8080/api"
    settings = Settings(login=login, password=password, base_url=base_url)
    api = ApiClient(settings=settings)

    # Регистрация нового пользователя
    json_data = {
        "login": api.settings.login,
        "pass": api.settings.password
    }
    resp = api.post(f"{base_url}/signup", json=json_data, status_code=201)
    print("User registration:\n", resp)

    # Авторизация
    api.auth()

    # Получение информации о пользователе
    user_info_resp = api.get(f"{base_url}/user", status_code=200)
    print("User info:\n", user_info_resp)

    # Показать всех существующих пользователей (10)
    users_info_resp = api.get(f"{base_url}/users", status_code=200)
    print("Users info:\n", users_info_resp[:10])

    # Удаление пользователя
    delete_user_resp = api.delete(f"{base_url}/user", status_code=200)
    print("User deletion:\n", delete_user_resp)



