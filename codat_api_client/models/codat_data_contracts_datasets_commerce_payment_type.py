from enum import Enum


class CodatDataContractsDatasetsCommercePaymentType(str, Enum):
    CARD = "Card"
    CASH = "Cash"
    CUSTOM = "Custom"
    INVOICE = "Invoice"
    MOBILE = "Mobile"
    ONLINECARD = "OnlineCard"
    PAYPAL = "Paypal"
    PREPAID = "Prepaid"
    STORECREDIT = "StoreCredit"
    SWISH = "Swish"
    UNKNOWN = "Unknown"
    VIPPS = "Vipps"

    def __str__(self) -> str:
        return str(self.value)
