# Ejercicio 2

"""
Escribe un script que borre los ceros por la izquierda de una dirección IP pasada por
parámetros.

Por ejemplo: "210.010.090.180", devolvería "210.10.90.180"
"""

import re

def is_correct_ip_format(ip: str) -> bool:
    """
    Comprueba que la IP que se pasa por parámetro tiene el formato correcto

    Parameters
    ----------
    ip: str
        IP a comprobar

    Return
    ------
    bool
        - True: El formato es correcto
        - False: El formato es incorrecto
    """
    return True if re.match('^([0-9]{1,3}\.){3}([0-9]{1,3}){1}$', ip) else False


def split_ip(ip: str) -> list[str]:
    """
    Separa la ip mediante los puntos

    Parameters
    ----------
    ip: str
        IP a separar

    Return
    ------
    list[str]
        Listado de string con cada uno de los elementos de la ip
    """
    return ip.split(".")


def delete_zeros(splitted_ip: list[str]) -> list[str]:
    """
    Elimina los ceros que estén a la izquierda de los elementos de la IP

    Parameters
    ----------
    splitted_ip: list[str]
        Listado con cada uno de los elementos de la IP
    
    Return
    ------
    str
        NUeva IP sin los 0 a la izquierda
    """
    return [str(int(ip_element)) for ip_element in splitted_ip]


def make_new_ip(elements_ip: list[str]) -> str:
    """
    Junta los elementos de separados sin los 0

    Parameters
    ----------
    elements_ip: list[str]
        Listado de los 
    """
    return ".".join(elements_ip)
