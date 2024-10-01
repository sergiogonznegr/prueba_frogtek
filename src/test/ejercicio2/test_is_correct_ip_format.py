import pytest

from ejercicios.ejercicio2.ejercicio2 import is_correct_ip_format


@pytest.fixture
def ip_correct():
    return "210.10.90.180"


@pytest.fixture
def ip_incorrect():
    return "1111.1111.1111.1111"


def test_is_correct_ip_format_correct(ip_correct):
    is_correct = is_correct_ip_format(ip_correct)
    assert is_correct is True


def test_is_correct_ip_format_incorrect(ip_incorrect):
    is_correct = is_correct_ip_format(ip_incorrect)
    assert is_correct is False
