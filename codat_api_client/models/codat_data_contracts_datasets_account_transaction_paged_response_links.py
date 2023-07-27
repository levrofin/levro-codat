from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define, field

if TYPE_CHECKING:
    from ..models.codat_data_contracts_responses_hal_link import CodatDataContractsResponsesHalLink


T = TypeVar("T", bound="CodatDataContractsDatasetsAccountTransactionPagedResponseLinks")


@define
class CodatDataContractsDatasetsAccountTransactionPagedResponseLinks:
    """ """

    additional_properties: Dict[str, "CodatDataContractsResponsesHalLink"] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_responses_hal_link import CodatDataContractsResponsesHalLink

        d = src_dict.copy()
        codat_data_contracts_datasets_account_transaction_paged_response_links = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CodatDataContractsResponsesHalLink.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        codat_data_contracts_datasets_account_transaction_paged_response_links.additional_properties = (
            additional_properties
        )
        return codat_data_contracts_datasets_account_transaction_paged_response_links

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "CodatDataContractsResponsesHalLink":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "CodatDataContractsResponsesHalLink") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
