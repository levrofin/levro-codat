from enum import Enum


class CodatAssessDataContractsFinancialsMetricsMetricDataSetErrorType(str, Enum):
    DATESOUTOFRANGE = "DatesOutOfRange"
    DATANOTSYNCED = "DataNotSynced"
    DATASETNOTSUPPORTED = "DataSetNotSupported"
    DATASYNCFAILED = "DataSyncFailed"
    DATATYPENOTENABLED = "DataTypeNotEnabled"

    def __str__(self) -> str:
        return str(self.value)
