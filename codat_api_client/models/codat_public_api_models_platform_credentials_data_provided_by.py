from enum import Enum


class CodatPublicApiModelsPlatformCredentialsDataProvidedBy(str, Enum):
    CLIENT = "Client"
    CODAT = "Codat"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
