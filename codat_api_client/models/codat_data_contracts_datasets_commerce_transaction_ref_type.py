from enum import Enum


class CodatDataContractsDatasetsCommerceTransactionRefType(str, Enum):
    FEE = "Fee"
    ORDER = "Order"
    PAYMENT = "Payment"
    SERVICECHARGE = "ServiceCharge"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
