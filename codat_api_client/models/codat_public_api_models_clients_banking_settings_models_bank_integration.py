from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsClientsBankingSettingsModelsBankIntegration")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsClientsBankingSettingsModelsBankIntegration:
    """
    Attributes:
        name (Union[Unset, None, str]):
        integration_guid (Union[Unset, None, str]):
        selected (Union[Unset, bool]):
    """

    name: Union[Unset, None, str] = UNSET
    integration_guid: Union[Unset, None, str] = UNSET
    selected: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        integration_guid = self.integration_guid
        selected = self.selected

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if integration_guid is not UNSET:
            field_dict["integrationGuid"] = integration_guid
        if selected is not UNSET:
            field_dict["selected"] = selected

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        integration_guid = d.pop("integrationGuid", UNSET)

        selected = d.pop("selected", UNSET)

        codat_public_api_models_clients_banking_settings_models_bank_integration = cls(
            name=name,
            integration_guid=integration_guid,
            selected=selected,
        )

        return codat_public_api_models_clients_banking_settings_models_bank_integration
