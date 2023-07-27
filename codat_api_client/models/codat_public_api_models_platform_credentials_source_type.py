from enum import Enum


class CodatPublicApiModelsPlatformCredentialsSourceType(str, Enum):
    ACCOUNTING = "Accounting"
    BANKFEED = "BankFeed"
    BANKING = "Banking"
    COMMERCE = "Commerce"
    EXPENSE = "Expense"
    OTHER = "Other"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
