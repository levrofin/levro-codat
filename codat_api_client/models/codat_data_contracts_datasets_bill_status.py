from enum import Enum


class CodatDataContractsDatasetsBillStatus(str, Enum):
    DRAFT = "Draft"
    OPEN = "Open"
    PAID = "Paid"
    PARTIALLYPAID = "PartiallyPaid"
    UNKNOWN = "Unknown"
    VOID = "Void"

    def __str__(self) -> str:
        return str(self.value)
