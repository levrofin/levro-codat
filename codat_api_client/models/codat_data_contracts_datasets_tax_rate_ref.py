from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsTaxRateRef")


@define
class CodatDataContractsDatasetsTaxRateRef:
    """
    Attributes:
        id (str):
        name (Union[Unset, None, str]):
        effective_tax_rate (Union[Unset, None, float]):
    """

    id: str
    name: Union[Unset, None, str] = UNSET
    effective_tax_rate: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        effective_tax_rate = self.effective_tax_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if effective_tax_rate is not UNSET:
            field_dict["effectiveTaxRate"] = effective_tax_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name", UNSET)

        effective_tax_rate = d.pop("effectiveTaxRate", UNSET)

        codat_data_contracts_datasets_tax_rate_ref = cls(
            id=id,
            name=name,
            effective_tax_rate=effective_tax_rate,
        )

        return codat_data_contracts_datasets_tax_rate_ref
