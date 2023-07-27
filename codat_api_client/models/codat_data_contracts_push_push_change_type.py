from enum import Enum


class CodatDataContractsPushPushChangeType(str, Enum):
    ATTACHMENTUPLOADED = "AttachmentUploaded"
    CREATED = "Created"
    DELETED = "Deleted"
    MODIFIED = "Modified"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
