import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPullMessagesContractsMapMessage")


@attr.s(auto_attribs=True)
class CodatPullMessagesContractsMapMessage:
    """
    Attributes:
        log_level (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        log_date_time_utc (Union[Unset, None, datetime.datetime]):
    """

    log_level: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    log_date_time_utc: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        log_level = self.log_level
        message = self.message
        log_date_time_utc: Union[Unset, None, str] = UNSET
        if not isinstance(self.log_date_time_utc, Unset):
            log_date_time_utc = self.log_date_time_utc.isoformat() if self.log_date_time_utc else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if log_level is not UNSET:
            field_dict["logLevel"] = log_level
        if message is not UNSET:
            field_dict["message"] = message
        if log_date_time_utc is not UNSET:
            field_dict["logDateTimeUtc"] = log_date_time_utc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        log_level = d.pop("logLevel", UNSET)

        message = d.pop("message", UNSET)

        _log_date_time_utc = d.pop("logDateTimeUtc", UNSET)
        log_date_time_utc: Union[Unset, None, datetime.datetime]
        if _log_date_time_utc is None:
            log_date_time_utc = None
        elif isinstance(_log_date_time_utc, Unset):
            log_date_time_utc = UNSET
        else:
            log_date_time_utc = isoparse(_log_date_time_utc)

        codat_pull_messages_contracts_map_message = cls(
            log_level=log_level,
            message=message,
            log_date_time_utc=log_date_time_utc,
        )

        return codat_pull_messages_contracts_map_message
