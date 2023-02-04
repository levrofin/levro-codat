from enum import Enum


class CodatPublicApiModelsPlatformCredentialsIntegrationSupportedEnvironments(str, Enum):
    UNKNOWN = "Unknown"
    SANDBOXONLY = "SandboxOnly"
    LIVEONLY = "LiveOnly"
    LIVEANDSANDBOX = "LiveAndSandbox"

    def __str__(self) -> str:
        return str(self.value)
