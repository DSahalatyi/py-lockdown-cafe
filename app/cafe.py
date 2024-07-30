from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if not visitor.get("vaccine"):
            raise NotVaccinatedError(visitor["name"])

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < date.today():
            raise OutdatedVaccineError(visitor["name"])

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(visitor["name"])

        return f"Welcome to {self.name}"