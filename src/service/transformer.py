import io
import zipfile
import typing
import secrets
import datetime as dt

from src.model.document import Document
from src.model.sheet import Sheet


def _type_cast(val: str):
    try:
        v = float(val[:-1])
        return v if val[-1] != "-" else -v
    except ValueError:
        return val


def _extract_001(file: typing.BinaryIO) -> list[Document | Sheet] | None:
    """
    Extract single document from 001 batch file
    :param file: file object
    :return: list with Document and its Sheets
    """
    line = file.readline()
    row = line.decode("utf-8").strip().split(';')

    if row[0] == "ZZZ":
        return None

    doc_id = secrets.token_hex(16)
    subject_id = row[4]
    period = dt.date(year=int(row[2][:4]), month=int(row[2][-2:]), day=1)
    sheet_data = [[_type_cast(r) for r in row[-6:]]]

    while (line := file.readline()) and (row := line.decode("utf-8").strip().split(';')) and row[4] == subject_id:
        sheet_data.append([_type_cast(r) for r in row[-6:]])

    file.seek(-len(line), 1)  # move back to the last line read

    sheet_1 = Sheet(
        id=secrets.token_hex(16),
        name="Aktiva",
        number=1,
        subject_id=subject_id,
        doc_id=doc_id,
        items=[row for row in sheet_data if "A" in row[0] or "B" in row[0] or "AKTIVA" in row[0]]
    )
    sheet_2 = Sheet(
        id=secrets.token_hex(16),
        name="Pasiva",
        number=2,
        subject_id=subject_id,
        doc_id=doc_id,
        items=[row for row in sheet_data if "C" in row[0] or "D" in row[0] or "PASIVA" in row[0]]
    )
    return [
        sheet_1,
        sheet_2,
        Document(
            id=doc_id,
            subject_id=subject_id,
            type={
                "key": "001",
                "name": "Rozvaha",
                "layer": 1,
                "order": 1,
            },
            period=period,
            version={
                "version": 1,
                "author": "BATCH-DATA-SERVICE",
                "created": dt.datetime.now()
            },
            sheets=[sheet_1.model_dump(), sheet_2.model_dump()],
        )
    ]


def _extract_002(file: typing.BinaryIO) -> list[Document | Sheet] | None:
    """
    Extract single document from 002 batch file
    :param file: file object
    :return: list with Document and its Sheets
    """
    line = file.readline()
    row = line.decode("utf-8").strip().split(';')

    if row[0] == "ZZZ":
        return None

    doc_id = secrets.token_hex(16)
    subject_id = row[4]
    period = dt.date(year=int(row[2][:4]), month=int(row[2][-2:]), day=1)
    sheet_data = [[_type_cast(r) for r in row[-6:]]]

    while (line := file.readline()) and (row := line.decode("utf-8").strip().split(';')) and row[4] == subject_id:
        sheet_data.append([_type_cast(r) for r in row[-6:]])

    file.seek(-len(line), 1)  # move back to the last line read

    sheet_1 = Sheet(
        id=secrets.token_hex(16),
        name="Výkaz zisku a ztráty",
        number=1,
        subject_id=subject_id,
        doc_id=doc_id,
        items=sheet_data
    )
    return [
        sheet_1,
        Document(
            id=doc_id,
            subject_id=subject_id,
            type={
                "key": "002",
                "name": "Výkaz zisku a ztráty",
                "layer": 1,
                "order": 2,
            },
            period=period,
            version={
                "version": 1,
                "author": "BATCH-DATA-SERVICE",
                "created": dt.datetime.now()
            },
            sheets=[sheet_1.model_dump()],
        )
    ]


