from enum import Enum


class CodatDataContractsDatasetsPaymentMethodType(str, Enum):
    BANKTRANSFER = "BankTransfer"
    CASH = "Cash"
    CHECK = "Check"
    CREDITCARD = "CreditCard"
    DEBITCARD = "DebitCard"
    OTHER = "Other"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
