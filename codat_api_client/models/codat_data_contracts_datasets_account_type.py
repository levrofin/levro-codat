from enum import Enum


class CodatDataContractsDatasetsAccountType(str, Enum):
    UNKNOWN = "Unknown"
    ASSET = "Asset"
    EXPENSE = "Expense"
    INCOME = "Income"
    LIABILITY = "Liability"
    EQUITY = "Equity"

    def __str__(self) -> str:
        return str(self.value)
