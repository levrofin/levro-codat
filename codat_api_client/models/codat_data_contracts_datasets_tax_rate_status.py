from enum import Enum


class CodatDataContractsDatasetsTaxRateStatus(str, Enum):
    ACTIVE = "Active"
    ARCHIVED = "Archived"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
