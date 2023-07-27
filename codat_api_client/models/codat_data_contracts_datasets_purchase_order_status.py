from enum import Enum


class CodatDataContractsDatasetsPurchaseOrderStatus(str, Enum):
    CLOSED = "Closed"
    DRAFT = "Draft"
    OPEN = "Open"
    UNKNOWN = "Unknown"
    VOID = "Void"

    def __str__(self) -> str:
        return str(self.value)
