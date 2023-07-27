from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatStandardReportingContractsIDimensionItem")


@define
class CodatStandardReportingContractsIDimensionItem:
    """
    Attributes:
        index (Union[Unset, int]):
    """

    index: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        index = self.index

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        index = d.pop("index", UNSET)

        codat_standard_reporting_contracts_i_dimension_item = cls(
            index=index,
        )

        return codat_standard_reporting_contracts_i_dimension_item
