import pytest
import unittest.mock

import os


@pytest.fixture(autouse=True)
def mock_environ(monkeypatch) -> None:
    with unittest.mock.patch.dict(os.environ, clear=True):
        env = {
            "DATA_TARGET_URL": "http://localhost:8080/api/v1/data_target",
        }
        for key, value in env.items():
            monkeypatch.setenv(key, value)
        yield


