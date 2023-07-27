from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsClientsIntegrationSettingsPatchModel")


@define
class CodatPublicApiModelsClientsIntegrationSettingsPatchModel:
    """
    Attributes:
        one_time_sync (Union[Unset, None, str]):
    """

    one_time_sync: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        one_time_sync = self.one_time_sync

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if one_time_sync is not UNSET:
            field_dict["oneTimeSync"] = one_time_sync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        one_time_sync = d.pop("oneTimeSync", UNSET)

        codat_public_api_models_clients_integration_settings_patch_model = cls(
            one_time_sync=one_time_sync,
        )

        return codat_public_api_models_clients_integration_settings_patch_model
