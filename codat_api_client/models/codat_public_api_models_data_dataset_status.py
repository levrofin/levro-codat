from enum import Enum


class CodatPublicApiModelsDataDatasetStatus(str, Enum):
    AUTHERROR = "AuthError"
    CANCELLED = "Cancelled"
    COMPLETE = "Complete"
    FETCHERROR = "FetchError"
    FETCHING = "Fetching"
    INITIAL = "Initial"
    INTERNALERROR = "InternalError"
    MAPERROR = "MapError"
    MAPPING = "Mapping"
    MAPQUEUED = "MapQueued"
    NOTSUPPORTED = "NotSupported"
    PERMISSIONSERROR = "PermissionsError"
    PREREQUISITENOTMET = "PrerequisiteNotMet"
    PROCESSING = "Processing"
    PROCESSINGERROR = "ProcessingError"
    PROCESSINGQUEUED = "ProcessingQueued"
    QUEUED = "Queued"
    RATELIMITERROR = "RateLimitError"
    VALIDATING = "Validating"
    VALIDATIONERROR = "ValidationError"
    VALIDATIONQUEUED = "ValidationQueued"

    def __str__(self) -> str:
        return str(self.value)
