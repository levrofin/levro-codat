from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsBillPaymentPagedResponseHrefModel")


@define
class CodatDataContractsDatasetsBillPaymentPagedResponseHrefModel:
    """
    Attributes:
        href (Union[Unset, None, str]):
    """

    href: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href", UNSET)

        codat_data_contracts_datasets_bill_payment_paged_response_href_model = cls(
            href=href,
        )

        return codat_data_contracts_datasets_bill_payment_paged_response_href_model
