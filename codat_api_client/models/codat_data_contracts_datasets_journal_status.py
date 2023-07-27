from enum import Enum


class CodatDataContractsDatasetsJournalStatus(str, Enum):
    ACTIVE = "Active"
    ARCHIVED = "Archived"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
