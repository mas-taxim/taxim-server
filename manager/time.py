from datetime import datetime


def transform(yyyy: int, mm: int, dd: int, hh: int, mi: int):
    dt = datetime(yyyy, mm, dd, hh, mi, 00)
    return dt.strftime("%Y%m%d"), dt.timestamp() * 1000
