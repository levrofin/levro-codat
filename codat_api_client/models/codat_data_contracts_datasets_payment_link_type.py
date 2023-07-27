from enum import Enum


class CodatDataContractsDatasetsPaymentLinkType(str, Enum):
    CREDITNOTE = "CreditNote"
    DISCOUNT = "Discount"
    INVOICE = "Invoice"
    MANUALJOURNAL = "ManualJournal"
    OTHER = "Other"
    PAYMENT = "Payment"
    PAYMENTONACCOUNT = "PaymentOnAccount"
    REFUND = "Refund"
    UNKNOWN = "Unknown"
    UNLINKED = "Unlinked"

    def __str__(self) -> str:
        return str(self.value)
