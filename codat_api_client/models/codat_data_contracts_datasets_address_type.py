from enum import Enum


class CodatDataContractsDatasetsAddressType(str, Enum):
    BILLING = "Billing"
    DELIVERY = "Delivery"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
