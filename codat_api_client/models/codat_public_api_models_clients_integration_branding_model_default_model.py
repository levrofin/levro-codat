from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_clients_integration_branding_model_image_model import (
        CodatPublicApiModelsClientsIntegrationBrandingModelImageModel,
    )


T = TypeVar("T", bound="CodatPublicApiModelsClientsIntegrationBrandingModelDefaultModel")


@define
class CodatPublicApiModelsClientsIntegrationBrandingModelDefaultModel:
    """
    Attributes:
        image (Union[Unset, CodatPublicApiModelsClientsIntegrationBrandingModelImageModel]):
    """

    image: Union[Unset, "CodatPublicApiModelsClientsIntegrationBrandingModelImageModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_clients_integration_branding_model_image_model import (
            CodatPublicApiModelsClientsIntegrationBrandingModelImageModel,
        )

        d = src_dict.copy()
        _image = d.pop("image", UNSET)
        image: Union[Unset, CodatPublicApiModelsClientsIntegrationBrandingModelImageModel]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = CodatPublicApiModelsClientsIntegrationBrandingModelImageModel.from_dict(_image)

        codat_public_api_models_clients_integration_branding_model_default_model = cls(
            image=image,
        )

        return codat_public_api_models_clients_integration_branding_model_default_model
