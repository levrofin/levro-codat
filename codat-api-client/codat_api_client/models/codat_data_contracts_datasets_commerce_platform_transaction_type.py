from enum import Enum


class CodatDataContractsDatasetsCommercePlatformTransactionType(str, Enum):
    UNKNOWN = "Unknown"
    PAYMENT = "Payment"
    REFUND = "Refund"
    PAYOUT = "Payout"
    FAILEDPAYOUT = "FailedPayout"
    TRANSFER = "Transfer"
    PAYMENTFEE = "PaymentFee"
    PAYMENTFEEREFUND = "PaymentFeeRefund"

    def __str__(self) -> str:
        return str(self.value)
