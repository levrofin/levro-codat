from enum import Enum


class CodatDataContractsDatasetsCommercePaymentStatus(str, Enum):
    UNKNOWN = "Unknown"
    PENDING = "Pending"
    AUTHORIZED = "Authorized"
    PAID = "Paid"
    FAILED = "Failed"
    CANCELLED = "Cancelled"

    def __str__(self) -> str:
        return str(self.value)
