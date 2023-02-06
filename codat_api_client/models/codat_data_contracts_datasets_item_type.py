from enum import Enum


class CodatDataContractsDatasetsItemType(str, Enum):
    UNKNOWN = "Unknown"
    INVENTORY = "Inventory"
    NONINVENTORY = "NonInventory"
    SERVICE = "Service"

    def __str__(self) -> str:
        return str(self.value)
