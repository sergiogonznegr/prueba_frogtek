import pytest

from ejercicios.ejercicio2.ejercicio2 import ip_has_left_zeros


@pytest.mark.parametrize("ip,expected", (["01.100.12.23", True], ["10.000000100.012.023", True], ["1.100.00012.023", True], ["01.0100.012.023", True]))
def test_ip_has_left_zeros(ip, expected):
    has_left_zeros = ip_has_left_zeros(ip)
    assert has_left_zeros is expected


@pytest.mark.parametrize("ip,expected", (["1.100.12.23", False], ["127.0.0.1", False], ["190.123.34.6", False], ["10129393.24534.24534.346", False]))
def test_ip_has_not_left_zeros(ip, expected):
    has_not_left_zeros = ip_has_left_zeros(ip)
    assert has_not_left_zeros is expected
