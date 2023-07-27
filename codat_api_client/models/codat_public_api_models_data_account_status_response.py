from enum import Enum


class CodatPublicApiModelsDataAccountStatusResponse(str, Enum):
    ACTIVE = "Active"
    ARCHIVED = "Archived"
    PENDING = "Pending"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
