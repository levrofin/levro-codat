import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsSyncSettingsSyncSettingModel")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsSyncSettingsSyncSettingModel:
    """
    Attributes:
        data_type (Union[Unset, None, str]):
        fetch_on_first_link (Union[Unset, bool]):
        sync_schedule (Union[Unset, int]):
        sync_order (Union[Unset, int]):
        sync_from_utc (Union[Unset, None, datetime.datetime]):
        sync_from_window (Union[Unset, None, int]):
        months_to_sync (Union[Unset, None, int]):
        is_locked (Union[Unset, None, bool]):
    """

    data_type: Union[Unset, None, str] = UNSET
    fetch_on_first_link: Union[Unset, bool] = UNSET
    sync_schedule: Union[Unset, int] = UNSET
    sync_order: Union[Unset, int] = UNSET
    sync_from_utc: Union[Unset, None, datetime.datetime] = UNSET
    sync_from_window: Union[Unset, None, int] = UNSET
    months_to_sync: Union[Unset, None, int] = UNSET
    is_locked: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        data_type = self.data_type
        fetch_on_first_link = self.fetch_on_first_link
        sync_schedule = self.sync_schedule
        sync_order = self.sync_order
        sync_from_utc: Union[Unset, None, str] = UNSET
        if not isinstance(self.sync_from_utc, Unset):
            sync_from_utc = self.sync_from_utc.isoformat() if self.sync_from_utc else None

        sync_from_window = self.sync_from_window
        months_to_sync = self.months_to_sync
        is_locked = self.is_locked

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if fetch_on_first_link is not UNSET:
            field_dict["fetchOnFirstLink"] = fetch_on_first_link
        if sync_schedule is not UNSET:
            field_dict["syncSchedule"] = sync_schedule
        if sync_order is not UNSET:
            field_dict["syncOrder"] = sync_order
        if sync_from_utc is not UNSET:
            field_dict["syncFromUtc"] = sync_from_utc
        if sync_from_window is not UNSET:
            field_dict["syncFromWindow"] = sync_from_window
        if months_to_sync is not UNSET:
            field_dict["monthsToSync"] = months_to_sync
        if is_locked is not UNSET:
            field_dict["isLocked"] = is_locked

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_type = d.pop("dataType", UNSET)

        fetch_on_first_link = d.pop("fetchOnFirstLink", UNSET)

        sync_schedule = d.pop("syncSchedule", UNSET)

        sync_order = d.pop("syncOrder", UNSET)

        _sync_from_utc = d.pop("syncFromUtc", UNSET)
        sync_from_utc: Union[Unset, None, datetime.datetime]
        if _sync_from_utc is None:
            sync_from_utc = None
        elif isinstance(_sync_from_utc, Unset):
            sync_from_utc = UNSET
        else:
            sync_from_utc = isoparse(_sync_from_utc)

        sync_from_window = d.pop("syncFromWindow", UNSET)

        months_to_sync = d.pop("monthsToSync", UNSET)

        is_locked = d.pop("isLocked", UNSET)

        codat_public_api_models_sync_settings_sync_setting_model = cls(
            data_type=data_type,
            fetch_on_first_link=fetch_on_first_link,
            sync_schedule=sync_schedule,
            sync_order=sync_order,
            sync_from_utc=sync_from_utc,
            sync_from_window=sync_from_window,
            months_to_sync=months_to_sync,
            is_locked=is_locked,
        )

        return codat_public_api_models_sync_settings_sync_setting_model
