from enum import Enum


class CodatDataContractsPushOptionType(str, Enum):
    ARRAY = "Array"
    OBJECT = "Object"
    STRING = "String"
    NUMBER = "Number"
    BOOLEAN = "Boolean"
    DATETIME = "DateTime"
    FILE = "File"
    MULTIPART = "MultiPart"

    def __str__(self) -> str:
        return str(self.value)
