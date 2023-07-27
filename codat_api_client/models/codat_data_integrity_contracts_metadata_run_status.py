from enum import Enum


class CodatDataIntegrityContractsMetadataRunStatus(str, Enum):
    COMPLETE = "Complete"
    COMPLETEWITHWARNING = "CompleteWithWarning"
    DOESNOTEXIST = "DoesNotExist"
    ERROR = "Error"
    PROCESSING = "Processing"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
