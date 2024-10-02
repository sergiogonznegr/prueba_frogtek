import argparse
import logging
import sys

from ejercicios.ejercicio3.api_connector.open_weather import (
    OpenWeatherAuthenticator,
    OpenWeatherClientCityName,
    OpenWeatherClientGeolocationData,
)
from ejercicios.ejercicio3.ejercicio3 import (
    clean_data_file,
    convert_path_to_full_path,
    get_cities_list,
    get_content_file,
    get_weather_data_by_city_name,
    get_weather_data_by_geolocation_data,
    write_data_in_file,
)
from exception.ejercicio3_exceptions import CityNameError
from logging_custom.settings import setup_logging

log_level = getattr(logging, "Ejercicio 3", logging.INFO)
setup_logging(log_level)


FILE = 'ciudades_openweather.txt'


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--file_path", type=str, help="Ruta dónde se encuentra el archivo. Nombre del archivo incluido", required=False
    )
    args = arg_parser.parse_args()

    full_path = args.file_path if args.file_path else convert_path_to_full_path(FILE)
    if not args.file_path:
        clean_data_file(file_path=full_path)

    logging.info(f"Se van a recoger los datos del archivo: {full_path}")

    try:
        file_cities = get_content_file(full_path)
        logging.info(f"El contenido sin transformar del archivo es: {file_cities}")
    except FileNotFoundError:
        logging.error(f"No se ha encontrado el archivo en la ruta: {full_path}")
        sys.exit(1)

    cities = get_cities_list(cities=file_cities)
    logging.info(f"Contenido del archivo: {cities}")

    openweather_client_city_name = OpenWeatherClientCityName()
    openweather_client_geolocation = OpenWeatherClientGeolocationData()
    openweather_auth = OpenWeatherAuthenticator()
    openweather_client_city_name.set_api_key(openweather_auth)
    openweather_client_geolocation.set_api_key(openweather_auth)
    data = []
    for city in cities:
        city_data, exists_city = get_weather_data_by_city_name(
            openweather_connector=openweather_client_city_name, city=city
        )
        logging.info(f"Datos de la ciudad: {city_data}")

        if not exists_city:
            data.append([city, city_data.main.temp, city_data.wind.speed, city_data.coord.lat, city_data.coord.lon])
            logging.warning(f"La ciudad {city} no existe o no tiene registros en la API")
            continue

        try:
            city_data = get_weather_data_by_geolocation_data(
                openweather_connector=openweather_client_geolocation, city_name=city, city_data=city_data
            )
        except CityNameError:
            logging.error(
                f"La ciudad recogida con las coordenadas: '{city_data.coord.lat}' '{city_data.coord.lon}' para la ciudad: {city_data.name} con la ciudad del archivo: {city}"
            )
            continue
        except KeyError as ke:
            logging.error(
                f"No se ha encontrado la key: {ke} en la respuesta, es posible que la petición haya salido mal"
            )
            continue

        data.append(
            [
                city,
                city_data.main.temp,
                city_data.wind.speed,
                city_data.coord.lat,
                city_data.coord.lon,
                city_data.sun.sunrise.strftime("%H:%M:%S"),
                city_data.sun.sunset.strftime("%H:%M:%S"),
            ]
        )

    if data:
        write_data_in_file(data_to_write=data, file_path=full_path)
        logging.info("Los datos fueron escritos en el archivo correctamente")

    data = get_content_file(file_path=full_path)
    logging.info(
        f"El contenido final del archivo es:\n\n{data}",
    )
