from enum import Enum


class CodatDataContractsDatasetsCreditNoteStatus(str, Enum):
    UNKNOWN = "Unknown"
    DRAFT = "Draft"
    SUBMITTED = "Submitted"
    PAID = "Paid"
    VOID = "Void"
    PARTIALLYPAID = "PartiallyPaid"

    def __str__(self) -> str:
        return str(self.value)
