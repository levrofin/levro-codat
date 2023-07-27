from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..models.codat_data_contracts_datasets_commerce_web_link_type import CodatDataContractsDatasetsCommerceWebLinkType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceWebLink")


@define
class CodatDataContractsDatasetsCommerceWebLink:
    """
    Attributes:
        type (Union[Unset, CodatDataContractsDatasetsCommerceWebLinkType]):
        url (Union[Unset, None, str]):
    """

    type: Union[Unset, CodatDataContractsDatasetsCommerceWebLinkType] = UNSET
    url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, CodatDataContractsDatasetsCommerceWebLinkType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodatDataContractsDatasetsCommerceWebLinkType(_type)

        url = d.pop("url", UNSET)

        codat_data_contracts_datasets_commerce_web_link = cls(
            type=type,
            url=url,
        )

        return codat_data_contracts_datasets_commerce_web_link
