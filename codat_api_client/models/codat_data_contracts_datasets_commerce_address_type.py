from enum import Enum


class CodatDataContractsDatasetsCommerceAddressType(str, Enum):
    BILLING = "Billing"
    DELIVERY = "Delivery"
    INVENTORY = "Inventory"
    ORDER = "Order"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
