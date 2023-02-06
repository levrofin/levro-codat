from enum import Enum


class CodatAssessDataContractsFinancialsStatementsAccountCategoryStatus(str, Enum):
    CONFIRMED = "Confirmed"
    SUGGESTED = "Suggested"

    def __str__(self) -> str:
        return str(self.value)
