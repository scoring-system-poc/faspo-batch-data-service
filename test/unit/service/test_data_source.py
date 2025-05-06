import pytest
import datetime as dt

from src.core.exception import HTTPException


@pytest.mark.asyncio
async def test_get_data_001__success(mock_aiohttp) -> None:
    from src.service.data_source import get_data
    from src.core.config import CONFIG

    response = await get_data("001", "1970", "01")

    assert response == b"mock;csv;data;"
    mock_aiohttp.get.assert_called_once_with(f"{CONFIG.DATA_SOURCE_URL}/Rozvaha/1970_01_Data_CSUIS_ROZV.zip")


@pytest.mark.asyncio
async def test_get_data_002__success(mock_aiohttp) -> None:
    from src.service.data_source import get_data
    from src.core.config import CONFIG

    response = await get_data("002", "1970", "01")

    assert response == b"mock;csv;data;"
    mock_aiohttp.get.assert_called_once_with(f"{CONFIG.DATA_SOURCE_URL}/ZiskZtraty/1970_01_Data_CSUIS_VYKZZ.zip")


@pytest.mark.asyncio
async def test_get_data_003__success(mock_aiohttp) -> None:
    from src.service.data_source import get_data
    from src.core.config import CONFIG

    response = await get_data("003", "1970", "01")

    assert response == b"mock;csv;data;"
    mock_aiohttp.get.assert_called_once_with(f"{CONFIG.DATA_SOURCE_URL}/PenezniToky/1970_01_Data_CSUIS_PPT.zip")


@pytest.mark.asyncio
async def test_get_data_080__success(mock_aiohttp) -> None:
    from src.service.data_source import get_data
    from src.core.config import CONFIG

    response = await get_data("080", "1970", "01")

    assert response == b"mock;csv;data;"
    mock_aiohttp.get.assert_called_once_with(f"{CONFIG.DATA_SOURCE_URL}/FinSZU/1970_01_Data_CSUIS_FINSZU.zip")


@pytest.mark.asyncio
async def test_get_data__default_month(mock_aiohttp) -> None:
    from src.service.data_source import get_data
    from src.core.config import CONFIG

    response = await get_data("001", "1970")

    assert response == b"mock;csv;data;"
    mock_aiohttp.get.assert_called_once_with(f"{CONFIG.DATA_SOURCE_URL}/Rozvaha/1970_12_Data_CSUIS_ROZV.zip")


@pytest.mark.asyncio
async def test_get_data__default_year(mock_aiohttp) -> None:
    from src.service.data_source import get_data
    from src.core.config import CONFIG

    response = await get_data("001", None, "03")
    year = str(dt.datetime.today().year)

    assert response == b"mock;csv;data;"
    mock_aiohttp.get.assert_called_once_with(f"{CONFIG.DATA_SOURCE_URL}/Rozvaha/{year}_03_Data_CSUIS_ROZV.zip")


@pytest.mark.asyncio
async def test_get_data__default(mock_aiohttp) -> None:
    from src.service.data_source import get_data
    from src.core.config import CONFIG

    response = await get_data("001")
    year = str(dt.datetime.today().year)
    month = str(dt.datetime.today().month).zfill(2)

    assert response == b"mock;csv;data;"
    mock_aiohttp.get.assert_called_once_with(f"{CONFIG.DATA_SOURCE_URL}/Rozvaha/{year}_{month}_Data_CSUIS_ROZV.zip")


@pytest.mark.asyncio
async def test_get_data__failure(mock_aiohttp) -> None:
    mock_aiohttp.status = 404
    mock_aiohttp.reason = "Not Found"

    from src.service.data_source import get_data

    with pytest.raises(HTTPException) as exc_info:
        await get_data("001", "1970", "01")

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Data source API request failed: Not Found"




