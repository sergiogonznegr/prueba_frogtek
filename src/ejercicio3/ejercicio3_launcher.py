
import argparse
import cattrs
import numpy as np
import logging
from ejercicio3 import get_content_file, convert_path_to_full_path
from api_connector.open_weather import OpenWeatherAuthenticator, OpenWeatherClient
from model_data.cities_data import DataCity
from logging_custom.settings import setup_logging


log_level = getattr(logging, "Ejercicio 3", logging.INFO)
setup_logging(log_level)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--file_name", type=str, help="Nombre y extensión del archivo", required=False)
    args = arg_parser.parse_args()

    logging.info(f"La string que se ha pasado es: '{args.file_name}'")
    full_path = convert_path_to_full_path(args.file_name)
    try:
        cities = get_content_file(full_path)
    except FileNotFoundError as fnfe:
        logging.error(f"No se ha encontrado el archivo en la ruta: {args.file_name}")
        raise Exception(fnfe)
    
    logging.info(f"Contenido del archivo: {cities}")

    openweather_client = OpenWeatherClient()
    openweather_auth = OpenWeatherAuthenticator()
    openweather_client.set_api_key(openweather_auth)
    data = []
    for city in cities:
        url = openweather_client.create_url(city_name=city)
        response = openweather_client.request_url(url=url)
        if response.status_code == 404:
            data.append([city, 0, 0, 0])
            continue
        city_data = cattrs.structure(response.json(), DataCity)
        data.append([city, city_data.main.temp, city_data.wind.speed, city_data.coord.lat, city_data.coord.lon])

    logging.info(f"Los datos que se van a insertar en el archivo son: {data}")

