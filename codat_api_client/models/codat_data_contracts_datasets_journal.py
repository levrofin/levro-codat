import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_journal_status import CodatDataContractsDatasetsJournalStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata


T = TypeVar("T", bound="CodatDataContractsDatasetsJournal")


@define
class CodatDataContractsDatasetsJournal:
    """
    Attributes:
        id (Union[Unset, None, str]):
        journal_code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        has_children (Union[Unset, bool]):
        created_on (Union[Unset, None, datetime.datetime]):
        status (Union[Unset, CodatDataContractsDatasetsJournalStatus]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
    """

    id: Union[Unset, None, str] = UNSET
    journal_code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    parent_id: Union[Unset, None, str] = UNSET
    has_children: Union[Unset, bool] = UNSET
    created_on: Union[Unset, None, datetime.datetime] = UNSET
    status: Union[Unset, CodatDataContractsDatasetsJournalStatus] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        journal_code = self.journal_code
        name = self.name
        type = self.type
        parent_id = self.parent_id
        has_children = self.has_children
        created_on: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat() if self.created_on else None

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if journal_code is not UNSET:
            field_dict["journalCode"] = journal_code
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if has_children is not UNSET:
            field_dict["hasChildren"] = has_children
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if status is not UNSET:
            field_dict["status"] = status
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        journal_code = d.pop("journalCode", UNSET)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        parent_id = d.pop("parentId", UNSET)

        has_children = d.pop("hasChildren", UNSET)

        _created_on = d.pop("createdOn", UNSET)
        created_on: Union[Unset, None, datetime.datetime]
        if _created_on is None:
            created_on = None
        elif isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CodatDataContractsDatasetsJournalStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodatDataContractsDatasetsJournalStatus(_status)

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

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CodatDataContractsDatasetsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CodatDataContractsDatasetsMetadata.from_dict(_metadata)

        codat_data_contracts_datasets_journal = cls(
            id=id,
            journal_code=journal_code,
            name=name,
            type=type,
            parent_id=parent_id,
            has_children=has_children,
            created_on=created_on,
            status=status,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            metadata=metadata,
        )

        return codat_data_contracts_datasets_journal
