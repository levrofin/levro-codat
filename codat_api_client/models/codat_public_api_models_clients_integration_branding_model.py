from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_clients_integration_branding_model_button_model import (
        CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel,
    )
    from ..models.codat_public_api_models_clients_integration_branding_model_logo_model import (
        CodatPublicApiModelsClientsIntegrationBrandingModelLogoModel,
    )


T = TypeVar("T", bound="CodatPublicApiModelsClientsIntegrationBrandingModel")


@define
class CodatPublicApiModelsClientsIntegrationBrandingModel:
    """
    Attributes:
        logo (Union[Unset, CodatPublicApiModelsClientsIntegrationBrandingModelLogoModel]):
        button (Union[Unset, CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel]):
        source_id (Union[Unset, str]):
    """

    logo: Union[Unset, "CodatPublicApiModelsClientsIntegrationBrandingModelLogoModel"] = UNSET
    button: Union[Unset, "CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel"] = UNSET
    source_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        logo: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.logo, Unset):
            logo = self.logo.to_dict()

        button: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.button, Unset):
            button = self.button.to_dict()

        source_id = self.source_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if logo is not UNSET:
            field_dict["logo"] = logo
        if button is not UNSET:
            field_dict["button"] = button
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_clients_integration_branding_model_button_model import (
            CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel,
        )
        from ..models.codat_public_api_models_clients_integration_branding_model_logo_model import (
            CodatPublicApiModelsClientsIntegrationBrandingModelLogoModel,
        )

        d = src_dict.copy()
        _logo = d.pop("logo", UNSET)
        logo: Union[Unset, CodatPublicApiModelsClientsIntegrationBrandingModelLogoModel]
        if isinstance(_logo, Unset):
            logo = UNSET
        else:
            logo = CodatPublicApiModelsClientsIntegrationBrandingModelLogoModel.from_dict(_logo)

        _button = d.pop("button", UNSET)
        button: Union[Unset, CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel]
        if isinstance(_button, Unset):
            button = UNSET
        else:
            button = CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel.from_dict(_button)

        source_id = d.pop("sourceId", UNSET)

        codat_public_api_models_clients_integration_branding_model = cls(
            logo=logo,
            button=button,
            source_id=source_id,
        )

        return codat_public_api_models_clients_integration_branding_model
