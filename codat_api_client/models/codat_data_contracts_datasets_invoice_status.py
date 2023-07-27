from enum import Enum


class CodatDataContractsDatasetsInvoiceStatus(str, Enum):
    DRAFT = "Draft"
    PAID = "Paid"
    PARTIALLYPAID = "PartiallyPaid"
    SUBMITTED = "Submitted"
    UNKNOWN = "Unknown"
    VOID = "Void"

    def __str__(self) -> str:
        return str(self.value)
