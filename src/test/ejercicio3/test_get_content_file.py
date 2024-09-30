import pytest

from ejercicios.ejercicio3.ejercicio3 import get_content_file


@pytest.fixture
def file_path():
    return "/opt/src/test/ejercicio3/file_to_get_content_file.txt"


def test_get_content_file(file_path):
    path = get_content_file(file_path=file_path)
    assert path == ["hola"]
