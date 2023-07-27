from enum import Enum


class CodatDataContractsDatasetsInvoicingStatus(str, Enum):
    INVOICED = "Invoiced"
    NOTINVOICED = "NotInvoiced"
    PARTIALLYINVOICED = "PartiallyInvoiced"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
