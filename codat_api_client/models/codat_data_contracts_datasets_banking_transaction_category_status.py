from enum import Enum


class CodatDataContractsDatasetsBankingTransactionCategoryStatus(str, Enum):
    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    ARCHIVED = "Archived"

    def __str__(self) -> str:
        return str(self.value)
