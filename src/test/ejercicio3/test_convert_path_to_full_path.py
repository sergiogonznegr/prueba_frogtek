import pytest

from ejercicios.ejercicio3.ejercicio3 import convert_path_to_full_path


@pytest.fixture
def partial_path():
    return "test/test.test"


def test_partial_path_to_full_path(partial_path):
    path = convert_path_to_full_path(path=partial_path)
    assert path == "/opt/src/ejercicios/ejercicio3/test/test.test"
