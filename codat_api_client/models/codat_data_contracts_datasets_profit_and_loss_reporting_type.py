from enum import Enum


class CodatDataContractsDatasetsProfitAndLossReportingType(str, Enum):
    ACCRUAL = "Accrual"
    CASH = "Cash"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
