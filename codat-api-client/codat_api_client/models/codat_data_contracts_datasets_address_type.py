from enum import Enum


class CodatDataContractsDatasetsAddressType(str, Enum):
    UNKNOWN = "Unknown"
    BILLING = "Billing"
    DELIVERY = "Delivery"

    def __str__(self) -> str:
        return str(self.value)
