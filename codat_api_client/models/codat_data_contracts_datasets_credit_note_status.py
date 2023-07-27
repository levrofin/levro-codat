from enum import Enum


class CodatDataContractsDatasetsCreditNoteStatus(str, Enum):
    DRAFT = "Draft"
    PAID = "Paid"
    PARTIALLYPAID = "PartiallyPaid"
    SUBMITTED = "Submitted"
    UNKNOWN = "Unknown"
    VOID = "Void"

    def __str__(self) -> str:
        return str(self.value)
