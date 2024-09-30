import logging
import os

import cattrs
from api_connector.open_weather import OpenWeatherClient
from model_data.cities_data import DataCity, Sun


def convert_path_to_full_path(path: str) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.dirname(current_dir)
    return os.path.join(base_path, path)


def get_content_file(file_path: str) -> list[str]:
    """
    Lee el contenido del archivo del que se ha pasado el path por parámetro

    Parameters
    ----------
    file_path: str
        Ruta del archivo

    Return
    ------
    list[str]
        Listado con el nombre de las ciudades
    """
    with open(file=file_path) as file:
        file_content = file.read()

    return file_content.split(",\n")


def write_data_in_file(data_to_write: list[list[str]], file_path: str) -> None:
    with open(file_path, "w") as file:
        for info in data_to_write:
            line_to_write = ",".join(info)
            file.write(line_to_write + "\n")


def get_weather_data_by_city_name(openweather_connector: OpenWeatherClient, city: str) -> tuple[DataCity, bool]:
    url = openweather_connector.create_url(city_name=city)
    response = openweather_connector.request_url(url=url)
    if response.status_code == 404:
        not_found_city = cattrs.structure(
            {"coord": {"lon": 0, "lat": 0}, "main": {"temp": 0}, "wind": {"speed": 0}, "name": "Guadalajara"}, DataCity
        )
        return not_found_city, False
    city_data = cattrs.structure(response.json(), DataCity)
    return city_data, True


def get_sun_state_by_geolocation_data(
    openweather_connector: OpenWeatherClient, city_name: str, city_data: DataCity
) -> DataCity:
    url = openweather_connector.create_url(latitude=city_data.coord.lat, longitude=city_data.coord.lon)
    response = openweather_connector.request_url(url=url)

    json_response = response.json()
    if city_name != json_response["name"]:
        logging.error(
            "El nombre devuelto por la api con las coordenadas geograficas no coincide con el nombre de ciudad pasado"
        )

    sun_data = cattrs.structure(json_response["sys"], Sun)
    city_data.sun = sun_data

    return city_data
