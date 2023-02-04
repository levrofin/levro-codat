import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPullMessagesContractsValidationMessage")


@attr.s(auto_attribs=True)
class CodatPullMessagesContractsValidationMessage:
    """
    Attributes:
        rule_id (Union[Unset, None, str]):
        item_id (Union[Unset, None, str]):
        validator_name (Union[Unset, None, str]):
        log_level (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        log_date_time_utc (Union[Unset, None, datetime.datetime]):
    """

    rule_id: Union[Unset, None, str] = UNSET
    item_id: Union[Unset, None, str] = UNSET
    validator_name: Union[Unset, None, str] = UNSET
    log_level: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    log_date_time_utc: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        rule_id = self.rule_id
        item_id = self.item_id
        validator_name = self.validator_name
        log_level = self.log_level
        message = self.message
        log_date_time_utc: Union[Unset, None, str] = UNSET
        if not isinstance(self.log_date_time_utc, Unset):
            log_date_time_utc = self.log_date_time_utc.isoformat() if self.log_date_time_utc else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if rule_id is not UNSET:
            field_dict["ruleId"] = rule_id
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if validator_name is not UNSET:
            field_dict["validatorName"] = validator_name
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
        rule_id = d.pop("ruleId", UNSET)

        item_id = d.pop("itemId", UNSET)

        validator_name = d.pop("validatorName", UNSET)

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

        codat_pull_messages_contracts_validation_message = cls(
            rule_id=rule_id,
            item_id=item_id,
            validator_name=validator_name,
            log_level=log_level,
            message=message,
            log_date_time_utc=log_date_time_utc,
        )

        return codat_pull_messages_contracts_validation_message
