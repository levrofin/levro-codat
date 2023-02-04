from enum import Enum


class CodatDataContractsDatasetsCommerceServiceChargeType(str, Enum):
    UNKNOWN = "Unknown"
    GENERIC = "Generic"
    SHIPPING = "Shipping"
    OVERPAYMENT = "Overpayment"

    def __str__(self) -> str:
        return str(self.value)