def _extract_003(file: typing.BinaryIO) -> list[Document | Sheet] | None:
    """
    Extract single document from 003 batch file
    :param file: file object
    :return: list with Document and its Sheets
    """
    line = file.readline()
    row = line.decode("utf-8").strip().split(';')

    if row[0] == "ZZZ":
        return None

    doc_id = secrets.token_hex(16)
    subject_id = row[4]
    period = dt.date(year=int(row[2][:4]), month=int(row[2][-2:]), day=1)
    sheet_data = [[_type_cast(r) for r in row[-2:]]]

    while (line := file.readline()) and (row := line.decode("utf-8").strip().split(';')) and row[4] == subject_id:
        sheet_data.append([_type_cast(r) for r in row[-2:]])

    file.seek(-len(line), 1)  # move back to the last line read

    sheet_1 = Sheet(
        id=secrets.token_hex(16),
        name="PenezniToky",
        number=1,
        subject_id=subject_id,
        doc_id=doc_id,
        items=sheet_data
    )
    return [
        sheet_1,
        Document(
            id=doc_id,
            subject_id=subject_id,
            type={
                "key": "003",
                "name": "PenezniTokyAVlastniKapital",
                "layer": 1,
                "order": 3,
            },
            period=period,
            version={
                "version": 1,
                "author": "BATCH-DATA-SERVICE",
                "created": dt.datetime.now()
            },
            sheets=[sheet_1.model_dump()],
        )
    ]


def _extract_080(file: typing.BinaryIO) -> list[Document | Sheet] | None:
    """
    Extract single document from 080 batch file
    :param file: file object
    :return: list with Document and its Sheets
    """
    line = file.readline()
    row = line.decode("utf-8").strip().split(';')

    if row[0] == "ZZZ":
        return None

    doc_id = secrets.token_hex(16)
    subject_id = row[4]
    period = dt.date(year=int(row[2][:4]), month=int(row[2][-2:]), day=1)
    sheet_data = [[
        row[5],
        row[6],
        row[7],
        row[8],
        row[9],
        _type_cast(row[-4]),
        _type_cast(row[-3]),
        _type_cast(row[-2]),
        _type_cast(row[-1]),
        f"{row[11][:4]}-{row[11][4:6]}-{row[11][6:8]}",
        f"{row[12][:4]}-{row[12][4:6]}-{row[12][6:8]}",
        row[10],
    ]]

    while (line := file.readline()) and (row := line.decode("utf-8").strip().split(';')) and row[4] == subject_id:
        sheet_data.append([
            row[5],
            row[6],
            row[7],
            row[8],
            row[9],
            _type_cast(row[-4]),
            _type_cast(row[-3]),
            _type_cast(row[-2]),
            _type_cast(row[-1]),
            f"{row[11][:4]}-{row[11][4:6]}-{row[11][6:8]}",
            f"{row[12][:4]}-{row[12][4:6]}-{row[12][6:8]}",
            row[10],
        ])

    file.seek(-len(line), 1)  # move back to the last line read

    sheet_1 = Sheet(
        id=secrets.token_hex(16),
        name="080",
        number=1,
        subject_id=subject_id,
        doc_id=doc_id,
        items=sheet_data
    )
    return [
        sheet_1,
        Document(
            id=doc_id,
            subject_id=subject_id,
            type={
                "key": "080",
                "name": "080",
                "layer": 1,
                "order": 4,
            },
            period=period,
            version={
                "version": 1,
                "author": "BATCH-DATA-SERVICE",
                "created": dt.datetime.now()
            },
            sheets=[sheet_1.model_dump()],
        )
    ]


def extract_data_from_mfcr_batch_file(doc_type: str, data: bytes) -> typing.Generator[Document | Sheet, None, None]:
    """
    Extracts data from MFCR batch file
    :param doc_type: Document type ("001", "002", "003", "080")
    :param data: ZIP data in bytes
    :return: Generator of Document and Sheet objects
    """
    zip_file = zipfile.ZipFile(io.BytesIO(data))

    for file_name in zip_file.namelist():
        with zip_file.open(file_name) as file:
            file.readline() # skip header

            while True:
                extracted = globals()["_extract_" + doc_type](file)
                extracted = False

                if not extracted:
                    break

                for item in extracted:
                    yield item
