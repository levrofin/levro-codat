from enum import Enum


class CodatDataContractsDatasetsTransactionType(str, Enum):
    ATM = "Atm"
    CASH = "Cash"
    CHECK = "Check"
    CREDIT = "Credit"
    DEBIT = "Debit"
    DEP = "Dep"
    DIRECTDEBIT = "DirectDebit"
    DIRECTDEP = "DirectDep"
    DIV = "Div"
    FEE = "Fee"
    INT = "Int"
    OTHER = "Other"
    PAYMENT = "Payment"
    POS = "Pos"
    REPEATPMT = "RepeatPmt"
    SERCHG = "SerChg"
    UNKNOWN = "Unknown"
    XFER = "Xfer"

    def __str__(self) -> str:
        return str(self.value)
