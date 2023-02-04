from enum import Enum


class CodatDataContractsDatasetsBankingBankingTransactionCode(str, Enum):
    UNKNOWN = "Unknown"
    FEE = "Fee"
    PAYMENT = "Payment"
    CASH = "Cash"
    TRANSFER = "Transfer"
    INTEREST = "Interest"
    CASHBACK = "Cashback"
    CHEQUE = "Cheque"
    DIRECTDEBIT = "DirectDebit"
    PURCHASE = "Purchase"
    STANDINGORDER = "StandingOrder"
    ADJUSTMENT = "Adjustment"
    CREDIT = "Credit"
    OTHER = "Other"
    NOTSUPPORTED = "NotSupported"

    def __str__(self) -> str:
        return str(self.value)
