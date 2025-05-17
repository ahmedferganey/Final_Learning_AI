from datetime import datetime

def format_datetime(dt: datetime) -> str:
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def round_float(value: float, decimals: int = 2) -> float:
    return round(value, decimals)
