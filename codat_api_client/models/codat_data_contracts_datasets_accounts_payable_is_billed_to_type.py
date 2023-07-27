from enum import Enum


class CodatDataContractsDatasetsAccountsPayableIsBilledToType(str, Enum):
    CUSTOMER = "Customer"
    NOTAPPLICABLE = "NotApplicable"
    PROJECT = "Project"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
