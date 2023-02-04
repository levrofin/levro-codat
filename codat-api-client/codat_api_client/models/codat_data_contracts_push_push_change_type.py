from enum import Enum


class CodatDataContractsPushPushChangeType(str, Enum):
    UNKNOWN = "Unknown"
    CREATED = "Created"
    MODIFIED = "Modified"
    DELETED = "Deleted"
    ATTACHMENTUPLOADED = "AttachmentUploaded"

    def __str__(self) -> str:
        return str(self.value)
