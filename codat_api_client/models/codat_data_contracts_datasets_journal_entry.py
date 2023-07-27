import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
        CodatDataContractsDatasetsDataInterfacesSupplementalData,
    )
    from ..models.codat_data_contracts_datasets_journal_line import CodatDataContractsDatasetsJournalLine
    from ..models.codat_data_contracts_datasets_journal_ref import CodatDataContractsDatasetsJournalRef
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
    from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef


T = TypeVar("T", bound="CodatDataContractsDatasetsJournalEntry")


@define
class CodatDataContractsDatasetsJournalEntry:
    """
    Attributes:
        id (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        posted_on (Union[Unset, None, datetime.datetime]):
        created_on (Union[Unset, None, datetime.datetime]):
        updated_on (Union[Unset, None, datetime.datetime]):
        journal_ref (Union[Unset, CodatDataContractsDatasetsJournalRef]):
        journal_lines (Union[Unset, None, List['CodatDataContractsDatasetsJournalLine']]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        record_ref (Union[Unset, CodatDataContractsDatasetsRecordRef]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
        supplemental_data (Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]):
    """

    id: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    posted_on: Union[Unset, None, datetime.datetime] = UNSET
    created_on: Union[Unset, None, datetime.datetime] = UNSET
    updated_on: Union[Unset, None, datetime.datetime] = UNSET
    journal_ref: Union[Unset, "CodatDataContractsDatasetsJournalRef"] = UNSET
    journal_lines: Union[Unset, None, List["CodatDataContractsDatasetsJournalLine"]] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    record_ref: Union[Unset, "CodatDataContractsDatasetsRecordRef"] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET
    supplemental_data: Union[Unset, "CodatDataContractsDatasetsDataInterfacesSupplementalData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        description = self.description
        posted_on: Union[Unset, None, str] = UNSET
        if not isinstance(self.posted_on, Unset):
            posted_on = self.posted_on.isoformat() if self.posted_on else None

        created_on: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat() if self.created_on else None

        updated_on: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat() if self.updated_on else None

        journal_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.journal_ref, Unset):
            journal_ref = self.journal_ref.to_dict()

        journal_lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.journal_lines, Unset):
            if self.journal_lines is None:
                journal_lines = None
            else:
                journal_lines = []
                for journal_lines_item_data in self.journal_lines:
                    journal_lines_item = journal_lines_item_data.to_dict()

                    journal_lines.append(journal_lines_item)

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        record_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_ref, Unset):
            record_ref = self.record_ref.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        supplemental_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplemental_data, Unset):
            supplemental_data = self.supplemental_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if posted_on is not UNSET:
            field_dict["postedOn"] = posted_on
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if updated_on is not UNSET:
            field_dict["updatedOn"] = updated_on
        if journal_ref is not UNSET:
            field_dict["journalRef"] = journal_ref
        if journal_lines is not UNSET:
            field_dict["journalLines"] = journal_lines
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if record_ref is not UNSET:
            field_dict["recordRef"] = record_ref
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if supplemental_data is not UNSET:
            field_dict["supplementalData"] = supplemental_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
            CodatDataContractsDatasetsDataInterfacesSupplementalData,
        )
        from ..models.codat_data_contracts_datasets_journal_line import CodatDataContractsDatasetsJournalLine
        from ..models.codat_data_contracts_datasets_journal_ref import CodatDataContractsDatasetsJournalRef
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
        from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        _posted_on = d.pop("postedOn", UNSET)
        posted_on: Union[Unset, None, datetime.datetime]
        if _posted_on is None:
            posted_on = None
        elif isinstance(_posted_on, Unset):
            posted_on = UNSET
        else:
            posted_on = isoparse(_posted_on)

        _created_on = d.pop("createdOn", UNSET)
        created_on: Union[Unset, None, datetime.datetime]
        if _created_on is None:
            created_on = None
        elif isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _updated_on = d.pop("updatedOn", UNSET)
        updated_on: Union[Unset, None, datetime.datetime]
        if _updated_on is None:
            updated_on = None
        elif isinstance(_updated_on, Unset):
            updated_on = UNSET
        else:
            updated_on = isoparse(_updated_on)

        _journal_ref = d.pop("journalRef", UNSET)
        journal_ref: Union[Unset, CodatDataContractsDatasetsJournalRef]
        if isinstance(_journal_ref, Unset):
            journal_ref = UNSET
        else:
            journal_ref = CodatDataContractsDatasetsJournalRef.from_dict(_journal_ref)

        journal_lines = []
        _journal_lines = d.pop("journalLines", UNSET)
        for journal_lines_item_data in _journal_lines or []:
            journal_lines_item = CodatDataContractsDatasetsJournalLine.from_dict(journal_lines_item_data)

            journal_lines.append(journal_lines_item)

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

        _record_ref = d.pop("recordRef", UNSET)
        record_ref: Union[Unset, CodatDataContractsDatasetsRecordRef]
        if isinstance(_record_ref, Unset):
            record_ref = UNSET
        else:
            record_ref = CodatDataContractsDatasetsRecordRef.from_dict(_record_ref)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CodatDataContractsDatasetsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CodatDataContractsDatasetsMetadata.from_dict(_metadata)

        _supplemental_data = d.pop("supplementalData", UNSET)
        supplemental_data: Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]
        if isinstance(_supplemental_data, Unset):
            supplemental_data = UNSET
        else:
            supplemental_data = CodatDataContractsDatasetsDataInterfacesSupplementalData.from_dict(_supplemental_data)

        codat_data_contracts_datasets_journal_entry = cls(
            id=id,
            description=description,
            posted_on=posted_on,
            created_on=created_on,
            updated_on=updated_on,
            journal_ref=journal_ref,
            journal_lines=journal_lines,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            record_ref=record_ref,
            metadata=metadata,
            supplemental_data=supplemental_data,
        )

        return codat_data_contracts_datasets_journal_entry
