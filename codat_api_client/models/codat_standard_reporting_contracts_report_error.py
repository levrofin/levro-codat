from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..models.codat_standard_reporting_contracts_report_error_type import CodatStandardReportingContractsReportErrorType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_standard_reporting_contracts_report_error_details import (
        CodatStandardReportingContractsReportErrorDetails,
    )


T = TypeVar("T", bound="CodatStandardReportingContractsReportError")


@define
class CodatStandardReportingContractsReportError:
    """
    Attributes:
        message (Union[Unset, None, str]):
        type (Union[Unset, CodatStandardReportingContractsReportErrorType]):
        details (Union[Unset, None, CodatStandardReportingContractsReportErrorDetails]):
    """

    message: Union[Unset, None, str] = UNSET
    type: Union[Unset, CodatStandardReportingContractsReportErrorType] = UNSET
    details: Union[Unset, None, "CodatStandardReportingContractsReportErrorDetails"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        details: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict() if self.details else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if type is not UNSET:
            field_dict["type"] = type
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_standard_reporting_contracts_report_error_details import (
            CodatStandardReportingContractsReportErrorDetails,
        )

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CodatStandardReportingContractsReportErrorType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodatStandardReportingContractsReportErrorType(_type)

        _details = d.pop("details", UNSET)
        details: Union[Unset, None, CodatStandardReportingContractsReportErrorDetails]
        if _details is None:
            details = None
        elif isinstance(_details, Unset):
            details = UNSET
        else:
            details = CodatStandardReportingContractsReportErrorDetails.from_dict(_details)

        codat_standard_reporting_contracts_report_error = cls(
            message=message,
            type=type,
            details=details,
        )

        return codat_standard_reporting_contracts_report_error
