from enum import Enum


class CodatDataContractsDatasetsBillPaymentLinkType(str, Enum):
    BILL = "Bill"
    BILLPAYMENT = "BillPayment"
    CREDITNOTE = "CreditNote"
    DISCOUNT = "Discount"
    MANUALJOURNAL = "ManualJournal"
    OTHER = "Other"
    PAYMENTONACCOUNT = "PaymentOnAccount"
    REFUND = "Refund"
    UNKNOWN = "Unknown"
    UNLINKED = "Unlinked"

    def __str__(self) -> str:
        return str(self.value)
