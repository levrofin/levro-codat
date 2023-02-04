from enum import Enum


class CodatDataContractsDatasetsInvoicingStatus(str, Enum):
    UNKNOWN = "Unknown"
    PARTIALLYINVOICED = "PartiallyInvoiced"
    INVOICED = "Invoiced"
    NOTINVOICED = "NotInvoiced"

    def __str__(self) -> str:
        return str(self.value)
