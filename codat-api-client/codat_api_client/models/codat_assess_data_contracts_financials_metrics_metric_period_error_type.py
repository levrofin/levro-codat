from enum import Enum


class CodatAssessDataContractsFinancialsMetricsMetricPeriodErrorType(str, Enum):
    MISSINGACCOUNTDATA = "MissingAccountData"
    DATESOUTOFRANGE = "DatesOutOfRange"

    def __str__(self) -> str:
        return str(self.value)
