from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.codat_assess_data_contracts_financials_metrics_metric_data_set_error_type import (
    CodatAssessDataContractsFinancialsMetricsMetricDataSetErrorType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatAssessDataContractsFinancialsMetricsMetricDataSetError")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsFinancialsMetricsMetricDataSetError:
    """
    Attributes:
        type (Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricDataSetErrorType]):
        message (Union[Unset, None, str]):
    """

    type: Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricDataSetErrorType] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, CodatAssessDataContractsFinancialsMetricsMetricDataSetErrorType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodatAssessDataContractsFinancialsMetricsMetricDataSetErrorType(_type)

        message = d.pop("message", UNSET)

        codat_assess_data_contracts_financials_metrics_metric_data_set_error = cls(
            type=type,
            message=message,
        )

        return codat_assess_data_contracts_financials_metrics_metric_data_set_error
