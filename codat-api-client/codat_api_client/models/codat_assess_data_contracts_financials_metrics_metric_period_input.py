from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatAssessDataContractsFinancialsMetricsMetricPeriodInput")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsFinancialsMetricsMetricPeriodInput:
    """
    Attributes:
        name (Union[Unset, None, str]):
        value (Union[Unset, None, float]):
    """

    name: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        codat_assess_data_contracts_financials_metrics_metric_period_input = cls(
            name=name,
            value=value,
        )

        return codat_assess_data_contracts_financials_metrics_metric_period_input
