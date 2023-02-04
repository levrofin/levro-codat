from enum import Enum


class CodatDataContractsDatasetsCommerceWebLinkType(str, Enum):
    UNKNOWN = "Unknown"
    WEBSITE = "Website"
    SOCIAL = "Social"

    def __str__(self) -> str:
        return str(self.value)
