from enum import Enum


class CodatDataContractsDatasetsAccountsReceivableIsBilledToType(str, Enum):
    UNKNOWN = "Unknown"
    NOTAPPLICABLE = "NotApplicable"
    PROJECT = "Project"

    def __str__(self) -> str:
        return str(self.value)
