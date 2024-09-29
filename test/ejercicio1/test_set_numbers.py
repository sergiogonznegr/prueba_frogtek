import pytest

from ejercicio1.ejercicio1 import set_numbers


@pytest.fixture
def numbers_list() -> str:
    return ["2010", "40"]


@pytest.fixture
def number() -> str:
    return "2010"


def test_sum_numbers_works_properly(numbers_list):
    numbers = set_numbers(numbers_list)
    assert numbers == 2050


def test_sum_numbers_raise_exception(number):
    with pytest.raises(Exception):
        set_numbers(number)
