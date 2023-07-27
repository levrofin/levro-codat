from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_location_ref import (
        CodatDataContractsDatasetsCommerceLocationRef,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceInventoryLocation")


@define
class CodatDataContractsDatasetsCommerceInventoryLocation:
    """
    Attributes:
        quantity (Union[Unset, float]):
        location_ref (Union[Unset, CodatDataContractsDatasetsCommerceLocationRef]):
    """

    quantity: Union[Unset, float] = UNSET
    location_ref: Union[Unset, "CodatDataContractsDatasetsCommerceLocationRef"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity
        location_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location_ref, Unset):
            location_ref = self.location_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if location_ref is not UNSET:
            field_dict["locationRef"] = location_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_commerce_location_ref import (
            CodatDataContractsDatasetsCommerceLocationRef,
        )

        d = src_dict.copy()
        quantity = d.pop("quantity", UNSET)

        _location_ref = d.pop("locationRef", UNSET)
        location_ref: Union[Unset, CodatDataContractsDatasetsCommerceLocationRef]
        if isinstance(_location_ref, Unset):
            location_ref = UNSET
        else:
            location_ref = CodatDataContractsDatasetsCommerceLocationRef.from_dict(_location_ref)

        codat_data_contracts_datasets_commerce_inventory_location = cls(
            quantity=quantity,
            location_ref=location_ref,
        )

        return codat_data_contracts_datasets_commerce_inventory_location
