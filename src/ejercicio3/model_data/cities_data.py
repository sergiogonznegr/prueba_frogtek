from datetime import datetime
import attrs

@attrs.define
class Coord:
    lon: float
    lat: float


@attrs.define
class Sun:
    sunrise: datetime
    sunset: datetime


@attrs.define
class Main:
    temp: int


@attrs.define
class Wind:
    speed: float


@attrs.define
class DataCity:
    coord: Coord
    main: Main
    wind: Wind
    sun: Sun
    name: str
    id: str

