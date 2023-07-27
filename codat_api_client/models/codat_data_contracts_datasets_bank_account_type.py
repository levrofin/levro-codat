from enum import Enum


class CodatDataContractsDatasetsBankAccountType(str, Enum):
    CREDIT = "Credit"
    DEBIT = "Debit"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
