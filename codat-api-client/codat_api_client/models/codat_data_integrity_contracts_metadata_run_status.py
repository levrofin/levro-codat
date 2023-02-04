from enum import Enum


class CodatDataIntegrityContractsMetadataRunStatus(str, Enum):
    UNKNOWN = "Unknown"
    DOESNOTEXIST = "DoesNotExist"
    ERROR = "Error"
    PROCESSING = "Processing"
    COMPLETEWITHWARNING = "CompleteWithWarning"
    COMPLETE = "Complete"

    def __str__(self) -> str:
        return str(self.value)
