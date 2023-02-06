from enum import Enum


class CodatDataContractsDatasetsCommerceTransactionRefType(str, Enum):
    UNKNOWN = "Unknown"
    FEE = "Fee"
    ORDER = "Order"
    PAYMENT = "Payment"
    SERVICECHARGE = "ServiceCharge"

    def __str__(self) -> str:
        return str(self.value)
