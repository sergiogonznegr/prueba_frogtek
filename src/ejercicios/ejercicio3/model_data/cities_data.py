from datetime import datetime

from attrs import define, field


def timestamp_to_datetime(date_timestamp: int) -> datetime:
    return datetime.fromtimestamp(date_timestamp)


@define
class Sun:
    sunrise: datetime = field(converter=timestamp_to_datetime)
    sunset: datetime = field(converter=timestamp_to_datetime)


@define
class Coord:
    lon: str
    lat: str


@define
class Temp:
    temp: str


@define
class Wind:
    speed: str


@define
class DataCity:
    coord: Coord = None
    main: Temp = None
    wind: Wind = None
    name: str = None
    sun: Sun = None
