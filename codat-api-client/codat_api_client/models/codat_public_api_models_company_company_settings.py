from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="CodatPublicApiModelsCompanyCompanySettings")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsCompanyCompanySettings:
    """
    Attributes:
        company_id (str):
        offline_connector_install (bool):
    """

    company_id: str
    offline_connector_install: bool

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        offline_connector_install = self.offline_connector_install

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "companyId": company_id,
                "offlineConnectorInstall": offline_connector_install,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        company_id = d.pop("companyId")

        offline_connector_install = d.pop("offlineConnectorInstall")

        codat_public_api_models_company_company_settings = cls(
            company_id=company_id,
            offline_connector_install=offline_connector_install,
        )

        return codat_public_api_models_company_company_settings
