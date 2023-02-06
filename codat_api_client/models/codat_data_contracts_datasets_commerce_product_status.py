from enum import Enum


class CodatDataContractsDatasetsCommerceProductStatus(str, Enum):
    UNKNOWN = "Unknown"
    PUBLISHED = "Published"
    UNPUBLISHED = "Unpublished"

    def __str__(self) -> str:
        return str(self.value)
