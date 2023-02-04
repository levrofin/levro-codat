from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_standard_reporting_contracts_i_dimension_item import (
        CodatStandardReportingContractsIDimensionItem,
    )


T = TypeVar("T", bound="CodatStandardReportingContractsIDimension")


@attr.s(auto_attribs=True)
class CodatStandardReportingContractsIDimension:
    """
    Attributes:
        index (Union[Unset, int]):
        display_name (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        items (Union[Unset, None, List['CodatStandardReportingContractsIDimensionItem']]):
    """

    index: Union[Unset, int] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    items: Union[Unset, None, List["CodatStandardReportingContractsIDimensionItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        index = self.index
        display_name = self.display_name
        type = self.type
        items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            if self.items is None:
                items = None
            else:
                items = []
                for items_item_data in self.items:
                    items_item = items_item_data.to_dict()

                    items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if type is not UNSET:
            field_dict["type"] = type
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_standard_reporting_contracts_i_dimension_item import (
            CodatStandardReportingContractsIDimensionItem,
        )

        d = src_dict.copy()
        index = d.pop("index", UNSET)

        display_name = d.pop("displayName", UNSET)

        type = d.pop("type", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = CodatStandardReportingContractsIDimensionItem.from_dict(items_item_data)

            items.append(items_item)

        codat_standard_reporting_contracts_i_dimension = cls(
            index=index,
            display_name=display_name,
            type=type,
            items=items,
        )

        return codat_standard_reporting_contracts_i_dimension
