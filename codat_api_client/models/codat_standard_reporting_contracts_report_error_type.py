from enum import Enum


class CodatStandardReportingContractsReportErrorType(str, Enum):
    DATANOTSYNCED = "DataNotSynced"
    DATASETNOTAVAILABLE = "DataSetNotAvailable"
    DATASETNOTSUPPORTED = "DataSetNotSupported"
    DATASYNCFAILED = "DataSyncFailed"
    DATATYPENOTENABLED = "DataTypeNotEnabled"
    DATESOUTOFRANGE = "DatesOutOfRange"
    UNCATEGORIZEDACCOUNTS = "UncategorizedAccounts"
    VALIDATIONERROR = "ValidationError"

    def __str__(self) -> str:
        return str(self.value)
