from enum import Enum


class CodatDataContractsDatasetsCommerceProductStatus(str, Enum):
    PUBLISHED = "Published"
    UNKNOWN = "Unknown"
    UNPUBLISHED = "Unpublished"

    def __str__(self) -> str:
        return str(self.value)
