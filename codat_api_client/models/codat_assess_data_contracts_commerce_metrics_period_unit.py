from enum import Enum


class CodatAssessDataContractsCommerceMetricsPeriodUnit(str, Enum):
    DAY = "Day"
    MONTH = "Month"
    WEEK = "Week"
    YEAR = "Year"

    def __str__(self) -> str:
        return str(self.value)
