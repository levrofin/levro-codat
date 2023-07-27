from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_clients_api_client_contract_sync_setting import CodatClientsApiClientContractSyncSetting


T = TypeVar("T", bound="CodatClientsApiClientContractCompanySyncSettings")


@define
class CodatClientsApiClientContractCompanySyncSettings:
    """
    Attributes:
        company_id (Union[Unset, str]):
        settings (Union[Unset, None, List['CodatClientsApiClientContractSyncSetting']]):
        overrides_defaults (Union[Unset, bool]):
    """

    company_id: Union[Unset, str] = UNSET
    settings: Union[Unset, None, List["CodatClientsApiClientContractSyncSetting"]] = UNSET
    overrides_defaults: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
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
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if settings is not UNSET:
            field_dict["settings"] = settings
        if overrides_defaults is not UNSET:
            field_dict["overridesDefaults"] = overrides_defaults

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_clients_api_client_contract_sync_setting import CodatClientsApiClientContractSyncSetting

        d = src_dict.copy()
        company_id = d.pop("companyId", UNSET)

        settings = []
        _settings = d.pop("settings", UNSET)
        for settings_item_data in _settings or []:
            settings_item = CodatClientsApiClientContractSyncSetting.from_dict(settings_item_data)

            settings.append(settings_item)

        overrides_defaults = d.pop("overridesDefaults", UNSET)

        codat_clients_api_client_contract_company_sync_settings = cls(
            company_id=company_id,
            settings=settings,
            overrides_defaults=overrides_defaults,
        )

        return codat_clients_api_client_contract_company_sync_settings
