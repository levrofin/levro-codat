from enum import Enum


class CodatDataContractsDatasetsAccountsPayableIsBilledToType(str, Enum):
    UNKNOWN = "Unknown"
    NOTAPPLICABLE = "NotApplicable"
    CUSTOMER = "Customer"
    PROJECT = "Project"

    def __str__(self) -> str:
        return str(self.value)
