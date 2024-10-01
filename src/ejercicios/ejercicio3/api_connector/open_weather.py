from abc import ABC, abstractmethod

import requests

from ejercicios.ejercicio3.model_data.cities_data import DataCity


class OpenWeatherAuthenticator:
    _API_KEY = "2b2c54bd4f822b146e23fc28a5e1c1e6"

    @property
    def api_key(self) -> str:
        """
        Retorna el valor de la api key

        Return
        ------
        str
            Valor de la API KEY
        """
        return self._API_KEY


class OpenWeatherClient(ABC):
    _BASE_URL = "https://api.openweathermap.org/"

    def __init__(self) -> None:
        self._api_key = None
        self._url = None

    def set_api_key(self, api_key_authenticator: OpenWeatherAuthenticator):
        self._api_key = api_key_authenticator.api_key

    @abstractmethod
    def create_url(self, *args, **kwargs) -> str:
        raise NotImplementedError()

    @abstractmethod
    def request_data(self, *args, **kwargs) -> requests.Response:
        raise NotImplementedError()


class OpenWeatherClientCityName(OpenWeatherClient):
    _URL_DATA_BY_CITY = "data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    def create_url(self, city_name: str) -> str:
        self._url = self._BASE_URL + self._URL_DATA_BY_CITY
        self._url = self._url.format(city_name=city_name, api_key=self._api_key)
        return self._url

    def request_data(self, url: str = None) -> requests.Response:
        url_to_request = url or self._url
        response = requests.get(url=url_to_request)
        return response


class OpenWeatherClientGeolocationData(OpenWeatherClient):
    _URL_DATA_BY_GEOLOCATION_DATA = "data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"

    def create_url(self, latitude: float, longitude: float) -> str:
        self._url = self._BASE_URL + self._URL_DATA_BY_GEOLOCATION_DATA
        self._url = self._url.format(latitude=latitude, longitude=longitude, api_key=self._api_key)
        return self._url

    def request_data(self, url: str = None) -> requests.Response:
        url_to_request = url or self._url
        response = requests.get(url=url_to_request)
        return response
