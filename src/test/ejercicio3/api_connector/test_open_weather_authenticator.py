from ejercicios.ejercicio3.api_connector.open_weather import OpenWeatherAuthenticator


def test_authenticator():
    authenticator = OpenWeatherAuthenticator()
    assert authenticator.api_key == "2b2c54bd4f822b146e23fc28a5e1c1e6"
