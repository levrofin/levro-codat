from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsPurchaseOrderRef")


@define
class CodatDataContractsDatasetsPurchaseOrderRef:
    """
    Attributes:
        id (Union[Unset, None, str]):
        purchase_order_number (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    purchase_order_number: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        purchase_order_number = self.purchase_order_number

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if purchase_order_number is not UNSET:
            field_dict["purchaseOrderNumber"] = purchase_order_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        purchase_order_number = d.pop("purchaseOrderNumber", UNSET)

        codat_data_contracts_datasets_purchase_order_ref = cls(
            id=id,
            purchase_order_number=purchase_order_number,
        )

        return codat_data_contracts_datasets_purchase_order_ref
