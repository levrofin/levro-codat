from enum import Enum


class CodatDataContractsDatasetsCashFlowStatementReportingBasis(str, Enum):
    ACCRUAL = "Accrual"
    CASH = "Cash"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
