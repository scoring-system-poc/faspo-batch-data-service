import pytest
import unittest.mock
import httpx


@pytest.fixture(autouse=True)
async def mock_data_source_service():
    with unittest.mock.patch("src.api.v1.mfcr.data_source") as mock_data_source:
        yield mock_data_source


@pytest.fixture(autouse=True)
async def mock_data_target_service():
    with unittest.mock.patch("src.api.v1.mfcr.data_target") as mock_data_target:
        yield mock_data_target


@pytest.fixture(autouse=True)
async def mock_transformer_service():
    with unittest.mock.patch("src.api.v1.mfcr.transformer") as mock_transformer:
        yield mock_transformer


@pytest.fixture
async def async_client(mock_environ) -> httpx.AsyncClient:
    from main import app

    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        yield client

