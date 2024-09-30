import argparse
import logging


from ejercicios.ejercicio3.api_connector.open_weather import OpenWeatherAuthenticator, OpenWeatherClientCityName, OpenWeatherClientGeolocationData
from ejercicios.ejercicio3.ejercicio3 import convert_path_to_full_path, get_content_file, get_sun_state_by_geolocation_data, get_weather_data_by_city_name, write_data_in_file
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
        raise fnfe

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
        if not exists_city:
            data.append([city, city_data.main.temp, city_data.wind.speed, city_data.coord.lat, city_data.coord.lon])
            continue
        city_data = get_sun_state_by_geolocation_data(
            openweather_connector=openweather_client_geolocation, city_name=city, city_data=city_data
        )
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

    write_data_in_file(data_to_write=data, file_path=full_path)
    logging.info("Los datos fueron escritos en el archivo correctamente")
