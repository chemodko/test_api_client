import requests


class ApiClient:
    def __init__(self, client_id, client_secret, access_token=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token

    def get_headers(self):
        headers = {
            "Authorization": f"Client-ID {self.client_id}"
        }
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        return headers

    def get(self, url, params=None):
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json()

    def post(self, url, data=None, json=None):
        response = requests.post(url, headers=self.get_headers(), data=data, json=json)
        return response.json()

    def put(self, url, data=None, json=None):
        response = requests.put(url, headers=self.get_headers(), data=data, json=json)
        return response.json()

    def delete(self, url):
        response = requests.delete(url, headers=self.get_headers())
        return response.status_code == 200


if __name__ == "__main__":
    # Пример использования:
    client_id = "client_id"
    client_secret = "client_secret"
    access_token = "access_token"

    api = ApiClient(client_id, client_secret, access_token)

    # Пример запроса GET
    image_hash = "nK9EbaU"
    response = api.get(f"https://api.imgur.com/3/image/{image_hash}")
    print(response)
    print()

    # Пример запроса POST
    data = {"refresh_token": "17746de109a0f5ff17e78d00d629ba40e158ad62",
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "refresh_token"}

    response = api.post("https://api.imgur.com/oauth2/token", data=data)
    print(response)
