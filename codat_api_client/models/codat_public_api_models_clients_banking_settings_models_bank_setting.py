from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_clients_banking_settings_models_bank_integration import (
        CodatPublicApiModelsClientsBankingSettingsModelsBankIntegration,
    )


T = TypeVar("T", bound="CodatPublicApiModelsClientsBankingSettingsModelsBankSetting")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsClientsBankingSettingsModelsBankSetting:
    """
    Attributes:
        name (Union[Unset, None, str]):
        source_guid (Union[Unset, str]):
        bank_integrations (Union[Unset, None, List['CodatPublicApiModelsClientsBankingSettingsModelsBankIntegration']]):
    """

    name: Union[Unset, None, str] = UNSET
    source_guid: Union[Unset, str] = UNSET
    bank_integrations: Union[
        Unset, None, List["CodatPublicApiModelsClientsBankingSettingsModelsBankIntegration"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        source_guid = self.source_guid
        bank_integrations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bank_integrations, Unset):
            if self.bank_integrations is None:
                bank_integrations = None
            else:
                bank_integrations = []
                for bank_integrations_item_data in self.bank_integrations:
                    bank_integrations_item = bank_integrations_item_data.to_dict()

                    bank_integrations.append(bank_integrations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if source_guid is not UNSET:
            field_dict["sourceGuid"] = source_guid
        if bank_integrations is not UNSET:
            field_dict["bankIntegrations"] = bank_integrations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_clients_banking_settings_models_bank_integration import (
            CodatPublicApiModelsClientsBankingSettingsModelsBankIntegration,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        source_guid = d.pop("sourceGuid", UNSET)

        bank_integrations = []
        _bank_integrations = d.pop("bankIntegrations", UNSET)
        for bank_integrations_item_data in _bank_integrations or []:
            bank_integrations_item = CodatPublicApiModelsClientsBankingSettingsModelsBankIntegration.from_dict(
                bank_integrations_item_data
            )

            bank_integrations.append(bank_integrations_item)

        codat_public_api_models_clients_banking_settings_models_bank_setting = cls(
            name=name,
            source_guid=source_guid,
            bank_integrations=bank_integrations,
        )

        return codat_public_api_models_clients_banking_settings_models_bank_setting
