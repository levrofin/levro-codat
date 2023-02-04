from enum import Enum


class CodatAssessDataContractsFinancialsMetricsMetricUnit(str, Enum):
    RATIO = "Ratio"
    MONEY = "Money"

    def __str__(self) -> str:
        return str(self.value)
