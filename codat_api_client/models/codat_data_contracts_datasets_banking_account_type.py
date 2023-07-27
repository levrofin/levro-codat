from enum import Enum


class CodatDataContractsDatasetsBankingAccountType(str, Enum):
    CREDIT = "Credit"
    DEBIT = "Debit"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
