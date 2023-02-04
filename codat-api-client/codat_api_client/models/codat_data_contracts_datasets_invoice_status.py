from enum import Enum


class CodatDataContractsDatasetsInvoiceStatus(str, Enum):
    UNKNOWN = "Unknown"
    DRAFT = "Draft"
    SUBMITTED = "Submitted"
    PARTIALLYPAID = "PartiallyPaid"
    PAID = "Paid"
    VOID = "Void"

    def __str__(self) -> str:
        return str(self.value)
