from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsReportLine")


@define
class CodatDataContractsDatasetsReportLine:
    """
    Attributes:
        value (float):
        account_id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        items (Union[Unset, None, List['CodatDataContractsDatasetsReportLine']]):
    """

    value: float
    account_id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    items: Union[Unset, None, List["CodatDataContractsDatasetsReportLine"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        account_id = self.account_id
        name = self.name
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
        field_dict.update(
            {
                "value": value,
            }
        )
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if name is not UNSET:
            field_dict["name"] = name
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        account_id = d.pop("accountId", UNSET)

        name = d.pop("name", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = CodatDataContractsDatasetsReportLine.from_dict(items_item_data)

            items.append(items_item)

        codat_data_contracts_datasets_report_line = cls(
            value=value,
            account_id=account_id,
            name=name,
            items=items,
        )

        return codat_data_contracts_datasets_report_line
