import os


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


def get_weather_data_by_city_name(city_name: str) -> dict[str, str]:
    pass


def get_sun_state_by_geolocation_data() -> dict[str, str]:
    pass