from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_clients_integration_branding_model_full_model import (
        CodatPublicApiModelsClientsIntegrationBrandingModelFullModel,
    )
    from ..models.codat_public_api_models_clients_integration_branding_model_square_model import (
        CodatPublicApiModelsClientsIntegrationBrandingModelSquareModel,
    )


T = TypeVar("T", bound="CodatPublicApiModelsClientsIntegrationBrandingModelLogoModel")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsClientsIntegrationBrandingModelLogoModel:
    """
    Attributes:
        full (Union[Unset, CodatPublicApiModelsClientsIntegrationBrandingModelFullModel]):
        square (Union[Unset, CodatPublicApiModelsClientsIntegrationBrandingModelSquareModel]):
    """

    full: Union[Unset, "CodatPublicApiModelsClientsIntegrationBrandingModelFullModel"] = UNSET
    square: Union[Unset, "CodatPublicApiModelsClientsIntegrationBrandingModelSquareModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        full: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.full, Unset):
            full = self.full.to_dict()

        square: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.square, Unset):
            square = self.square.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if full is not UNSET:
            field_dict["full"] = full
        if square is not UNSET:
            field_dict["square"] = square

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_clients_integration_branding_model_full_model import (
            CodatPublicApiModelsClientsIntegrationBrandingModelFullModel,
        )
        from ..models.codat_public_api_models_clients_integration_branding_model_square_model import (
            CodatPublicApiModelsClientsIntegrationBrandingModelSquareModel,
        )

        d = src_dict.copy()
        _full = d.pop("full", UNSET)
        full: Union[Unset, CodatPublicApiModelsClientsIntegrationBrandingModelFullModel]
        if isinstance(_full, Unset):
            full = UNSET
        else:
            full = CodatPublicApiModelsClientsIntegrationBrandingModelFullModel.from_dict(_full)

        _square = d.pop("square", UNSET)
        square: Union[Unset, CodatPublicApiModelsClientsIntegrationBrandingModelSquareModel]
        if isinstance(_square, Unset):
            square = UNSET
        else:
            square = CodatPublicApiModelsClientsIntegrationBrandingModelSquareModel.from_dict(_square)

        codat_public_api_models_clients_integration_branding_model_logo_model = cls(
            full=full,
            square=square,
        )

        return codat_public_api_models_clients_integration_branding_model_logo_model
