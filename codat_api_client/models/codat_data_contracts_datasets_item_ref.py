from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsItemRef")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsItemRef:
    """
    Attributes:
        id (str):
        name (Union[Unset, None, str]):
    """

    id: str
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name", UNSET)

        codat_data_contracts_datasets_item_ref = cls(
            id=id,
            name=name,
        )

        return codat_data_contracts_datasets_item_ref
