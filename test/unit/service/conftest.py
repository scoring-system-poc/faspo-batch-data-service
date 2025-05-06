import pytest
import unittest.mock
import typing
import io


@pytest.fixture
def mock_aiohttp() -> unittest.mock.AsyncMock:
    with unittest.mock.patch("aiohttp.ClientSession") as mock_aiohttp:
        mock_aiohttp.return_value = mock_aiohttp
        mock_aiohttp.get.return_value = mock_aiohttp
        mock_aiohttp.__aenter__.side_effect = mock_aiohttp

        mock_aiohttp.status = 200
        mock_aiohttp.read.side_effect = unittest.mock.AsyncMock(return_value=b"mock;csv;data;")
        mock_aiohttp.text.side_effect = unittest.mock.AsyncMock(return_value="id")

        yield mock_aiohttp


@pytest.fixture
def mock_mfcr_001_batch_content() -> typing.BinaryIO:
    return io.BytesIO(
        """001;000100;2024003;1000009999;12345678;;CZ020;CZ020B;A.I.1.;1;89470.00 ;0.00 ;89470.00 ;59740.00
        001;000100;2024003;1000009999;12345678;;CZ020;CZ020B;C.I.1.;2;9100.00 ;0.00 ;9100.00 ;0.00
        ZZZ;;0000000;;00000000;;;;;;0.00 ;0.00 ;0.00 ;1197476.00
        """.encode("utf-8")
    )


@pytest.fixture
def mock_mfcr_001_batch_content_with_header() -> typing.BinaryIO:
    return io.BytesIO(
        """some;fake;header
        001;000100;2024003;1000009999;12345678;;CZ020;CZ020B;A.I.1.;1;89470.00 ;0.00 ;89470.00 ;59740.00
        001;000100;2024003;1000009999;12345678;;CZ020;CZ020B;C.I.1.;2;9100.00 ;0.00 ;9100.00 ;0.00
        ZZZ;;0000000;;00000000;;;;;;0.00 ;0.00 ;0.00 ;1197476.00
        """.encode("utf-8")
    )



@pytest.fixture
def mock_mfcr_002_batch_content() -> typing.BinaryIO:
    return io.BytesIO(
        """002;000100;2024003;1000009999;12345678;;CZ020;CZ020B;A.I.1.;1;89470.00 ;0.00 ;89470.00 ;59740.00
        ZZZ;;0000000;;00000000;;;;;;0.00 ;0.00 ;0.00 ;1197476.00
        """.encode("utf-8")
    )


@pytest.fixture
def mock_mfcr_003_batch_content() -> typing.BinaryIO:
    return io.BytesIO(
        """003;000100;2024003;1000009999;12345678;0329;;CZ0100;A.;15396881066.55-
        ZZZ;;0000000;;00000000;;;;;;0.00 ;0.00 ;0.00 ;1197476.00
        """.encode("utf-8")
    )


@pytest.fixture
def mock_mfcr_080_batch_content() -> typing.BinaryIO:
    return io.BytesIO(
        """080;000100;2024003;1000009999;12345678;70856788;Státní fond podpory investic;Ú;Komunitní centrum Bystřice;CZK;bezúročně;20230327;20330131;03;22609000.00 ;22609000.00 ;1722600.00 ;0.00
        ZZZ;;0000000;;00000000;;;;;;0.00 ;0.00 ;0.00 ;1197476.00
        """.encode("utf-8")
    )
