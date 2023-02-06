import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsDataDataStatus")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsDataDataStatus:
    """
    Attributes:
        data_type (str):
        last_successful_sync (Union[Unset, None, datetime.datetime]):
        current_status (Union[Unset, None, str]):
        latest_sync_id (Union[Unset, None, str]):
        latest_successful_sync_id (Union[Unset, None, str]):
    """

    data_type: str
    last_successful_sync: Union[Unset, None, datetime.datetime] = UNSET
    current_status: Union[Unset, None, str] = UNSET
    latest_sync_id: Union[Unset, None, str] = UNSET
    latest_successful_sync_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        data_type = self.data_type
        last_successful_sync: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_successful_sync, Unset):
            last_successful_sync = self.last_successful_sync.isoformat() if self.last_successful_sync else None

        current_status = self.current_status
        latest_sync_id = self.latest_sync_id
        latest_successful_sync_id = self.latest_successful_sync_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "dataType": data_type,
            }
        )
        if last_successful_sync is not UNSET:
            field_dict["lastSuccessfulSync"] = last_successful_sync
        if current_status is not UNSET:
            field_dict["currentStatus"] = current_status
        if latest_sync_id is not UNSET:
            field_dict["latestSyncId"] = latest_sync_id
        if latest_successful_sync_id is not UNSET:
            field_dict["latestSuccessfulSyncId"] = latest_successful_sync_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_type = d.pop("dataType")

        _last_successful_sync = d.pop("lastSuccessfulSync", UNSET)
        last_successful_sync: Union[Unset, None, datetime.datetime]
        if _last_successful_sync is None:
            last_successful_sync = None
        elif isinstance(_last_successful_sync, Unset):
            last_successful_sync = UNSET
        else:
            last_successful_sync = isoparse(_last_successful_sync)

        current_status = d.pop("currentStatus", UNSET)

        latest_sync_id = d.pop("latestSyncId", UNSET)

        latest_successful_sync_id = d.pop("latestSuccessfulSyncId", UNSET)

        codat_public_api_models_data_data_status = cls(
            data_type=data_type,
            last_successful_sync=last_successful_sync,
            current_status=current_status,
            latest_sync_id=latest_sync_id,
            latest_successful_sync_id=latest_successful_sync_id,
        )

        return codat_public_api_models_data_data_status
