from enum import Enum


class CodatDataContractsDatasetsCashFlowStatementReportingData(str, Enum):
    DIRECT = "Direct"
    INDIRECT = "Indirect"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
