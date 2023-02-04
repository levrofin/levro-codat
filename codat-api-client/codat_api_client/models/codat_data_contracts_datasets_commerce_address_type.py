from enum import Enum


class CodatDataContractsDatasetsCommerceAddressType(str, Enum):
    UNKNOWN = "Unknown"
    BILLING = "Billing"
    DELIVERY = "Delivery"
    ORDER = "Order"
    INVENTORY = "Inventory"

    def __str__(self) -> str:
        return str(self.value)
