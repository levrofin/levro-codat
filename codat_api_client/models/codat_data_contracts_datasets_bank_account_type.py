from enum import Enum


class CodatDataContractsDatasetsBankAccountType(str, Enum):
    UNKNOWN = "Unknown"
    CREDIT = "Credit"
    DEBIT = "Debit"

    def __str__(self) -> str:
        return str(self.value)
