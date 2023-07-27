from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceTaxComponentRef")


@define
class CodatDataContractsDatasetsCommerceTaxComponentRef:
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

        codat_data_contracts_datasets_commerce_tax_component_ref = cls(
            id=id,
            name=name,
        )

        return codat_data_contracts_datasets_commerce_tax_component_ref
