from enum import Enum


class CodatDataContractsDatasetsTransferStatus(str, Enum):
    UNKNOWN = "Unknown"
    UNRECONCILED = "Unreconciled"
    RECONCILED = "Reconciled"
    VOID = "Void"

    def __str__(self) -> str:
        return str(self.value)
