import pytest

from ejercicios.ejercicio3.api_connector.open_weather import (
    OpenWeatherAuthenticator,
    OpenWeatherClientCityName,
    OpenWeatherClientGeolocationData,
)

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


def test_open_weather_by_city_name_create_url(authenticator):
    openweather_client = OpenWeatherClientCityName()
    openweather_client.set_api_key(authenticator)
    url = openweather_client.create_url(city_name="Toledo")
    assert (
        url
        == "https://api.openweathermap.org/data/2.5/weather?q=Toledo&appid=2b2c54bd4f822b146e23fc28a5e1c1e6&units=metric&lang=sp"
    )


@pytest.mark.vcr
def test_open_weather_by_city_name_request_data(authenticator):
    openweather_client = OpenWeatherClientCityName()
    openweather_client.set_api_key(authenticator)
    response = openweather_client.request_data(
        url="https://api.openweathermap.org/data/2.5/weather?q=Toledo&appid=2b2c54bd4f822b146e23fc28a5e1c1e6&units=metric&lang=sp"
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Toledo"


def test_open_weather_by_geolocation_data():
    openweather_client = OpenWeatherClientGeolocationData()
    assert isinstance(openweather_client, OpenWeatherClientGeolocationData)


def test_open_weather_by_geolocation_data_set_authenticator(authenticator):
    openweather_client = OpenWeatherClientGeolocationData()
    openweather_client.set_api_key(authenticator)
    assert openweather_client._api_key == "2b2c54bd4f822b146e23fc28a5e1c1e6"


def test_open_weather_by_geolocation_data_create_url(authenticator):
    openweather_client = OpenWeatherClientGeolocationData()
    openweather_client.set_api_key(authenticator)
    url = openweather_client.create_url(latitude=39.8333, longitude=-4)
    assert (
        url
        == "https://api.openweathermap.org/data/2.5/weather?lat=39.8333&lon=-4&appid=2b2c54bd4f822b146e23fc28a5e1c1e6&units=metric&lang=sp"
    )


@pytest.mark.vcr
def test_open_weather_by_geolocation_data_request_data(authenticator):
    openweather_client = OpenWeatherClientGeolocationData()
    openweather_client.set_api_key(authenticator)
    response = openweather_client.request_data(
        url="https://api.openweathermap.org/data/2.5/weather?lat=39.8333&lon=-4&appid=2b2c54bd4f822b146e23fc28a5e1c1e6&units=metric&lang=sp"
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Toledo"
