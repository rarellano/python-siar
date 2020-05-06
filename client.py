import requests
from decorators import siar_exceptions, response_json
from enum import Enum

API_URL = "https://servicio.mapama.gob.es/apisiar/API/v1/"


class SiarClient(object):
    class FrecuencyType(Enum):
        hourly = "horarios"
        daily = "diarios"
        weekly = "semanales"
        monthly = "mensuales"

    class DataType(Enum):
        ccaa = "ccaa"
        provincies = "provincia"
        stations = "estacion"

    def __init__(self, api_key, json=False, exceptions=True):
        super().__init__()
        self.api_key = api_key
        self.json = json
        self.exceptions = exceptions

    @response_json
    @siar_exceptions
    def info_ccaa(self):
        return requests.get(f"{API_URL}info/ccaa?ClaveAPI={self.api_key}",)

    @response_json
    @siar_exceptions
    def info_access(self):
        return requests.get(f"{API_URL}info/accesos?ClaveAPI={self.api_key}",)

    @response_json
    @siar_exceptions
    def info_provincies(self):
        return requests.get(f"{API_URL}info/provincias?ClaveAPI={self.api_key}",)

    @response_json
    @siar_exceptions
    def info_stations(self):
        return requests.get(f"{API_URL}info/estaciones?ClaveAPI={self.api_key}",)

    @response_json
    @siar_exceptions
    def test_bad_request(self):
        return requests.get(f"{API_URL}info/test?ClaveAPI={self.api_key}",)

    def __data_by_type(self, frequency_type, data_type, ids, start_date, end_date=None):
        if not end_date:
            end_date = start_date

        query_ids = f'&id={"&id=".join(ids)}'

        url = f"{API_URL}datos/{frequency_type}/{data_type}?ClaveAPI={self.api_key}\
                {query_ids}&fechainicial={start_date}&fechafinal={end_date}"
        return requests.get(url)

    @response_json
    @siar_exceptions
    def data_ccaa_by_hours(self, ids, start_date, end_date=None):
        response = self.__data_by_type(
            self.FrecuencyType.hourly.value,
            self.DataType.ccaa.value,
            ids,
            start_date,
            end_date=None,
        )
        return response

    @response_json
    @siar_exceptions
    def data_ccaa_by_day(self, ids, start_date, end_date=None):
        response = self.__data_by_type(
            self.FrecuencyType.daily.value,
            self.DataType.ccaa.value,
            ids,
            start_date,
            end_date=None,
        )
        return response

    @response_json
    @siar_exceptions
    def data_ccaa_by_week(self, ids, start_date, end_date=None):
        response = self.__data_by_type(
            self.FrecuencyType.weekly.value,
            self.DataType.ccaa.value,
            ids,
            start_date,
            end_date=None,
        )
        return response

    @response_json
    @siar_exceptions
    def data_ccaa_by_month(self, ids, start_date, end_date=None):
        response = self.__data_by_type(
            self.FrecuencyType.monthly.value,
            self.DataType.ccaa.value,
            ids,
            start_date,
            end_date=None,
        )
        return response

    @response_json
    @siar_exceptions
    def data_provincies_by_hours(self, ids, start_date, end_date=None):
        response = self.__data_by_type(
            self.FrecuencyType.hourly.value,
            self.DataType.provincies.value,
            ids,
            start_date,
            end_date=None,
        )
        return response

    @response_json
    @siar_exceptions
    def data_provincies_by_day(self, ids, start_date, end_date=None):
        response = self.__data_by_type(
            self.FrecuencyType.daily.value,
            self.DataType.provincies.value,
            ids,
            start_date,
            end_date=None,
        )
        return response

    @response_json
    @siar_exceptions
    def data_provincies_by_week(self, ids, start_date, end_date=None):
        response = self.__data_by_type(
            self.FrecuencyType.weekly.value,
            self.DataType.provincies.value,
            ids,
            start_date,
            end_date=None,
        )
        return response

    @response_json
    @siar_exceptions
    def data_provincies_by_month(self, ids, start_date, end_date=None):
        response = self.__data_by_type(
            self.FrecuencyType.monthly.value,
            self.DataType.provincies.value,
            ids,
            start_date,
            end_date=None,
        )
        return response

    @response_json
    @siar_exceptions
    def data_ccaa_by_month(self, ids, start_date, end_date=None):
        response = self.__data_by_type(
            self.FrecuencyType.monthly.value,
            self.DataType.ccaa.value,
            ids,
            start_date,
            end_date=None,
        )
        return response

    @response_json
    @siar_exceptions
    def data_stations_by_hours(self, ids, start_date, end_date=None):
        response = self.__data_by_type(
            self.FrecuencyType.hourly.value,
            self.DataType.stations.value,
            ids,
            start_date,
            end_date=None,
        )
        return response

    @response_json
    @siar_exceptions
    def data_stations_by_day(self, ids, start_date, end_date=None):
        response = self.__data_by_type(
            self.FrecuencyType.daily.value,
            self.DataType.stations.value,
            ids,
            start_date,
            end_date=None,
        )
        return response

    @response_json
    @siar_exceptions
    def data_stations_by_week(self, ids, start_date, end_date=None):
        response = self.__data_by_type(
            self.FrecuencyType.weekly.value,
            self.DataType.stations.value,
            ids,
            start_date,
            end_date=None,
        )
        return response

    @response_json
    @siar_exceptions
    def data_stations_by_month(self, ids, start_date, end_date=None):
        response = self.__data_by_type(
            self.FrecuencyType.monthly.value,
            self.DataType.stations.value,
            ids,
            start_date,
            end_date=None,
        )
        return response
