import requests
from settings import base_settings


class HttpApiClient:
    def __init__(self, headers: dict = None, token: str = None):
        self.headers = headers or {}
        self.token = token
        self.session = requests.Session()
        self.base_url = base_settings.base_url
        self.login = base_settings.login
        self.password = base_settings.password

    def __log_in(self) -> None:
        """Gets token, logs in to the API and sets the obtained token."""
        log_in_data = {
            "username": self.login,
            "password": self.password
        }
        token_resp = self.post(f"{self.base_url}/login", json=log_in_data, status_code=200)
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



