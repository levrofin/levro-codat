from enum import Enum


class CodatPublicApiModelsPlatformCredentialsDataProvidedBy(str, Enum):
    UNKNOWN = "Unknown"
    CODAT = "Codat"
    CLIENT = "Client"

    def __str__(self) -> str:
        return str(self.value)
