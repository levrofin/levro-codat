import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataIntegrityContractsMetadataMatchDateInfo")


@define
class CodatDataIntegrityContractsMetadataMatchDateInfo:
    """
    Attributes:
        min_date (Union[Unset, None, datetime.datetime]):
        max_date (Union[Unset, None, datetime.datetime]):
        min_overlapping_date (Union[Unset, None, datetime.datetime]):
        max_overlapping_date (Union[Unset, None, datetime.datetime]):
    """

    min_date: Union[Unset, None, datetime.datetime] = UNSET
    max_date: Union[Unset, None, datetime.datetime] = UNSET
    min_overlapping_date: Union[Unset, None, datetime.datetime] = UNSET
    max_overlapping_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        min_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.min_date, Unset):
            min_date = self.min_date.isoformat() if self.min_date else None

        max_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.max_date, Unset):
            max_date = self.max_date.isoformat() if self.max_date else None

        min_overlapping_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.min_overlapping_date, Unset):
            min_overlapping_date = self.min_overlapping_date.isoformat() if self.min_overlapping_date else None

        max_overlapping_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.max_overlapping_date, Unset):
            max_overlapping_date = self.max_overlapping_date.isoformat() if self.max_overlapping_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if min_date is not UNSET:
            field_dict["minDate"] = min_date
        if max_date is not UNSET:
            field_dict["maxDate"] = max_date
        if min_overlapping_date is not UNSET:
            field_dict["minOverlappingDate"] = min_overlapping_date
        if max_overlapping_date is not UNSET:
            field_dict["maxOverlappingDate"] = max_overlapping_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _min_date = d.pop("minDate", UNSET)
        min_date: Union[Unset, None, datetime.datetime]
        if _min_date is None:
            min_date = None
        elif isinstance(_min_date, Unset):
            min_date = UNSET
        else:
            min_date = isoparse(_min_date)

        _max_date = d.pop("maxDate", UNSET)
        max_date: Union[Unset, None, datetime.datetime]
        if _max_date is None:
            max_date = None
        elif isinstance(_max_date, Unset):
            max_date = UNSET
        else:
            max_date = isoparse(_max_date)

        _min_overlapping_date = d.pop("minOverlappingDate", UNSET)
        min_overlapping_date: Union[Unset, None, datetime.datetime]
        if _min_overlapping_date is None:
            min_overlapping_date = None
        elif isinstance(_min_overlapping_date, Unset):
            min_overlapping_date = UNSET
        else:
            min_overlapping_date = isoparse(_min_overlapping_date)

        _max_overlapping_date = d.pop("maxOverlappingDate", UNSET)
        max_overlapping_date: Union[Unset, None, datetime.datetime]
        if _max_overlapping_date is None:
            max_overlapping_date = None
        elif isinstance(_max_overlapping_date, Unset):
            max_overlapping_date = UNSET
        else:
            max_overlapping_date = isoparse(_max_overlapping_date)

        codat_data_integrity_contracts_metadata_match_date_info = cls(
            min_date=min_date,
            max_date=max_date,
            min_overlapping_date=min_overlapping_date,
            max_overlapping_date=max_overlapping_date,
        )

        return codat_data_integrity_contracts_metadata_match_date_info
