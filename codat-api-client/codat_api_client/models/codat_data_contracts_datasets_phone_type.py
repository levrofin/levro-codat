from enum import Enum


class CodatDataContractsDatasetsPhoneType(str, Enum):
    UNKNOWN = "Unknown"
    PRIMARY = "Primary"
    LANDLINE = "Landline"
    MOBILE = "Mobile"
    FAX = "Fax"

    def __str__(self) -> str:
        return str(self.value)
