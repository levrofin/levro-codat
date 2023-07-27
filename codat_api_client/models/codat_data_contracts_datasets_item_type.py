from enum import Enum


class CodatDataContractsDatasetsItemType(str, Enum):
    INVENTORY = "Inventory"
    NONINVENTORY = "NonInventory"
    SERVICE = "Service"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
