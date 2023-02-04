from enum import Enum


class CodatAssessDataContractsCommerceMetricsPeriodUnit(str, Enum):
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"

    def __str__(self) -> str:
        return str(self.value)
