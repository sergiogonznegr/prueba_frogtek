import os

import pytest

from ejercicios.ejercicio3.ejercicio3 import convert_path_to_full_path


@pytest.fixture
def choose_env():
    env = os.getenv("GITHUB_ACTIONS")
    if env:
        return "/home/runner/work/prueba_frogtek/prueba_frogtek/src/ejercicios/ejercicio3/test/test.test"
    else:
        return "/opt/src/ejercicios/ejercicio3/test/test.test"


@pytest.fixture
def partial_path():
    return "test/test.test"


def test_partial_path_to_full_path(partial_path, choose_env):
    path = convert_path_to_full_path(path=partial_path)
    assert path == choose_env
