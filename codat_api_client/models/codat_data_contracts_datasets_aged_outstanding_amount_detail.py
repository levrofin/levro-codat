from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsAgedOutstandingAmountDetail")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsAgedOutstandingAmountDetail:
    """
    Attributes:
        name (Union[Unset, None, str]):
        amount (Union[Unset, float]):
    """

    name: Union[Unset, None, str] = UNSET
    amount: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        amount = d.pop("amount", UNSET)

        codat_data_contracts_datasets_aged_outstanding_amount_detail = cls(
            name=name,
            amount=amount,
        )

        return codat_data_contracts_datasets_aged_outstanding_amount_detail
