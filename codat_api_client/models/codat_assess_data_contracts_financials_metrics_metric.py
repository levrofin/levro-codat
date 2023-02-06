from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.codat_assess_data_contracts_financials_metrics_metric_key import (
    CodatAssessDataContractsFinancialsMetricsMetricKey,
)
from ..models.codat_assess_data_contracts_financials_metrics_metric_unit import (
    CodatAssessDataContractsFinancialsMetricsMetricUnit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_financials_metrics_metric_error import (
        CodatAssessDataContractsFinancialsMetricsMetricError,
    )
    from ..models.codat_assess_data_contracts_financials_metrics_metric_period import (
        CodatAssessDataContractsFinancialsMetricsMetricPeriod,
    )


T = TypeVar("T", bound="CodatAssessDataContractsFinancialsMetricsMetric")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsFinancialsMetricsMetric:
    """
    Attributes:
        name (Union[Unset, None, str]):
        metric_unit (Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricUnit]):
        key (Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricKey]):
        periods (Union[Unset, None, List['CodatAssessDataContractsFinancialsMetricsMetricPeriod']]):
        errors (Union[Unset, None, List['CodatAssessDataContractsFinancialsMetricsMetricError']]):
    """

    name: Union[Unset, None, str] = UNSET
    metric_unit: Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricUnit] = UNSET
    key: Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricKey] = UNSET
    periods: Union[Unset, None, List["CodatAssessDataContractsFinancialsMetricsMetricPeriod"]] = UNSET
    errors: Union[Unset, None, List["CodatAssessDataContractsFinancialsMetricsMetricError"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        metric_unit: Union[Unset, str] = UNSET
        if not isinstance(self.metric_unit, Unset):
            metric_unit = self.metric_unit.value

        key: Union[Unset, str] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.value

        periods: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.periods, Unset):
            if self.periods is None:
                periods = None
            else:
                periods = []
                for periods_item_data in self.periods:
                    periods_item = periods_item_data.to_dict()

                    periods.append(periods_item)

        errors: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            if self.errors is None:
                errors = None
            else:
                errors = []
                for errors_item_data in self.errors:
                    errors_item = errors_item_data.to_dict()

                    errors.append(errors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if metric_unit is not UNSET:
            field_dict["metricUnit"] = metric_unit
        if key is not UNSET:
            field_dict["key"] = key
        if periods is not UNSET:
            field_dict["periods"] = periods
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_financials_metrics_metric_error import (
            CodatAssessDataContractsFinancialsMetricsMetricError,
        )
        from ..models.codat_assess_data_contracts_financials_metrics_metric_period import (
            CodatAssessDataContractsFinancialsMetricsMetricPeriod,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _metric_unit = d.pop("metricUnit", UNSET)
        metric_unit: Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricUnit]
        if isinstance(_metric_unit, Unset):
            metric_unit = UNSET
        else:
            metric_unit = CodatAssessDataContractsFinancialsMetricsMetricUnit(_metric_unit)

        _key = d.pop("key", UNSET)
        key: Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricKey]
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = CodatAssessDataContractsFinancialsMetricsMetricKey(_key)

        periods = []
        _periods = d.pop("periods", UNSET)
        for periods_item_data in _periods or []:
            periods_item = CodatAssessDataContractsFinancialsMetricsMetricPeriod.from_dict(periods_item_data)

            periods.append(periods_item)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = CodatAssessDataContractsFinancialsMetricsMetricError.from_dict(errors_item_data)

            errors.append(errors_item)

        codat_assess_data_contracts_financials_metrics_metric = cls(
            name=name,
            metric_unit=metric_unit,
            key=key,
            periods=periods,
            errors=errors,
        )

        return codat_assess_data_contracts_financials_metrics_metric
