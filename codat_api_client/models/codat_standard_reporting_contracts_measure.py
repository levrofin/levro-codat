from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatStandardReportingContractsMeasure")


@attr.s(auto_attribs=True)
class CodatStandardReportingContractsMeasure:
    """
    Attributes:
        display_name (Union[Unset, None, str]):
        units (Union[Unset, None, str]):
        index (Union[Unset, int]):
        type (Union[Unset, None, str]):
    """

    display_name: Union[Unset, None, str] = UNSET
    units: Union[Unset, None, str] = UNSET
    index: Union[Unset, int] = UNSET
    type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        units = self.units
        index = self.index
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if units is not UNSET:
            field_dict["units"] = units
        if index is not UNSET:
            field_dict["index"] = index
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName", UNSET)

        units = d.pop("units", UNSET)

        index = d.pop("index", UNSET)

        type = d.pop("type", UNSET)

        codat_standard_reporting_contracts_measure = cls(
            display_name=display_name,
            units=units,
            index=index,
            type=type,
        )

        return codat_standard_reporting_contracts_measure
