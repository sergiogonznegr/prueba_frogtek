# Ejercicio 3

"""
Escribe un script en Python que tome como entrada un fichero con una lista con las
siguientes ciudades españolas (Huesca, Frogtek, Jaca, Guadalajara), una por línea. Por
cada una de las ciudades, el script hará dos queries a la API de OpenWeather
(https://openweathermap.org) y guardará en el fichero original los datos que pedimos,
separados por una coma (,):

    ● 1) Usando el nombre de la ciudad, consulta y guarda la temperatura, la velocidad del
    viento y sus coordenadas geográficas (longitud y latitud).
    ● 2) Usando las coordenadas del punto anterior, consulta y guarda la hora del
    amanecer y anochecer y valida que el nombre de la ciudad devuelto por la petición
    usando coordenadas devuelve el mismo nombre de la ciudad del listado.

Si en el punto 1), hay algún tipo de error, se rellenarán los valores con 0 y no se hará la
petición 2).

Por ejemplo, si el listado inicial fuera de dos ciudades de nombre EXISTE y NOEXISTE, el
fichero final quedaría así:

    EXISTE,23.21,2.54,-0.7499,40.560,06:45:12,21:45:12
    NOEXISTE,0,0,0,0
"""

import logging
import os

import cattrs

from ejercicios.ejercicio3.api_connector.open_weather import OpenWeatherClient
from ejercicios.ejercicio3.model_data.cities_data import DataCity, Sun


def convert_path_to_full_path(path: str) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.dirname(current_dir)
    return os.path.join(base_path, current_dir, path)


def get_content_file(file_path: str) -> str:
    """
    Lee el contenido del archivo del que se ha pasado el path por parámetro

    Parameters
    ----------
    file_path: str
        Ruta del archivo

    Return
    ------
    str
        Contenido del archivo
    """
    with open(file=file_path) as file:
        file_content = file.read()

    return file_content


def write_data_in_file(data_to_write: list[list[str]], file_path: str) -> None:
    with open(file_path, "w") as file:
        for info in data_to_write:
            line_to_write = ",".join(info)
            file.write(line_to_write + "\n")


def get_weather_data_by_city_name(openweather_connector: OpenWeatherClient, city: str) -> tuple[DataCity, bool]:
    url = openweather_connector.create_url(city_name=city)
    response = openweather_connector.request_data(url=url)
    if response.status_code == 404:
        not_found_city = cattrs.structure(
            {"coord": {"lon": 0, "lat": 0}, "main": {"temp": 0}, "wind": {"speed": 0}, "name": city}, DataCity
        )
        return not_found_city, False
    city_data = cattrs.structure(response.json(), DataCity)
    return city_data, True


def get_weather_data_by_geolocation_data(
    openweather_connector: OpenWeatherClient, city_name: str, city_data: DataCity
) -> tuple[DataCity, bool]:
    url = openweather_connector.create_url(latitude=city_data.coord.lat, longitude=city_data.coord.lon)
    response = openweather_connector.request_data(url=url)

    json_response = response.json()
    if city_name != json_response["name"]:
        logging.warning(
            f"El nombre devuelto por la api ({json_response["name"]}) con las coordenadas geograficas no coincide con el nombre de ciudad pasado ({city_name})"
        )

    sun_data = cattrs.structure(json_response["sys"], Sun)
    city_data.sun = sun_data

    return city_data, True
