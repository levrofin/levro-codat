from enum import Enum


class CodatDataContractsDatasetsAccountType(str, Enum):
    ASSET = "Asset"
    EQUITY = "Equity"
    EXPENSE = "Expense"
    INCOME = "Income"
    LIABILITY = "Liability"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
