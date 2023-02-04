from enum import Enum


class CodatDataContractsDatasetsTransactionType(str, Enum):
    UNKNOWN = "Unknown"
    CREDIT = "Credit"
    DEBIT = "Debit"
    INT = "Int"
    DIV = "Div"
    FEE = "Fee"
    SERCHG = "SerChg"
    DEP = "Dep"
    ATM = "Atm"
    POS = "Pos"
    XFER = "Xfer"
    CHECK = "Check"
    PAYMENT = "Payment"
    CASH = "Cash"
    DIRECTDEP = "DirectDep"
    DIRECTDEBIT = "DirectDebit"
    REPEATPMT = "RepeatPmt"
    OTHER = "Other"

    def __str__(self) -> str:
        return str(self.value)
