from enum import Enum


class CodatDataContractsDatasetsWebLinkType(str, Enum):
    SOCIAL = "Social"
    UNKNOWN = "Unknown"
    WEBSITE = "Website"

    def __str__(self) -> str:
        return str(self.value)
