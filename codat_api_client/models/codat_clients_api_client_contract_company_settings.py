from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatClientsApiClientContractCompanySettings")


@define
class CodatClientsApiClientContractCompanySettings:
    """
    Attributes:
        company_id (Union[Unset, str]):
        offline_connector_install (Union[Unset, None, bool]):
        one_time_sync (Union[Unset, None, str]):
    """

    company_id: Union[Unset, str] = UNSET
    offline_connector_install: Union[Unset, None, bool] = UNSET
    one_time_sync: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        offline_connector_install = self.offline_connector_install
        one_time_sync = self.one_time_sync

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if offline_connector_install is not UNSET:
            field_dict["offlineConnectorInstall"] = offline_connector_install
        if one_time_sync is not UNSET:
            field_dict["oneTimeSync"] = one_time_sync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        company_id = d.pop("companyId", UNSET)

        offline_connector_install = d.pop("offlineConnectorInstall", UNSET)

        one_time_sync = d.pop("oneTimeSync", UNSET)

        codat_clients_api_client_contract_company_settings = cls(
            company_id=company_id,
            offline_connector_install=offline_connector_install,
            one_time_sync=one_time_sync,
        )

        return codat_clients_api_client_contract_company_settings
