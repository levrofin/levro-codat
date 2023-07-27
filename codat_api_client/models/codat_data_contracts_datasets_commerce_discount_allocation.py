from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceDiscountAllocation")


@define
class CodatDataContractsDatasetsCommerceDiscountAllocation:
    """
    Attributes:
        name (Union[Unset, None, str]):
        total_amount (Union[Unset, float]):
    """

    name: Union[Unset, None, str] = UNSET
    total_amount: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        total_amount = self.total_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        codat_data_contracts_datasets_commerce_discount_allocation = cls(
            name=name,
            total_amount=total_amount,
        )

        return codat_data_contracts_datasets_commerce_discount_allocation
