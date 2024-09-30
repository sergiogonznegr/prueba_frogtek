from datetime import datetime

import cattrs
import pytest

from ejercicios.ejercicio3.model_data.cities_data import DataCity, Sun


@pytest.fixture
def data_example():
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


def test_data_city_modeling_response(data_example):
    data_city_model = cattrs.structure(data_example, DataCity)
    assert data_city_model.coord.lat == "40.4165"
    assert data_city_model.coord.lon == "-3.7026"
    assert data_city_model.main.temp == "22.12"
    assert data_city_model.name == "Madrid"
    assert data_city_model.wind.speed == "1.54"


def test_sun_data_modeling_response(data_example):
    sun_data_model = cattrs.structure(data_example["sys"], Sun)
    assert sun_data_model.sunrise == datetime(2024, 9, 30, 6, 10, 22)
    assert sun_data_model.sunset == datetime(2024, 9, 30, 17, 58, 52)
