import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsAttachmentsDatasetAttachment")


@define
class CodatDataContractsDatasetsAttachmentsDatasetAttachment:
    """
    Attributes:
        id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        content_type (Union[Unset, None, str]):
        date_created (Union[Unset, None, datetime.datetime]):
        file_size (Union[Unset, None, int]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        include_when_sent (Union[Unset, bool]):
    """

    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    content_type: Union[Unset, None, str] = UNSET
    date_created: Union[Unset, None, datetime.datetime] = UNSET
    file_size: Union[Unset, None, int] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    include_when_sent: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        content_type = self.content_type
        date_created: Union[Unset, None, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat() if self.date_created else None

        file_size = self.file_size
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        include_when_sent = self.include_when_sent

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if include_when_sent is not UNSET:
            field_dict["includeWhenSent"] = include_when_sent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        content_type = d.pop("contentType", UNSET)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, None, datetime.datetime]
        if _date_created is None:
            date_created = None
        elif isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        file_size = d.pop("fileSize", UNSET)

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: Union[Unset, None, datetime.datetime]
        if _modified_date is None:
            modified_date = None
        elif isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, None, datetime.datetime]
        if _source_modified_date is None:
            source_modified_date = None
        elif isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        include_when_sent = d.pop("includeWhenSent", UNSET)

        codat_data_contracts_datasets_attachments_dataset_attachment = cls(
            id=id,
            name=name,
            content_type=content_type,
            date_created=date_created,
            file_size=file_size,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            include_when_sent=include_when_sent,
        )

        return codat_data_contracts_datasets_attachments_dataset_attachment
