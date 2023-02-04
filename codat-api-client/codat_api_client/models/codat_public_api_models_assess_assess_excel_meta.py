import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsAssessAssessExcelMeta")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsAssessAssessExcelMeta:
    """
    Attributes:
        last_generated (Union[Unset, None, datetime.datetime]):
        in_progress (Union[Unset, bool]):
        queued (Union[Unset, datetime.datetime]):
        success (Union[Unset, bool]):
        error_message (Union[Unset, None, str]):
        last_invocation_id (Union[Unset, str]):
        report_type (Union[Unset, None, str]):
        file_size (Union[Unset, None, int]):
    """

    last_generated: Union[Unset, None, datetime.datetime] = UNSET
    in_progress: Union[Unset, bool] = UNSET
    queued: Union[Unset, datetime.datetime] = UNSET
    success: Union[Unset, bool] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    last_invocation_id: Union[Unset, str] = UNSET
    report_type: Union[Unset, None, str] = UNSET
    file_size: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        last_generated: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_generated, Unset):
            last_generated = self.last_generated.isoformat() if self.last_generated else None

        in_progress = self.in_progress
        queued: Union[Unset, str] = UNSET
        if not isinstance(self.queued, Unset):
            queued = self.queued.isoformat()

        success = self.success
        error_message = self.error_message
        last_invocation_id = self.last_invocation_id
        report_type = self.report_type
        file_size = self.file_size

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if last_generated is not UNSET:
            field_dict["lastGenerated"] = last_generated
        if in_progress is not UNSET:
            field_dict["inProgress"] = in_progress
        if queued is not UNSET:
            field_dict["queued"] = queued
        if success is not UNSET:
            field_dict["success"] = success
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if last_invocation_id is not UNSET:
            field_dict["lastInvocationId"] = last_invocation_id
        if report_type is not UNSET:
            field_dict["reportType"] = report_type
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _last_generated = d.pop("lastGenerated", UNSET)
        last_generated: Union[Unset, None, datetime.datetime]
        if _last_generated is None:
            last_generated = None
        elif isinstance(_last_generated, Unset):
            last_generated = UNSET
        else:
            last_generated = isoparse(_last_generated)

        in_progress = d.pop("inProgress", UNSET)

        _queued = d.pop("queued", UNSET)
        queued: Union[Unset, datetime.datetime]
        if isinstance(_queued, Unset):
            queued = UNSET
        else:
            queued = isoparse(_queued)

        success = d.pop("success", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        last_invocation_id = d.pop("lastInvocationId", UNSET)

        report_type = d.pop("reportType", UNSET)

        file_size = d.pop("fileSize", UNSET)

        codat_public_api_models_assess_assess_excel_meta = cls(
            last_generated=last_generated,
            in_progress=in_progress,
            queued=queued,
            success=success,
            error_message=error_message,
            last_invocation_id=last_invocation_id,
            report_type=report_type,
            file_size=file_size,
        )

        return codat_public_api_models_assess_assess_excel_meta
