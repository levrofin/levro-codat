from enum import Enum


class CodatDataContractsDatasetsCommercePhoneType(str, Enum):
    FAX = "Fax"
    LANDLINE = "Landline"
    MOBILE = "Mobile"
    PRIMARY = "Primary"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
