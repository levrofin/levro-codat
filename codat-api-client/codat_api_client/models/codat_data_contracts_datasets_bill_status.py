from enum import Enum


class CodatDataContractsDatasetsBillStatus(str, Enum):
    UNKNOWN = "Unknown"
    OPEN = "Open"
    PARTIALLYPAID = "PartiallyPaid"
    PAID = "Paid"
    VOID = "Void"
    DRAFT = "Draft"

    def __str__(self) -> str:
        return str(self.value)
