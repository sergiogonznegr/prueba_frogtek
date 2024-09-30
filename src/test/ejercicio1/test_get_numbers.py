import pytest

from ejercicios.ejercicio1.ejercicio1 import get_numbers


@pytest.fixture
def text_string():
    return "Frogtek se fundó en 2010 y ahora tiene 40 empleados"


def test_get_numbers(text_string):
    numbers = get_numbers(text_string)
    assert numbers == ["2010", "40"]
