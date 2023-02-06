from enum import Enum


class CodatAssessDataContractsFinancialsMetricsMetricErrorType(str, Enum):
    UNCATEGORIZEDACCOUNTS = "UncategorizedAccounts"
    MISSINGINPUTDATA = "MissingInputData"
    INPUTDATAERROR = "InputDataError"

    def __str__(self) -> str:
        return str(self.value)
