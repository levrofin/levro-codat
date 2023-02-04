from enum import Enum


class CodatDataContractsDatasetsCommerceDisputeStatus(str, Enum):
    UNKNOWN = "Unknown"
    WON = "Won"
    LOST = "Lost"
    ACCEPTED = "Accepted"
    PROCESSING = "Processing"
    CHARGEREFUNDED = "ChargeRefunded"
    EVIDENCEREQUIRED = "EvidenceRequired"
    INQUIRYEVIDENCEREQUIRED = "InquiryEvidenceRequired"
    INQUIRYPROCESSING = "InquiryProcessing"
    INQUIRYCLOSED = "InquiryClosed"
    WAITINGTHIRDPARTY = "WaitingThirdParty"

    def __str__(self) -> str:
        return str(self.value)
