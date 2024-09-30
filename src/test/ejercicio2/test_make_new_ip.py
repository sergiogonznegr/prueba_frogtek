import pytest

from ejercicios.ejercicio2.ejercicio2 import make_new_ip


@pytest.fixture
def splitted_ip():
    return ["123", "90", "76", "12"]


def test_make_new_ip(splitted_ip):
    ip_splitted_without_zeros = make_new_ip(splitted_ip)
    assert ip_splitted_without_zeros == "123.90.76.12"
