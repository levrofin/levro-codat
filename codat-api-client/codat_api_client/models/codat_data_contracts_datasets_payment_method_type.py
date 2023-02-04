from enum import Enum


class CodatDataContractsDatasetsPaymentMethodType(str, Enum):
    UNKNOWN = "Unknown"
    CASH = "Cash"
    CHECK = "Check"
    CREDITCARD = "CreditCard"
    DEBITCARD = "DebitCard"
    BANKTRANSFER = "BankTransfer"
    OTHER = "Other"

    def __str__(self) -> str:
        return str(self.value)
