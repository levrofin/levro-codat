from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsDataValidDatatypeLinksResponse")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsDataValidDatatypeLinksResponse:
    """
    Attributes:
        property_ (Union[Unset, None, str]):
        links (Union[Unset, None, List[str]]):
    """

    property_: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        property_ = self.property_
        links: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.links, Unset):
            if self.links is None:
                links = None
            else:
                links = self.links

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if property_ is not UNSET:
            field_dict["property"] = property_
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        property_ = d.pop("property", UNSET)

        links = cast(List[str], d.pop("links", UNSET))

        codat_public_api_models_data_valid_datatype_links_response = cls(
            property_=property_,
            links=links,
        )

        return codat_public_api_models_data_valid_datatype_links_response
