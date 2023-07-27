from enum import Enum


class CodatDataContractsDatasetsCommercePlatformTransactionType(str, Enum):
    FAILEDPAYOUT = "FailedPayout"
    PAYMENT = "Payment"
    PAYMENTFEE = "PaymentFee"
    PAYMENTFEEREFUND = "PaymentFeeRefund"
    PAYOUT = "Payout"
    REFUND = "Refund"
    TRANSFER = "Transfer"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
