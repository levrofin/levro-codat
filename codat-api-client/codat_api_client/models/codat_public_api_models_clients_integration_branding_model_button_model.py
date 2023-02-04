from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_clients_integration_branding_model_default_model import (
        CodatPublicApiModelsClientsIntegrationBrandingModelDefaultModel,
    )
    from ..models.codat_public_api_models_clients_integration_branding_model_hover_model import (
        CodatPublicApiModelsClientsIntegrationBrandingModelHoverModel,
    )


T = TypeVar("T", bound="CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel:
    """
    Attributes:
        default (Union[Unset, CodatPublicApiModelsClientsIntegrationBrandingModelDefaultModel]):
        hover (Union[Unset, CodatPublicApiModelsClientsIntegrationBrandingModelHoverModel]):
    """

    default: Union[Unset, "CodatPublicApiModelsClientsIntegrationBrandingModelDefaultModel"] = UNSET
    hover: Union[Unset, "CodatPublicApiModelsClientsIntegrationBrandingModelHoverModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        default: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default, Unset):
            default = self.default.to_dict()

        hover: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hover, Unset):
            hover = self.hover.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if default is not UNSET:
            field_dict["default"] = default
        if hover is not UNSET:
            field_dict["hover"] = hover

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_clients_integration_branding_model_default_model import (
            CodatPublicApiModelsClientsIntegrationBrandingModelDefaultModel,
        )
        from ..models.codat_public_api_models_clients_integration_branding_model_hover_model import (
            CodatPublicApiModelsClientsIntegrationBrandingModelHoverModel,
        )

        d = src_dict.copy()
        _default = d.pop("default", UNSET)
        default: Union[Unset, CodatPublicApiModelsClientsIntegrationBrandingModelDefaultModel]
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = CodatPublicApiModelsClientsIntegrationBrandingModelDefaultModel.from_dict(_default)

        _hover = d.pop("hover", UNSET)
        hover: Union[Unset, CodatPublicApiModelsClientsIntegrationBrandingModelHoverModel]
        if isinstance(_hover, Unset):
            hover = UNSET
        else:
            hover = CodatPublicApiModelsClientsIntegrationBrandingModelHoverModel.from_dict(_hover)

        codat_public_api_models_clients_integration_branding_model_button_model = cls(
            default=default,
            hover=hover,
        )

        return codat_public_api_models_clients_integration_branding_model_button_model
