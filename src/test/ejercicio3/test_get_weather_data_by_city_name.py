import json

import pytest
import requests
from requests import Response

from ejercicios.ejercicio3.api_connector.open_weather import OpenWeatherClientCityName
from ejercicios.ejercicio3.ejercicio3 import get_weather_data_by_city_name
from ejercicios.ejercicio3.model_data.cities_data import DataCity


def fake_response_200():
    return {
        "coord": {"lon": -3.7026, "lat": 40.4165},
        "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}],
        "base": "stations",
        "main": {
            "temp": 22.12,
            "feels_like": 21.14,
            "temp_min": 18.89,
            "temp_max": 24.04,
            "pressure": 1018,
            "humidity": 29,
            "sea_level": 1018,
            "grnd_level": 944,
        },
        "visibility": 10000,
        "wind": {"speed": 1.54, "deg": 220},
        "clouds": {"all": 0},
        "dt": 1727726101,
        "sys": {"type": 2, "id": 2084029, "country": "ES", "sunrise": 1727676622, "sunset": 1727719132},
        "timezone": 7200,
        "id": 3117735,
        "name": "Madrid",
        "cod": 200,
    }


def fake_response_404():
    return {"cod": "404", "message": "city not found"}


class FakeOpenWeatherClientCityName200(OpenWeatherClientCityName):

    def request_data(self, url: str = None) -> Response:
        response = requests.Response()
        response.status_code = 200
        response._content = str.encode(json.dumps(fake_response_200()))
        return response


class FakeOpenWeatherClientCityName404(OpenWeatherClientCityName):

    def request_data(self, url: str = None) -> Response:
        response = requests.Response()
        response.status_code = 404
        response._content = str.encode(json.dumps(fake_response_404()))
        return response


@pytest.fixture
def open_weather_200():
    return FakeOpenWeatherClientCityName200()


@pytest.fixture
def open_weather_404():
    return FakeOpenWeatherClientCityName404()


def test_get_weather_data_by_city_name_200(open_weather_200):
    city_data, exists_city = get_weather_data_by_city_name(open_weather_200, "Madrid")
    assert isinstance(city_data, DataCity) is True
    assert city_data.coord.lat == "40.4165"
    assert city_data.coord.lon == "-3.7026"
    assert city_data.main.temp == "22.12"
    assert city_data.name == "Madrid"
    assert city_data.wind.speed == "1.54"
    assert exists_city is True


def test_get_weather_data_by_city_name_404(open_weather_404):
    city_data, exists_city = get_weather_data_by_city_name(open_weather_404, "Frogtek")
    assert isinstance(city_data, DataCity)
    assert city_data.coord.lat == "0"
    assert city_data.coord.lon == "0"
    assert city_data.main.temp == "0"
    assert city_data.name == "Frogtek"
    assert city_data.wind.speed == "0"
    assert exists_city is False
