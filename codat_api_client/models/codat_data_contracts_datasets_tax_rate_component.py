from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsTaxRateComponent")


@define
class CodatDataContractsDatasetsTaxRateComponent:
    """
    Attributes:
        is_compound (bool):
        name (Union[Unset, None, str]):
        rate (Union[Unset, None, float]):
    """

    is_compound: bool
    name: Union[Unset, None, str] = UNSET
    rate: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_compound = self.is_compound
        name = self.name
        rate = self.rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "isCompound": is_compound,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_compound = d.pop("isCompound")

        name = d.pop("name", UNSET)

        rate = d.pop("rate", UNSET)

        codat_data_contracts_datasets_tax_rate_component = cls(
            is_compound=is_compound,
            name=name,
            rate=rate,
        )

        return codat_data_contracts_datasets_tax_rate_component
