import unittest.mock

import pytest
import datetime as dt

from src.service.transformer import (
    _type_cast,
    _extract_001,
    _extract_002,
    _extract_003,
    _extract_080,
    extract_data_from_mfcr_batch_file,
)
from src.model.document import Document
from src.model.sheet import Sheet


@pytest.mark.asyncio
async def test_type_cast__success():
    assert _type_cast("1.2 ") == 1.2
    assert _type_cast("1.2-") == -1.2
    assert _type_cast("abc") == "abc"


@pytest.mark.asyncio
async def test_extract_001(mock_mfcr_001_batch_content):
    result = _extract_001(mock_mfcr_001_batch_content)

    assert isinstance(result, list)
    assert len(result) == 3

    assert isinstance(result[0], Sheet)
    assert isinstance(result[1], Sheet)
    assert isinstance(result[2], Document)

    assert result[0].number == 1
    assert result[0].subject_id == "12345678"
    assert result[0].doc_id == result[2].id
    assert len(result[0].items) == 1
    assert result[0].items[0] == ["A.I.1.", "1", 89470.0, 0.0, 89470.0, 59740.0]

    assert result[1].number == 2
    assert result[1].subject_id == "12345678"
    assert result[1].doc_id == result[2].id
    assert len(result[1].items) == 1
    assert result[1].items[0] == ["C.I.1.", "2", 9100.0, 0.0, 9100.0, 0.0]

    assert result[2].subject_id == "12345678"
    assert result[2].type.key == "001"
    assert result[2].period == dt.date(2024, 3, 1)
    assert len(result[2].sheets) == 2


@pytest.mark.asyncio
async def test_extract_002(mock_mfcr_002_batch_content):
    result = _extract_002(mock_mfcr_002_batch_content)

    assert isinstance(result, list)
    assert len(result) == 2

    assert isinstance(result[0], Sheet)
    assert isinstance(result[1], Document)

    assert result[0].number == 1
    assert result[0].subject_id == "12345678"
    assert result[0].doc_id == result[1].id
    assert len(result[0].items) == 1
    assert result[0].items[0] == ["A.I.1.", "1", 89470.0, 0.0, 89470.0, 59740.0]

    assert result[1].subject_id == "12345678"
    assert result[1].type.key == "002"
    assert result[1].period == dt.date(2024, 3, 1)
    assert len(result[1].sheets) == 1


@pytest.mark.asyncio
async def test_extract_003(mock_mfcr_003_batch_content):
    result = _extract_003(mock_mfcr_003_batch_content)

    assert isinstance(result, list)
    assert len(result) == 2

    assert isinstance(result[0], Sheet)
    assert isinstance(result[1], Document)

    assert result[0].number == 1
    assert result[0].subject_id == "12345678"
    assert result[0].doc_id == result[1].id
    assert len(result[0].items) == 1
    assert result[0].items[0] == ["A.", -15396881066.55]

    assert result[1].subject_id == "12345678"
    assert result[1].type.key == "003"
    assert result[1].period == dt.date(2024, 3, 1)
    assert len(result[1].sheets) == 1


@pytest.mark.asyncio
async def test_extract_080(mock_mfcr_080_batch_content):
    result = _extract_080(mock_mfcr_080_batch_content)

    assert isinstance(result, list)
    assert len(result) == 2

    assert isinstance(result[0], Sheet)
    assert isinstance(result[1], Document)

    assert result[0].number == 1
    assert result[0].subject_id == "12345678"
    assert result[0].doc_id == result[1].id
    assert len(result[0].items) == 1
    assert result[0].items[0] == ["70856788", "Státní fond podpory investic", "Ú", "Komunitní centrum Bystřice", "CZK", 22609000.0, 22609000.0, 1722600.0, 0.0, "2023-03-27", "2033-01-31", "bezúročně"]

    assert result[1].subject_id == "12345678"
    assert result[1].type.key == "080"
    assert result[1].period == dt.date(2024, 3, 1)
    assert len(result[1].sheets) == 1


@pytest.mark.asyncio
async def test_extract_data_from_mfcr_batch_file(mock_mfcr_001_batch_content_with_header):
    pass
