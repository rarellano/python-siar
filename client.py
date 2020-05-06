import requests
from decorators import siar_exceptions, response_json

API_URL = "https://servicio.mapama.gob.es/apisiar/API/v1/"


class SiarClient(object):
    def __init__(self, api_key, json=False):
        super().__init__()
        self.api_key = api_key
        self.json = json

    @response_json
    @siar_exceptions
    def info_ccaa(self):
        response = requests.get(f"{API_URL}info/ccaa?ClaveAPI={self.api_key}",)
        return response if not self.json else response

    @response_json
    @siar_exceptions
    def info_access(self):
        response = requests.get(f"{API_URL}info/accesos?ClaveAPI={self.api_key}",)
        return response if not self.json else response

    @response_json
    @siar_exceptions
    def info_provincies(self):
        response = requests.get(f"{API_URL}info/provincias?ClaveAPI={self.api_key}",)
        return response if not self.json else response

    @response_json
    @siar_exceptions
    def info_stations(self):
        response = requests.get(f"{API_URL}info/estaciones?ClaveAPI={self.api_key}",)
        return response if not self.json else response

    @response_json
    @siar_exceptions
    def test_bad_request(self):
        response = requests.get(f"{API_URL}info/test?ClaveAPI={self.api_key}",)
        return response if not self.json else response

    @response_json
    @siar_exceptions
    def data_by_hours(self, area=None, province=None, station=None):
        response = requests.get(f"{API_URL}datos/horarios?ClaveAPI={self.api_key}",)
        return response if not self.json else response
