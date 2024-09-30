
import pytest
from ejercicios.ejercicio3.api_connector.open_weather import OpenWeatherAuthenticator, OpenWeatherClientCityName, OpenWeatherClientGeolocationData


OpenWeatherClientGeolocationData


@pytest.fixture
def authenticator():
    return OpenWeatherAuthenticator()


def test_open_weather_by_city_name():
    openweather_client = OpenWeatherClientCityName()
    assert isinstance(openweather_client, OpenWeatherClientCityName)


def test_open_weather_by_city_name_set_authenticator(authenticator):
    openweather_client = OpenWeatherClientCityName()
    openweather_client.set_api_key(authenticator)
    assert openweather_client._api_key == "2b2c54bd4f822b146e23fc28a5e1c1e6"
