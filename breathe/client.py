import requests

from .models.employees import Employees
UNAUTHORISED = 400
HTTP_OK = 200
ERROR_TYPES = (
    (405, "Method Not Allowed")
)
class Client:
    def __init__(self, api_key: str, url: str):
        self.url = url
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({'X-API-KEY': self.api_key})
        self.employees = Employees(self)

    def get(self, endpoint: str, data: dict = None, headers: dict = None) -> dict:
        resp = self.session.get(self.url + endpoint, data=data, headers=headers)
        return resp.json()

    def put(self, endpoint: str, data: dict = None, headers: dict = None) -> dict:
        resp = self.session.put(self.url + endpoint, data=data, headers=headers)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp

    def post(self, endpoint: str, data: dict = None, headers: dict = None) -> dict:
        resp = self.session.post(self.url + endpoint, data=data, headers=headers)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp
