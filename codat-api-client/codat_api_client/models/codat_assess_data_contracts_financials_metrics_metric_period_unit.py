from enum import Enum


class CodatAssessDataContractsFinancialsMetricsMetricPeriodUnit(str, Enum):
    MONTH = "Month"
    WEEK = "Week"
    DAY = "Day"

    def __str__(self) -> str:
        return str(self.value)
