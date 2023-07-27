from enum import Enum


class CodatDataContractsDatasetsTransferStatus(str, Enum):
    RECONCILED = "Reconciled"
    UNKNOWN = "Unknown"
    UNRECONCILED = "Unreconciled"
    VOID = "Void"

    def __str__(self) -> str:
        return str(self.value)
