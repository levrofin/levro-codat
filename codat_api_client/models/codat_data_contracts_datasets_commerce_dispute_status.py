from enum import Enum


class CodatDataContractsDatasetsCommerceDisputeStatus(str, Enum):
    ACCEPTED = "Accepted"
    CHARGEREFUNDED = "ChargeRefunded"
    EVIDENCEREQUIRED = "EvidenceRequired"
    INQUIRYCLOSED = "InquiryClosed"
    INQUIRYEVIDENCEREQUIRED = "InquiryEvidenceRequired"
    INQUIRYPROCESSING = "InquiryProcessing"
    LOST = "Lost"
    PROCESSING = "Processing"
    UNKNOWN = "Unknown"
    WAITINGTHIRDPARTY = "WaitingThirdParty"
    WON = "Won"

    def __str__(self) -> str:
        return str(self.value)
