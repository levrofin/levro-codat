from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.codat_data_contracts_datasets_web_link_type import CodatDataContractsDatasetsWebLinkType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsWebLink")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsWebLink:
    """
    Attributes:
        type (CodatDataContractsDatasetsWebLinkType):
        url (Union[Unset, None, str]):
    """

    type: CodatDataContractsDatasetsWebLinkType
    url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = CodatDataContractsDatasetsWebLinkType(d.pop("type"))

        url = d.pop("url", UNSET)

        codat_data_contracts_datasets_web_link = cls(
            type=type,
            url=url,
        )

        return codat_data_contracts_datasets_web_link
