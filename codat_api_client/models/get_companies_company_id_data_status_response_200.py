from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.codat_public_api_models_data_data_status import CodatPublicApiModelsDataDataStatus


T = TypeVar("T", bound="GetCompaniesCompanyIdDataStatusResponse200")


@attr.s(auto_attribs=True)
class GetCompaniesCompanyIdDataStatusResponse200:
    """ """

    additional_properties: Dict[str, "CodatPublicApiModelsDataDataStatus"] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_data_data_status import CodatPublicApiModelsDataDataStatus

        d = src_dict.copy()
        get_companies_company_id_data_status_response_200 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CodatPublicApiModelsDataDataStatus.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_companies_company_id_data_status_response_200.additional_properties = additional_properties
        return get_companies_company_id_data_status_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "CodatPublicApiModelsDataDataStatus":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "CodatPublicApiModelsDataDataStatus") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
