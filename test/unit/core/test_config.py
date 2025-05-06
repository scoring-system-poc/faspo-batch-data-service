import pytest


@pytest.mark.asyncio
async def test_config(mock_environ) -> None:
    from src.core.config import CONFIG

    assert CONFIG.DATA_SOURCE_URL == "https://monitor.statnipokladna.gov.cz/api/monitorws"
    assert CONFIG.DATA_TARGET_URL == "http://localhost:8080/api/v1/data_target"
    assert CONFIG.SCHEDULE_HOUR == 0
    assert CONFIG.SCHEDULE_MINUTE == 0
    assert CONFIG.LOG_LEVEL == "INFO"


