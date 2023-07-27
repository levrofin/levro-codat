from enum import Enum


class CodatDataContractsDatasetsCommerceServiceChargeType(str, Enum):
    GENERIC = "Generic"
    OVERPAYMENT = "Overpayment"
    SHIPPING = "Shipping"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
