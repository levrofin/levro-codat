import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_financials_metrics_metric_period_error import (
        CodatAssessDataContractsFinancialsMetricsMetricPeriodError,
    )
    from ..models.codat_assess_data_contracts_financials_metrics_metric_period_input import (
        CodatAssessDataContractsFinancialsMetricsMetricPeriodInput,
    )


T = TypeVar("T", bound="CodatAssessDataContractsFinancialsMetricsMetricPeriod")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsFinancialsMetricsMetricPeriod:
    """
    Attributes:
        from_date (Union[Unset, datetime.datetime]):
        to_date (Union[Unset, datetime.datetime]):
        value (Union[Unset, None, float]):
        inputs (Union[Unset, None, List['CodatAssessDataContractsFinancialsMetricsMetricPeriodInput']]):
        errors (Union[Unset, None, List['CodatAssessDataContractsFinancialsMetricsMetricPeriodError']]):
    """

    from_date: Union[Unset, datetime.datetime] = UNSET
    to_date: Union[Unset, datetime.datetime] = UNSET
    value: Union[Unset, None, float] = UNSET
    inputs: Union[Unset, None, List["CodatAssessDataContractsFinancialsMetricsMetricPeriodInput"]] = UNSET
    errors: Union[Unset, None, List["CodatAssessDataContractsFinancialsMetricsMetricPeriodError"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from_date: Union[Unset, str] = UNSET
        if not isinstance(self.from_date, Unset):
            from_date = self.from_date.isoformat()

        to_date: Union[Unset, str] = UNSET
        if not isinstance(self.to_date, Unset):
            to_date = self.to_date.isoformat()

        value = self.value
        inputs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inputs, Unset):
            if self.inputs is None:
                inputs = None
            else:
                inputs = []
                for inputs_item_data in self.inputs:
                    inputs_item = inputs_item_data.to_dict()

                    inputs.append(inputs_item)

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
        if from_date is not UNSET:
            field_dict["fromDate"] = from_date
        if to_date is not UNSET:
            field_dict["toDate"] = to_date
        if value is not UNSET:
            field_dict["value"] = value
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_financials_metrics_metric_period_error import (
            CodatAssessDataContractsFinancialsMetricsMetricPeriodError,
        )
        from ..models.codat_assess_data_contracts_financials_metrics_metric_period_input import (
            CodatAssessDataContractsFinancialsMetricsMetricPeriodInput,
        )

        d = src_dict.copy()
        _from_date = d.pop("fromDate", UNSET)
        from_date: Union[Unset, datetime.datetime]
        if isinstance(_from_date, Unset):
            from_date = UNSET
        else:
            from_date = isoparse(_from_date)

        _to_date = d.pop("toDate", UNSET)
        to_date: Union[Unset, datetime.datetime]
        if isinstance(_to_date, Unset):
            to_date = UNSET
        else:
            to_date = isoparse(_to_date)

        value = d.pop("value", UNSET)

        inputs = []
        _inputs = d.pop("inputs", UNSET)
        for inputs_item_data in _inputs or []:
            inputs_item = CodatAssessDataContractsFinancialsMetricsMetricPeriodInput.from_dict(inputs_item_data)

            inputs.append(inputs_item)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = CodatAssessDataContractsFinancialsMetricsMetricPeriodError.from_dict(errors_item_data)

            errors.append(errors_item)

        codat_assess_data_contracts_financials_metrics_metric_period = cls(
            from_date=from_date,
            to_date=to_date,
            value=value,
            inputs=inputs,
            errors=errors,
        )

        return codat_assess_data_contracts_financials_metrics_metric_period
