from enum import Enum


class CodatDataContractsDatasetsAccountsReceivableIsBilledToType(str, Enum):
    NOTAPPLICABLE = "NotApplicable"
    PROJECT = "Project"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
