from enum import Enum


class CodatPublicApiModelsPlatformCredentialsIntegrationSupportedEnvironments(str, Enum):
    LIVEANDSANDBOX = "LiveAndSandbox"
    LIVEONLY = "LiveOnly"
    SANDBOXONLY = "SandboxOnly"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
