from enum import Enum


class CodatDataContractsDatasetsTrackingCategoryStatus(str, Enum):
    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    ARCHIVED = "Archived"

    def __str__(self) -> str:
        return str(self.value)
