from enum import Enum


class CodatPublicApiModelsPlatformCredentialsSourceType(str, Enum):
    UNKNOWN = "Unknown"
    ACCOUNTING = "Accounting"
    BANKING = "Banking"
    BANKFEED = "BankFeed"
    COMMERCE = "Commerce"
    EXPENSE = "Expense"
    OTHER = "Other"

    def __str__(self) -> str:
        return str(self.value)
