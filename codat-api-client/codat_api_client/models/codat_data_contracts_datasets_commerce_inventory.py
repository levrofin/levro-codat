from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_inventory_location import (
        CodatDataContractsDatasetsCommerceInventoryLocation,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceInventory")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCommerceInventory:
    """
    Attributes:
        total_quantity (Union[Unset, None, float]):
        locations (Union[Unset, None, List['CodatDataContractsDatasetsCommerceInventoryLocation']]):
    """

    total_quantity: Union[Unset, None, float] = UNSET
    locations: Union[Unset, None, List["CodatDataContractsDatasetsCommerceInventoryLocation"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        total_quantity = self.total_quantity
        locations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            if self.locations is None:
                locations = None
            else:
                locations = []
                for locations_item_data in self.locations:
                    locations_item = locations_item_data.to_dict()

                    locations.append(locations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if total_quantity is not UNSET:
            field_dict["totalQuantity"] = total_quantity
        if locations is not UNSET:
            field_dict["locations"] = locations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_commerce_inventory_location import (
            CodatDataContractsDatasetsCommerceInventoryLocation,
        )

        d = src_dict.copy()
        total_quantity = d.pop("totalQuantity", UNSET)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = CodatDataContractsDatasetsCommerceInventoryLocation.from_dict(locations_item_data)

            locations.append(locations_item)

        codat_data_contracts_datasets_commerce_inventory = cls(
            total_quantity=total_quantity,
            locations=locations,
        )

        return codat_data_contracts_datasets_commerce_inventory
