from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_sync_settings_sync_setting_model import (
        CodatPublicApiModelsSyncSettingsSyncSettingModel,
    )


T = TypeVar("T", bound="CodatPublicApiModelsClientsClientSyncSettingsModel")


@define
class CodatPublicApiModelsClientsClientSyncSettingsModel:
    """
    Attributes:
        client_id (Union[Unset, str]):
        settings (Union[Unset, None, List['CodatPublicApiModelsSyncSettingsSyncSettingModel']]):
        overrides_defaults (Union[Unset, bool]):
    """

    client_id: Union[Unset, str] = UNSET
    settings: Union[Unset, None, List["CodatPublicApiModelsSyncSettingsSyncSettingModel"]] = UNSET
    overrides_defaults: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id
        settings: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.settings, Unset):
            if self.settings is None:
                settings = None
            else:
                settings = []
                for settings_item_data in self.settings:
                    settings_item = settings_item_data.to_dict()

                    settings.append(settings_item)

        overrides_defaults = self.overrides_defaults

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if settings is not UNSET:
            field_dict["settings"] = settings
        if overrides_defaults is not UNSET:
            field_dict["overridesDefaults"] = overrides_defaults

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_sync_settings_sync_setting_model import (
            CodatPublicApiModelsSyncSettingsSyncSettingModel,
        )

        d = src_dict.copy()
        client_id = d.pop("clientId", UNSET)

        settings = []
        _settings = d.pop("settings", UNSET)
        for settings_item_data in _settings or []:
            settings_item = CodatPublicApiModelsSyncSettingsSyncSettingModel.from_dict(settings_item_data)

            settings.append(settings_item)

        overrides_defaults = d.pop("overridesDefaults", UNSET)

        codat_public_api_models_clients_client_sync_settings_model = cls(
            client_id=client_id,
            settings=settings,
            overrides_defaults=overrides_defaults,
        )

        return codat_public_api_models_clients_client_sync_settings_model
