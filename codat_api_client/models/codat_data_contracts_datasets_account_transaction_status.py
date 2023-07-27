from enum import Enum


class CodatDataContractsDatasetsAccountTransactionStatus(str, Enum):
    RECONCILED = "Reconciled"
    UNKNOWN = "Unknown"
    UNRECONCILED = "Unreconciled"
    VOID = "Void"

    def __str__(self) -> str:
        return str(self.value)
