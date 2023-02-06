from enum import Enum


class CodatDataContractsDatasetsAccountStatus(str, Enum):
    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    ARCHIVED = "Archived"
    PENDING = "Pending"

    def __str__(self) -> str:
        return str(self.value)
