from enum import Enum


class CodatDataContractsDatasetsAccountStatus(str, Enum):
    ACTIVE = "Active"
    ARCHIVED = "Archived"
    PENDING = "Pending"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
