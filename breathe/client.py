import requests

from breathe.exceptions import IncorrectlyConfigured, ConnectionError
from breathe.models.employees import Employee

PROD_URL = "https://api.breathehr.info:443/v1/"
SANDBOX_URL = "https://api.sandbox.breathehr.info:443/v1/"


class Client:
    def __init__(self, api_key: str, mode: str = "production"):
        if mode != "production" and mode != "sandbox":
            raise IncorrectlyConfigured("Mode must be one of: production or sandbox")
        if len(api_key) < 48:
            raise IncorrectlyConfigured("Incorrect API key provided")
        self.url = PROD_URL
        if mode == "sandbox":
            self.url = SANDBOX_URL
        self.api_key = api_key

        self.session = requests.Session()
        self.session.headers.update({'X-API-KEY': self.api_key})
        self.employees = Employee(self)
        self._test_connect()

    def _test_connect(self):
        resp = self.request("GET", "divisions")
        if resp.status_code != requests.codes.ok:
            raise ConnectionError(resp.json())

    def request(self, method, endpoint: str, data: dict = None, headers: dict = None, json: dict = None) -> requests.Response:
        return self.session.request(method, self.url + endpoint, data=data, headers=headers, json=json)

