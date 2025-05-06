import pytest
import unittest.mock
import httpx


@pytest.mark.asyncio
async def test__process(mock_data_source_service, mock_data_target_service, mock_transformer_service) -> None:
    mock_data_source_service.get_data.side_effect = unittest.mock.AsyncMock(return_value=b"<response>...</response>")
    mock_transformer_service.extract_data_from_mfcr_batch_file.return_value = [{"id": "item1"}, {"id": "item2"}]
    mock_data_target_service.post_data.side_effect = unittest.mock.AsyncMock(side_effect=lambda x, *_: x["id"])

    doc_type = "001"
    year = "1970"
    month = "01"
    correlation_id = "test_correlation_id"

    from src.api.v1.mfcr import _process
    result = await _process(doc_type, year, month, correlation_id)

    assert result == ["item1", "item2"]

    mock_data_source_service.get_data.side_effect.assert_awaited_once_with(doc_type, year, month)
    mock_transformer_service.extract_data_from_mfcr_batch_file.assert_called_once_with("001", b"<response>...</response>")
    mock_data_target_service.post_data.side_effect.assert_any_await({"id": "item1"}, correlation_id)
    mock_data_target_service.post_data.side_effect.assert_any_await({"id": "item2"}, correlation_id)


@pytest.mark.asyncio
async def test_001(async_client: httpx.AsyncClient) -> None:
    with unittest.mock.patch("src.api.v1.mfcr._process") as mock_process:
        mock_process.return_value = ["item1", "item2"]
        response = await async_client.post(
            "/api/v1/mfcr/001",
            params={"year": "1970", "month": "01"},
            headers={"Correlation-Id": "test_correlation_id"},
        )

    assert response.status_code == 201
    assert response.json() == ["item1", "item2"]

    mock_process.assert_awaited_once_with("001", "1970", "01", "test_correlation_id")


@pytest.mark.asyncio
async def test_002(async_client: httpx.AsyncClient) -> None:
    with unittest.mock.patch("src.api.v1.mfcr._process") as mock_process:
        mock_process.return_value = ["item1", "item2"]
        response = await async_client.post(
            "/api/v1/mfcr/002",
            params={"year": "1970", "month": "01"},
            headers={"Correlation-Id": "test_correlation_id"},
        )

    assert response.status_code == 201
    assert response.json() == ["item1", "item2"]

    mock_process.assert_awaited_once_with("002", "1970", "01", "test_correlation_id")


@pytest.mark.asyncio
async def test_003(async_client: httpx.AsyncClient) -> None:
    with unittest.mock.patch("src.api.v1.mfcr._process") as mock_process:
        mock_process.return_value = ["item1", "item2"]
        response = await async_client.post(
            "/api/v1/mfcr/003",
            params={"year": "1970", "month": "01"},
            headers={"Correlation-Id": "test_correlation_id"},
        )

    assert response.status_code == 201
    assert response.json() == ["item1", "item2"]

    mock_process.assert_awaited_once_with("003", "1970", "01", "test_correlation_id")


@pytest.mark.asyncio
async def test_080(async_client: httpx.AsyncClient) -> None:
    with unittest.mock.patch("src.api.v1.mfcr._process") as mock_process:
        mock_process.return_value = ["item1", "item2"]
        response = await async_client.post(
            "/api/v1/mfcr/080",
            params={"year": "1970", "month": "01"},
            headers={"Correlation-Id": "test_correlation_id"},
        )

    assert response.status_code == 201
    assert response.json() == ["item1", "item2"]

    mock_process.assert_awaited_once_with("080", "1970", "01", "test_correlation_id")
