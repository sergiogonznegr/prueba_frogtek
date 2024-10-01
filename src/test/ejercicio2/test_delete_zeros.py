import pytest

from ejercicios.ejercicio2.ejercicio2 import delete_zeros


@pytest.fixture
def splitted_ip():
    return ["123", "090", "076", "12"]


def test_delete_zeros(splitted_ip):
    ip_splitted_without_zeros = delete_zeros(splitted_ip)
    assert ip_splitted_without_zeros == ["123", "90", "76", "12"]
