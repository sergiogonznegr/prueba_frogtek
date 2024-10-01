import pytest

from ejercicios.ejercicio1.ejercicio1 import get_numbers


def text_string_1():
    return "Frogtek se fundó en 2010 y ahora tiene 40 empleados"


def text_string_2():
    return "Frogtek desarrolla un software para la gestión de tiendas de barrio"


@pytest.mark.parametrize("test_input,expected", [(text_string_1(), ["2010", "40"]), (text_string_2(), [])])
def test_get_numbers(test_input, expected):
    numbers = get_numbers(test_input)
    assert numbers == expected
