import aiohttp
import datetime as dt

from src.core.config import CONFIG
from src.core.exception import HTTPException


async def get_data(doc_type: str, year: str | None = None, month: str | None = None) -> bytes:
    """
    Get batch data from the data source API.
    :param doc_type: Type of financial document.
    :param year: Year of the batch.
    :param month: Month of the batch.
    :return: Raw data in bytes.
    """
    path_mapping = {
        "001": ("Rozvaha", "ROZV"),
        "002": ("ZiskZtraty", "VYKZZ"),
        "003": ("PenezniToky", "PPT"),
        "080": ("FinSZU", "FINSZU"),
    }
    today = dt.datetime.today()

    url_details = path_mapping.get(doc_type)
    year = str(year or today.year)
    month = str(month or ("12" if year != today.year else today.month))

    url = f"{CONFIG.DATA_SOURCE_URL}/{url_details[0]}/{year}_{month.zfill(2)}_Data_CSUIS_{url_details[1]}.zip"

    async with (
        aiohttp.ClientSession() as async_session,
        async_session.get(url) as response,
    ):
        if response.status != 200:
            raise HTTPException(
                status_code=response.status,
                detail=f"Data source API request failed: {response.reason}",
                logger_name=__name__,
            )

        return await response.read()
