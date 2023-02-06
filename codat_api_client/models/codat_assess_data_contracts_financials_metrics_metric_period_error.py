from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.codat_assess_data_contracts_financials_metrics_metric_period_error_type import (
    CodatAssessDataContractsFinancialsMetricsMetricPeriodErrorType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_financials_metrics_metric_period_error_details import (
        CodatAssessDataContractsFinancialsMetricsMetricPeriodErrorDetails,
    )


T = TypeVar("T", bound="CodatAssessDataContractsFinancialsMetricsMetricPeriodError")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsFinancialsMetricsMetricPeriodError:
    """
    Attributes:
        type (Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricPeriodErrorType]):
        message (Union[Unset, None, str]):
        details (Union[Unset, None, CodatAssessDataContractsFinancialsMetricsMetricPeriodErrorDetails]):
    """

    type: Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricPeriodErrorType] = UNSET
    message: Union[Unset, None, str] = UNSET
    details: Union[Unset, None, "CodatAssessDataContractsFinancialsMetricsMetricPeriodErrorDetails"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        message = self.message
        details: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict() if self.details else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if message is not UNSET:
            field_dict["message"] = message
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_financials_metrics_metric_period_error_details import (
            CodatAssessDataContractsFinancialsMetricsMetricPeriodErrorDetails,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricPeriodErrorType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodatAssessDataContractsFinancialsMetricsMetricPeriodErrorType(_type)

        message = d.pop("message", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, None, CodatAssessDataContractsFinancialsMetricsMetricPeriodErrorDetails]
        if _details is None:
            details = None
        elif isinstance(_details, Unset):
            details = UNSET
        else:
            details = CodatAssessDataContractsFinancialsMetricsMetricPeriodErrorDetails.from_dict(_details)

        codat_assess_data_contracts_financials_metrics_metric_period_error = cls(
            type=type,
            message=message,
            details=details,
        )

        return codat_assess_data_contracts_financials_metrics_metric_period_error
