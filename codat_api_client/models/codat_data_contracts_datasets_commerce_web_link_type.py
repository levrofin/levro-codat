from enum import Enum


class CodatDataContractsDatasetsCommerceWebLinkType(str, Enum):
    SOCIAL = "Social"
    UNKNOWN = "Unknown"
    WEBSITE = "Website"

    def __str__(self) -> str:
        return str(self.value)
