from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsDataDataSetPagedResponseHrefModel")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsDataDataSetPagedResponseHrefModel:
    """
    Attributes:
        href (Union[Unset, None, str]):
    """

    href: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href", UNSET)

        codat_public_api_models_data_data_set_paged_response_href_model = cls(
            href=href,
        )

        return codat_public_api_models_data_data_set_paged_response_href_model
