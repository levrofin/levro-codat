from enum import Enum


class CodatAssessDataContractsCashFlowTransactionsSourceType(str, Enum):
    BANKING = "Banking"

    def __str__(self) -> str:
        return str(self.value)
