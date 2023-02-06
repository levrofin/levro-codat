import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_data_integrity_contracts_metadata_run_status import CodatDataIntegrityContractsMetadataRunStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataIntegrityContractsMetadataMatchStatusInfo")


@attr.s(auto_attribs=True)
class CodatDataIntegrityContractsMetadataMatchStatusInfo:
    """
    Attributes:
        last_matched (Union[Unset, None, datetime.datetime]):
        current_status (Union[Unset, CodatDataIntegrityContractsMetadataRunStatus]):
        status_message (Union[Unset, None, str]):
    """

    last_matched: Union[Unset, None, datetime.datetime] = UNSET
    current_status: Union[Unset, CodatDataIntegrityContractsMetadataRunStatus] = UNSET
    status_message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        last_matched: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_matched, Unset):
            last_matched = self.last_matched.isoformat() if self.last_matched else None

        current_status: Union[Unset, str] = UNSET
        if not isinstance(self.current_status, Unset):
            current_status = self.current_status.value

        status_message = self.status_message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if last_matched is not UNSET:
            field_dict["lastMatched"] = last_matched
        if current_status is not UNSET:
            field_dict["currentStatus"] = current_status
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _last_matched = d.pop("lastMatched", UNSET)
        last_matched: Union[Unset, None, datetime.datetime]
        if _last_matched is None:
            last_matched = None
        elif isinstance(_last_matched, Unset):
            last_matched = UNSET
        else:
            last_matched = isoparse(_last_matched)

        _current_status = d.pop("currentStatus", UNSET)
        current_status: Union[Unset, CodatDataIntegrityContractsMetadataRunStatus]
        if isinstance(_current_status, Unset):
            current_status = UNSET
        else:
            current_status = CodatDataIntegrityContractsMetadataRunStatus(_current_status)

        status_message = d.pop("statusMessage", UNSET)

        codat_data_integrity_contracts_metadata_match_status_info = cls(
            last_matched=last_matched,
            current_status=current_status,
            status_message=status_message,
        )

        return codat_data_integrity_contracts_metadata_match_status_info
