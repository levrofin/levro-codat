from enum import Enum


class CodatDataContractsDatasetsCommercePaymentStatus(str, Enum):
    AUTHORIZED = "Authorized"
    CANCELLED = "Cancelled"
    FAILED = "Failed"
    PAID = "Paid"
    PENDING = "Pending"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
