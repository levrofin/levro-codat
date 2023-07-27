from enum import Enum


class CodatDataContractsDatasetsBankingBankingTransactionCode(str, Enum):
    ADJUSTMENT = "Adjustment"
    CASH = "Cash"
    CASHBACK = "Cashback"
    CHEQUE = "Cheque"
    CREDIT = "Credit"
    DIRECTDEBIT = "DirectDebit"
    FEE = "Fee"
    INTEREST = "Interest"
    NOTSUPPORTED = "NotSupported"
    OTHER = "Other"
    PAYMENT = "Payment"
    PURCHASE = "Purchase"
    STANDINGORDER = "StandingOrder"
    TRANSFER = "Transfer"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
