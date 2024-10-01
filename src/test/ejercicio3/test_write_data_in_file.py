import os
import pytest

from ejercicios.ejercicio3.ejercicio3 import write_data_in_file


@pytest.fixture
def file_path():
    return os.path.abspath("test/ejercicio3/tmp/file_to_write_data.txt")


@pytest.fixture
def data_to_write():
    return [["Texto a escribir"]]


def test_write_data_in_file(data_to_write, file_path):
    correct_write = write_data_in_file(data_to_write=data_to_write, file_path=file_path)
    assert correct_write is True
