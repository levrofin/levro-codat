from enum import Enum


class CodatDataContractsDatasetsBillPaymentLinkType(str, Enum):
    UNKNOWN = "Unknown"
    UNLINKED = "Unlinked"
    BILL = "Bill"
    OTHER = "Other"
    CREDITNOTE = "CreditNote"
    BILLPAYMENT = "BillPayment"
    PAYMENTONACCOUNT = "PaymentOnAccount"
    REFUND = "Refund"
    MANUALJOURNAL = "ManualJournal"
    DISCOUNT = "Discount"

    def __str__(self) -> str:
        return str(self.value)
