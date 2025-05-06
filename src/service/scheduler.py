import logging
import asyncio
import datetime as dt

from src.core.config import CONFIG
from src.api.v1.mfcr import _process


logger = logging.getLogger(__name__)


async def _schedule():
    while True:
        now = dt.datetime.now()
        next_day = (now + dt.timedelta(days=1)).replace(
            hour=CONFIG.SCHEDULE_HOUR,
            minute=CONFIG.SCHEDULE_MINUTE,
            second=0,
            microsecond=0,
        )

        logger.info(f"scheduling MFCR batch check for {next_day.strftime('%Y-%m-%d %H:%M:%S')}")
        await asyncio.sleep((next_day - now).seconds)

        if next_day.day == 1 and next_day.month in [1, 4, 7, 10]:
            logger.info("processing MFCR batch data for the first day of the quarter")
            try:
                tasks = [
                    _process("001", correlation_id="scheduled-001"),
                    _process("002", correlation_id="scheduled-002"),
                ]

                if next_day.month == 1:
                    tasks.append(_process("003", correlation_id="scheduled-003"))
                    tasks.append(_process("080", correlation_id="scheduled-080"))

                await asyncio.gather(*tasks)
            except Exception as e:
                logger.error(f"error during scheduled MFCR processing: {e}")
        else:
            logger.info("scheduled MFCR processing skipped, not the first day of quarter")


def schedule():
    """
    Schedule daily check if new batch data should be processed from MFCR.
    :return:
    """
    asyncio.create_task(_schedule())
