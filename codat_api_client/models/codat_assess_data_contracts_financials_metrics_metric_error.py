from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.codat_assess_data_contracts_financials_metrics_metric_error_type import (
    CodatAssessDataContractsFinancialsMetricsMetricErrorType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_financials_metrics_metric_error_details import (
        CodatAssessDataContractsFinancialsMetricsMetricErrorDetails,
    )


T = TypeVar("T", bound="CodatAssessDataContractsFinancialsMetricsMetricError")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsFinancialsMetricsMetricError:
    """
    Attributes:
        type (Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricErrorType]):
        message (Union[Unset, None, str]):
        details (Union[Unset, None, CodatAssessDataContractsFinancialsMetricsMetricErrorDetails]):
    """

    type: Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricErrorType] = UNSET
    message: Union[Unset, None, str] = UNSET
    details: Union[Unset, None, "CodatAssessDataContractsFinancialsMetricsMetricErrorDetails"] = UNSET

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
        from ..models.codat_assess_data_contracts_financials_metrics_metric_error_details import (
            CodatAssessDataContractsFinancialsMetricsMetricErrorDetails,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricErrorType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodatAssessDataContractsFinancialsMetricsMetricErrorType(_type)

        message = d.pop("message", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, None, CodatAssessDataContractsFinancialsMetricsMetricErrorDetails]
        if _details is None:
            details = None
        elif isinstance(_details, Unset):
            details = UNSET
        else:
            details = CodatAssessDataContractsFinancialsMetricsMetricErrorDetails.from_dict(_details)

        codat_assess_data_contracts_financials_metrics_metric_error = cls(
            type=type,
            message=message,
            details=details,
        )

        return codat_assess_data_contracts_financials_metrics_metric_error
