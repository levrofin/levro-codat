from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.codat_data_contracts_datasets_commerce_phone_type import CodatDataContractsDatasetsCommercePhoneType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsCommercePhone")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCommercePhone:
    """
    Attributes:
        number (Union[Unset, None, str]):
        type (Union[Unset, CodatDataContractsDatasetsCommercePhoneType]):
    """

    number: Union[Unset, None, str] = UNSET
    type: Union[Unset, CodatDataContractsDatasetsCommercePhoneType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CodatDataContractsDatasetsCommercePhoneType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodatDataContractsDatasetsCommercePhoneType(_type)

        codat_data_contracts_datasets_commerce_phone = cls(
            number=number,
            type=type,
        )

        return codat_data_contracts_datasets_commerce_phone
