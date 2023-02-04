from enum import Enum


class CodatDataContractsDatasetsWebLinkType(str, Enum):
    UNKNOWN = "Unknown"
    WEBSITE = "Website"
    SOCIAL = "Social"

    def __str__(self) -> str:
        return str(self.value)
