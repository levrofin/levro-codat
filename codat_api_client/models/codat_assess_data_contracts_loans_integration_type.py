from enum import Enum


class CodatAssessDataContractsLoansIntegrationType(str, Enum):
    ACCOUNTING = "Accounting"
    BANKING = "Banking"
    COMMERCE = "Commerce"

    def __str__(self) -> str:
        return str(self.value)
