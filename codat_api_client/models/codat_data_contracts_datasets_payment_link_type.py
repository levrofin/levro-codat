from enum import Enum


class CodatDataContractsDatasetsPaymentLinkType(str, Enum):
    UNKNOWN = "Unknown"
    UNLINKED = "Unlinked"
    INVOICE = "Invoice"
    CREDITNOTE = "CreditNote"
    OTHER = "Other"
    REFUND = "Refund"
    PAYMENT = "Payment"
    PAYMENTONACCOUNT = "PaymentOnAccount"
    MANUALJOURNAL = "ManualJournal"
    DISCOUNT = "Discount"

    def __str__(self) -> str:
        return str(self.value)
