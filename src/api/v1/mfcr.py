import typing
import logging
import fastapi

from src.core.exception import HTTPException
from src.service import data_source, data_target, transformer


logger = logging.getLogger(__name__)
router = fastapi.APIRouter(
    prefix="/mfcr",
    tags=["MFCR"],
)


async def _process(
    doc_type: str,
    year: str | None = None,
    month: str | None = None,
    correlation_id: typing.Annotated[str | None, fastapi.Header()] = None,
) -> list[str]:
    """
    Process batch data from MFCR for the given document type, year, and month.
    :param doc_type: Document type to process ("001", "002", "003", "080").
    :param year: Year of the data to process.
    :param month: Month of the data to process.
    :param correlation_id: Correlation ID for tracking the request.
    :return: List of item IDs that were posted to the target.
    """
    logger.info(f"acquired: doc_type={doc_type}; year={year}; month={month};")
    try:
        raw_data = await data_source.get_data(doc_type, year, month)
        logger.info("MFCR batch data downloaded")

        transformed_data = transformer.extract_data_from_mfcr_batch_file(doc_type, raw_data)
        logger.info("Data transformation successful")

        item_ids = [await data_target.post_data(item, correlation_id) for item in transformed_data]
        logger.info("Data posting successful")

        return item_ids

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(
            status_code=500,
            logger_name=__name__,
            logger_lvl=logging.ERROR,
            logger_msg=f"MFCR API request failed: {str(e)}",
        )


@router.post("/001")
async def mfcr_001(
    year: str | None = None,
    month: str | None = None,
    correlation_id: typing.Annotated[str | None, fastapi.Header()] = None,
) -> fastapi.responses.JSONResponse:
    return fastapi.responses.JSONResponse(
        status_code=201,
        content=await _process("001", year, month, correlation_id),
    )


@router.post("/002")
async def mfcr_002(
    year: str | None = None,
    month: str | None = None,
    correlation_id: typing.Annotated[str | None, fastapi.Header()] = None,
) -> fastapi.responses.JSONResponse:
    return fastapi.responses.JSONResponse(
        status_code=201,
        content=await _process("002", year, month, correlation_id),
    )


@router.post("/003")
async def mfcr_003(
    year: str | None = None,
    month: str | None = None,
    correlation_id: typing.Annotated[str | None, fastapi.Header()] = None,
) -> fastapi.responses.JSONResponse:
    return fastapi.responses.JSONResponse(
        status_code=201,
        content=await _process("003", year, month, correlation_id),
    )


@router.post("/080")
async def mfcr_080(
    year: str | None = None,
    month: str | None = None,
    correlation_id: typing.Annotated[str | None, fastapi.Header()] = None,
) -> fastapi.responses.JSONResponse:
    return fastapi.responses.JSONResponse(
        status_code=201,
        content=await _process("080", year, month, correlation_id),
    )
