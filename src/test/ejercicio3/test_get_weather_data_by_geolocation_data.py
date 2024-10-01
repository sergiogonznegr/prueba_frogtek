import json
from datetime import datetime

import cattrs
import pytest
import requests
from requests import Response

from ejercicios.ejercicio3.api_connector.open_weather import OpenWeatherClientGeolocationData
from ejercicios.ejercicio3.ejercicio3 import get_weather_data_by_geolocation_data
from ejercicios.ejercicio3.model_data.cities_data import DataCity
from exception.ejercicio3_exceptions import CityNameError


def fake_response():
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


class FakeOpenWeatherClientGeolocationData(OpenWeatherClientGeolocationData):

    def request_data(self, url: str = None) -> Response:
        response = requests.Response()
        response.status_code = 200
        response._content = str.encode(json.dumps(fake_response()))
        return response


@pytest.fixture
def open_weather():
    return FakeOpenWeatherClientGeolocationData()


@pytest.fixture
def data_city():
    return cattrs.structure(fake_response(), DataCity)


def test_get_weather_data_by_geolocation_data(open_weather, data_city):
    city_data = get_weather_data_by_geolocation_data(open_weather, "Madrid", data_city)
    assert isinstance(city_data, DataCity) is True
    assert city_data.sun.sunrise == datetime(2024, 9, 30, 6, 10, 22)
    assert city_data.sun.sunset == datetime(2024, 9, 30, 17, 58, 52)


def test_get_weather_data_by_geolocation_data_not_match_city_name(open_weather, data_city):
    with pytest.raises(CityNameError):
        get_weather_data_by_geolocation_data(
            openweather_connector=open_weather, city_name="Frogtek", city_data=data_city
        )
