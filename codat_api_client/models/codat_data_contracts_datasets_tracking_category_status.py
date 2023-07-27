from enum import Enum


class CodatDataContractsDatasetsTrackingCategoryStatus(str, Enum):
    ACTIVE = "Active"
    ARCHIVED = "Archived"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
