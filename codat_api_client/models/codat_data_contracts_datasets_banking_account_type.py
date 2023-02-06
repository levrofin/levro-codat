from enum import Enum


class CodatDataContractsDatasetsBankingAccountType(str, Enum):
    UNKNOWN = "Unknown"
    CREDIT = "Credit"
    DEBIT = "Debit"

    def __str__(self) -> str:
        return str(self.value)
