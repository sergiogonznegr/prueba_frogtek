import attrs

@attrs.define
class CityNotFound:
    name: str
    message: str