from enum import Enum


class CodatDataContractsPushOptionType(str, Enum):
    ARRAY = "Array"
    BOOLEAN = "Boolean"
    DATETIME = "DateTime"
    FILE = "File"
    MULTIPART = "MultiPart"
    NUMBER = "Number"
    OBJECT = "Object"
    STRING = "String"

    def __str__(self) -> str:
        return str(self.value)
