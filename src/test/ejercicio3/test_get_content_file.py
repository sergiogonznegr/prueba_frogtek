import os
import pytest

from ejercicios.ejercicio3.ejercicio3 import get_content_file


@pytest.fixture
def file_path():
    return os.path.abspath("test/ejercicio3/tmp/file_to_get_content_file.txt")


def test_get_content_file(file_path):
    path = get_content_file(file_path=file_path)
    assert path == "hola"
