from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsClientsIntegrationSettingsModel")


@define
class CodatPublicApiModelsClientsIntegrationSettingsModel:
    """
    Attributes:
        integration_id (Union[Unset, str]):
        one_time_sync (Union[Unset, None, str]):
    """

    integration_id: Union[Unset, str] = UNSET
    one_time_sync: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        integration_id = self.integration_id
        one_time_sync = self.one_time_sync

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if integration_id is not UNSET:
            field_dict["integrationId"] = integration_id
        if one_time_sync is not UNSET:
            field_dict["oneTimeSync"] = one_time_sync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        integration_id = d.pop("integrationId", UNSET)

        one_time_sync = d.pop("oneTimeSync", UNSET)

        codat_public_api_models_clients_integration_settings_model = cls(
            integration_id=integration_id,
            one_time_sync=one_time_sync,
        )

        return codat_public_api_models_clients_integration_settings_model
