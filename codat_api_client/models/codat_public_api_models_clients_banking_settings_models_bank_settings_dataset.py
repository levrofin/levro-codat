from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_clients_banking_settings_models_bank_setting import (
        CodatPublicApiModelsClientsBankingSettingsModelsBankSetting,
    )


T = TypeVar("T", bound="CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset")


@define
class CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset:
    """
    Attributes:
        bank_settings (Union[Unset, None, List['CodatPublicApiModelsClientsBankingSettingsModelsBankSetting']]):
    """

    bank_settings: Union[Unset, None, List["CodatPublicApiModelsClientsBankingSettingsModelsBankSetting"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        bank_settings: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bank_settings, Unset):
            if self.bank_settings is None:
                bank_settings = None
            else:
                bank_settings = []
                for bank_settings_item_data in self.bank_settings:
                    bank_settings_item = bank_settings_item_data.to_dict()

                    bank_settings.append(bank_settings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if bank_settings is not UNSET:
            field_dict["bankSettings"] = bank_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_clients_banking_settings_models_bank_setting import (
            CodatPublicApiModelsClientsBankingSettingsModelsBankSetting,
        )

        d = src_dict.copy()
        bank_settings = []
        _bank_settings = d.pop("bankSettings", UNSET)
        for bank_settings_item_data in _bank_settings or []:
            bank_settings_item = CodatPublicApiModelsClientsBankingSettingsModelsBankSetting.from_dict(
                bank_settings_item_data
            )

            bank_settings.append(bank_settings_item)

        codat_public_api_models_clients_banking_settings_models_bank_settings_dataset = cls(
            bank_settings=bank_settings,
        )

        return codat_public_api_models_clients_banking_settings_models_bank_settings_dataset
