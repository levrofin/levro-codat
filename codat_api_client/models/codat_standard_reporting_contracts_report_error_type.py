from enum import Enum


class CodatStandardReportingContractsReportErrorType(str, Enum):
    DATESOUTOFRANGE = "DatesOutOfRange"
    DATANOTSYNCED = "DataNotSynced"
    DATASETNOTSUPPORTED = "DataSetNotSupported"
    DATASYNCFAILED = "DataSyncFailed"
    DATATYPENOTENABLED = "DataTypeNotEnabled"
    UNCATEGORIZEDACCOUNTS = "UncategorizedAccounts"
    DATASETNOTAVAILABLE = "DataSetNotAvailable"
    VALIDATIONERROR = "ValidationError"

    def __str__(self) -> str:
        return str(self.value)
