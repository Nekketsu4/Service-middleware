import requests


class Route:
    APP_ID = '2750bc42-702e-4cbe-bae5-798f171389e1'

    def __init__(self):
        self._parameters = []
        self._response = []

    def set_parameters(self, data: dict):
        self._parameters = data

    def get_parameters(self) -> list:
        return self._parameters

    def set_response(self, data):
        self._response = data

    def get_response(self) -> list:
        return self._response

    def send(self, uri: str, method='GET'):
        url = 'http://core.webstktw.beget.tech/api/v0/apps/' + self.APP_ID + uri
        response = requests.request(url=url, method=method, data=self._parameters)
        self.set_response(response.json())
