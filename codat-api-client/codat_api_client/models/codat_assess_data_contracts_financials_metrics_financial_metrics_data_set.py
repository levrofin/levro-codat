from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.codat_assess_data_contracts_financials_metrics_metric_period_unit import (
    CodatAssessDataContractsFinancialsMetricsMetricPeriodUnit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_financials_metrics_metric import (
        CodatAssessDataContractsFinancialsMetricsMetric,
    )
    from ..models.codat_assess_data_contracts_financials_metrics_metric_data_set_error import (
        CodatAssessDataContractsFinancialsMetricsMetricDataSetError,
    )


T = TypeVar("T", bound="CodatAssessDataContractsFinancialsMetricsFinancialMetricsDataSet")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsFinancialsMetricsFinancialMetricsDataSet:
    """
    Attributes:
        currency (Union[Unset, None, str]):
        metrics (Union[Unset, None, List['CodatAssessDataContractsFinancialsMetricsMetric']]):
        period_unit (Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricPeriodUnit]):
        errors (Union[Unset, None, List['CodatAssessDataContractsFinancialsMetricsMetricDataSetError']]):
    """

    currency: Union[Unset, None, str] = UNSET
    metrics: Union[Unset, None, List["CodatAssessDataContractsFinancialsMetricsMetric"]] = UNSET
    period_unit: Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricPeriodUnit] = UNSET
    errors: Union[Unset, None, List["CodatAssessDataContractsFinancialsMetricsMetricDataSetError"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency
        metrics: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metrics, Unset):
            if self.metrics is None:
                metrics = None
            else:
                metrics = []
                for metrics_item_data in self.metrics:
                    metrics_item = metrics_item_data.to_dict()

                    metrics.append(metrics_item)

        period_unit: Union[Unset, str] = UNSET
        if not isinstance(self.period_unit, Unset):
            period_unit = self.period_unit.value

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
        if currency is not UNSET:
            field_dict["currency"] = currency
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if period_unit is not UNSET:
            field_dict["periodUnit"] = period_unit
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_financials_metrics_metric import (
            CodatAssessDataContractsFinancialsMetricsMetric,
        )
        from ..models.codat_assess_data_contracts_financials_metrics_metric_data_set_error import (
            CodatAssessDataContractsFinancialsMetricsMetricDataSetError,
        )

        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        metrics = []
        _metrics = d.pop("metrics", UNSET)
        for metrics_item_data in _metrics or []:
            metrics_item = CodatAssessDataContractsFinancialsMetricsMetric.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        _period_unit = d.pop("periodUnit", UNSET)
        period_unit: Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricPeriodUnit]
        if isinstance(_period_unit, Unset):
            period_unit = UNSET
        else:
            period_unit = CodatAssessDataContractsFinancialsMetricsMetricPeriodUnit(_period_unit)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = CodatAssessDataContractsFinancialsMetricsMetricDataSetError.from_dict(errors_item_data)

            errors.append(errors_item)

        codat_assess_data_contracts_financials_metrics_financial_metrics_data_set = cls(
            currency=currency,
            metrics=metrics,
            period_unit=period_unit,
            errors=errors,
        )

        return codat_assess_data_contracts_financials_metrics_financial_metrics_data_set
