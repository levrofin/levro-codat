from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatStandardReportingContractsIReportDataMeasure")


@attr.s(auto_attribs=True)
class CodatStandardReportingContractsIReportDataMeasure:
    """
    Attributes:
        index (Union[Unset, int]):
        measure_display_name (Union[Unset, None, str]):
    """

    index: Union[Unset, int] = UNSET
    measure_display_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        index = self.index
        measure_display_name = self.measure_display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if measure_display_name is not UNSET:
            field_dict["measureDisplayName"] = measure_display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        index = d.pop("index", UNSET)

        measure_display_name = d.pop("measureDisplayName", UNSET)

        codat_standard_reporting_contracts_i_report_data_measure = cls(
            index=index,
            measure_display_name=measure_display_name,
        )

        return codat_standard_reporting_contracts_i_report_data_measure
