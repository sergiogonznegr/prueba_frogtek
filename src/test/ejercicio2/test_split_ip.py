import pytest

from ejercicios.ejercicio2.ejercicio2 import split_ip


@pytest.fixture
def ip():
    return "201.31.24.90"


def test_split_ip(ip):
    ip_splitted = split_ip(ip=ip)
    assert ip_splitted == ["201", "31", "24", "90"]
