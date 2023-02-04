from enum import Enum


class CodatDataContractsDatasetsCommercePaymentType(str, Enum):
    UNKNOWN = "Unknown"
    CASH = "Cash"
    CARD = "Card"
    INVOICE = "Invoice"
    ONLINECARD = "OnlineCard"
    SWISH = "Swish"
    VIPPS = "Vipps"
    MOBILE = "Mobile"
    STORECREDIT = "StoreCredit"
    PAYPAL = "Paypal"
    CUSTOM = "Custom"
    PREPAID = "Prepaid"

    def __str__(self) -> str:
        return str(self.value)
