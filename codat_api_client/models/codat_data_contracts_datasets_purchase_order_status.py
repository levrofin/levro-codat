from enum import Enum


class CodatDataContractsDatasetsPurchaseOrderStatus(str, Enum):
    UNKNOWN = "Unknown"
    DRAFT = "Draft"
    OPEN = "Open"
    CLOSED = "Closed"
    VOID = "Void"

    def __str__(self) -> str:
        return str(self.value)
