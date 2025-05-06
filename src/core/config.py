import pydantic
import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    """
    Environment configuration for the application.
    """
    # Data Source
    DATA_SOURCE_URL: str = "https://monitor.statnipokladna.cz/data/extrakty/csv"

    # Data Target
    DATA_TARGET_URL: str

    # Schedule
    SCHEDULE_HOUR: int = 0
    SCHEDULE_MINUTE: int = 0

    # General
    LOG_LEVEL: pydantic.constr(to_upper=True) = "INFO"


CONFIG = Config()
