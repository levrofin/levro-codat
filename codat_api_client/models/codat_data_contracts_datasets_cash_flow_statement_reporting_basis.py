from enum import Enum


class CodatDataContractsDatasetsCashFlowStatementReportingBasis(str, Enum):
    UNKNOWN = "Unknown"
    ACCRUAL = "Accrual"
    CASH = "Cash"

    def __str__(self) -> str:
        return str(self.value)
