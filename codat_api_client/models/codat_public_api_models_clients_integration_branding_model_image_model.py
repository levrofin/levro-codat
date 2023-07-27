from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsClientsIntegrationBrandingModelImageModel")


@define
class CodatPublicApiModelsClientsIntegrationBrandingModelImageModel:
    """
    Attributes:
        src (Union[Unset, None, str]):
        alt (Union[Unset, None, str]):
    """

    src: Union[Unset, None, str] = UNSET
    alt: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        src = self.src
        alt = self.alt

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if src is not UNSET:
            field_dict["src"] = src
        if alt is not UNSET:
            field_dict["alt"] = alt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        src = d.pop("src", UNSET)

        alt = d.pop("alt", UNSET)

        codat_public_api_models_clients_integration_branding_model_image_model = cls(
            src=src,
            alt=alt,
        )

        return codat_public_api_models_clients_integration_branding_model_image_model
