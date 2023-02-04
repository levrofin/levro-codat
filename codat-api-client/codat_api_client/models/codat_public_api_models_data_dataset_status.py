from enum import Enum


class CodatPublicApiModelsDataDatasetStatus(str, Enum):
    INITIAL = "Initial"
    QUEUED = "Queued"
    FETCHING = "Fetching"
    MAPQUEUED = "MapQueued"
    MAPPING = "Mapping"
    COMPLETE = "Complete"
    FETCHERROR = "FetchError"
    MAPERROR = "MapError"
    INTERNALERROR = "InternalError"
    PROCESSINGQUEUED = "ProcessingQueued"
    PROCESSING = "Processing"
    PROCESSINGERROR = "ProcessingError"
    VALIDATIONQUEUED = "ValidationQueued"
    VALIDATING = "Validating"
    VALIDATIONERROR = "ValidationError"
    AUTHERROR = "AuthError"
    CANCELLED = "Cancelled"
    NOTSUPPORTED = "NotSupported"
    RATELIMITERROR = "RateLimitError"
    PERMISSIONSERROR = "PermissionsError"
    PREREQUISITENOTMET = "PrerequisiteNotMet"

    def __str__(self) -> str:
        return str(self.value)
