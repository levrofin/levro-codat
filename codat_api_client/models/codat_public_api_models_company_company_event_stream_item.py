import datetime
from typing import Any, Dict, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="CodatPublicApiModelsCompanyCompanyEventStreamItem")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsCompanyCompanyEventStreamItem:
    """
    Attributes:
        type (str):
        description (str):
        event_time_utc (datetime.datetime):
    """

    type: str
    description: str
    event_time_utc: datetime.datetime

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        description = self.description
        event_time_utc = self.event_time_utc.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "description": description,
                "eventTimeUtc": event_time_utc,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        description = d.pop("description")

        event_time_utc = isoparse(d.pop("eventTimeUtc"))

        codat_public_api_models_company_company_event_stream_item = cls(
            type=type,
            description=description,
            event_time_utc=event_time_utc,
        )

        return codat_public_api_models_company_company_event_stream_item
