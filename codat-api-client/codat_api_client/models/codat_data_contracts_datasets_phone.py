from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.codat_data_contracts_datasets_phone_type import CodatDataContractsDatasetsPhoneType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsPhone")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsPhone:
    """
    Attributes:
        type (CodatDataContractsDatasetsPhoneType):
        number (Union[Unset, None, str]):
    """

    type: CodatDataContractsDatasetsPhoneType
    number: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        number = self.number

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = CodatDataContractsDatasetsPhoneType(d.pop("type"))

        number = d.pop("number", UNSET)

        codat_data_contracts_datasets_phone = cls(
            type=type,
            number=number,
        )

        return codat_data_contracts_datasets_phone
