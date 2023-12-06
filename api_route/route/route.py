import requests


class Route:
    APP_ID = '2750bc42-702e-4cbe-bae5-798f171389e1'
    URL = 'http://core.webstktw.beget.tech/api/v0/apps/'

    def __init__(self):
        self._parameters = {}
        self._response = None

    def set_parameters(self, data: dict):
        self._parameters = data

    def get_parameters(self) -> dict:
        return self._parameters

    def set_response(self, data):
        self._response = data

    def get_response(self):
        return self._response

    def send(self, uri: str, method: str):
        url = self.URL + self.APP_ID + uri
        response = requests.request(url=url, method=method, data=self.get_parameters())
        self.set_response(response)


