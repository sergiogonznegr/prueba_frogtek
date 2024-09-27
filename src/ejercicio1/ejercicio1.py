# Ejercicio 1

"""
Escribe un script que sume todos los números de una cadena de texto pasada por
parámetros.
Ejemplos:
● "Frogtek se fundó en 2010 y ahora tiene 40 empleados", devolvería "2050"
● "Frogtek desarrolla un software para la gestión de tiendas de barrio", devolvería "0"
"""

import re


def get_numbers(text_string: str) -> list[str]:
    """
    Recoge los números que haya dentro de la string pasada por parámetro

    Parameters
    ----------
    string: str
        Cadena de texto de la que sacar los números
    
    Returns
    -------
    int
        Suma de los números encontrados
    """
    return re.findall('\\d+', text_string)


def sum_numbers(numbers_list: list[str]) -> int:
    """
    Suma los números que hay en la lista pasada por parámetro

    Parameters
    ----------
    numbers_list: list[str]
        Listado con los números que se extrajeron de la cadena de texto

    Return
    ------
    int
        Suma de los números
    """
    if not isinstance(numbers_list, list):
        raise Exception()
    
    return sum(map(int, numbers_list))
