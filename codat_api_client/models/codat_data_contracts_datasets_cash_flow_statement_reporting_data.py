from enum import Enum


class CodatDataContractsDatasetsCashFlowStatementReportingData(str, Enum):
    UNKNOWN = "Unknown"
    INDIRECT = "Indirect"
    DIRECT = "Direct"

    def __str__(self) -> str:
        return str(self.value)
