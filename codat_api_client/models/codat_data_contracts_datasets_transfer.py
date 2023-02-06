import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_contact_ref import CodatDataContractsDatasetsContactRef
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
        CodatDataContractsDatasetsDataInterfacesSupplementalData,
    )
    from ..models.codat_data_contracts_datasets_from_account import CodatDataContractsDatasetsFromAccount
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
    from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef
    from ..models.codat_data_contracts_datasets_to_account import CodatDataContractsDatasetsToAccount
    from ..models.codat_data_contracts_datasets_tracking_category_ref import (
        CodatDataContractsDatasetsTrackingCategoryRef,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsTransfer")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsTransfer:
    """
    Attributes:
        id (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        contact_ref (Union[Unset, CodatDataContractsDatasetsContactRef]):
        date (Union[Unset, datetime.datetime]):
        from_ (Union[Unset, CodatDataContractsDatasetsFromAccount]):
        to (Union[Unset, CodatDataContractsDatasetsToAccount]):
        tracking_category_refs (Union[Unset, None, List['CodatDataContractsDatasetsTrackingCategoryRef']]):
        deposited_record_refs (Union[Unset, None, List['CodatDataContractsDatasetsRecordRef']]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
        supplemental_data (Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]):
    """

    id: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    contact_ref: Union[Unset, "CodatDataContractsDatasetsContactRef"] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    from_: Union[Unset, "CodatDataContractsDatasetsFromAccount"] = UNSET
    to: Union[Unset, "CodatDataContractsDatasetsToAccount"] = UNSET
    tracking_category_refs: Union[Unset, None, List["CodatDataContractsDatasetsTrackingCategoryRef"]] = UNSET
    deposited_record_refs: Union[Unset, None, List["CodatDataContractsDatasetsRecordRef"]] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET
    supplemental_data: Union[Unset, "CodatDataContractsDatasetsDataInterfacesSupplementalData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        description = self.description
        contact_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact_ref, Unset):
            contact_ref = self.contact_ref.to_dict()

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        from_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        tracking_category_refs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking_category_refs, Unset):
            if self.tracking_category_refs is None:
                tracking_category_refs = None
            else:
                tracking_category_refs = []
                for tracking_category_refs_item_data in self.tracking_category_refs:
                    tracking_category_refs_item = tracking_category_refs_item_data.to_dict()

                    tracking_category_refs.append(tracking_category_refs_item)

        deposited_record_refs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.deposited_record_refs, Unset):
            if self.deposited_record_refs is None:
                deposited_record_refs = None
            else:
                deposited_record_refs = []
                for deposited_record_refs_item_data in self.deposited_record_refs:
                    deposited_record_refs_item = deposited_record_refs_item_data.to_dict()

                    deposited_record_refs.append(deposited_record_refs_item)

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

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
        if contact_ref is not UNSET:
            field_dict["contactRef"] = contact_ref
        if date is not UNSET:
            field_dict["date"] = date
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if tracking_category_refs is not UNSET:
            field_dict["trackingCategoryRefs"] = tracking_category_refs
        if deposited_record_refs is not UNSET:
            field_dict["depositedRecordRefs"] = deposited_record_refs
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if supplemental_data is not UNSET:
            field_dict["supplementalData"] = supplemental_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_contact_ref import CodatDataContractsDatasetsContactRef
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
            CodatDataContractsDatasetsDataInterfacesSupplementalData,
        )
        from ..models.codat_data_contracts_datasets_from_account import CodatDataContractsDatasetsFromAccount
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
        from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef
        from ..models.codat_data_contracts_datasets_to_account import CodatDataContractsDatasetsToAccount
        from ..models.codat_data_contracts_datasets_tracking_category_ref import (
            CodatDataContractsDatasetsTrackingCategoryRef,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        _contact_ref = d.pop("contactRef", UNSET)
        contact_ref: Union[Unset, CodatDataContractsDatasetsContactRef]
        if isinstance(_contact_ref, Unset):
            contact_ref = UNSET
        else:
            contact_ref = CodatDataContractsDatasetsContactRef.from_dict(_contact_ref)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, CodatDataContractsDatasetsFromAccount]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = CodatDataContractsDatasetsFromAccount.from_dict(_from_)

        _to = d.pop("to", UNSET)
        to: Union[Unset, CodatDataContractsDatasetsToAccount]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = CodatDataContractsDatasetsToAccount.from_dict(_to)

        tracking_category_refs = []
        _tracking_category_refs = d.pop("trackingCategoryRefs", UNSET)
        for tracking_category_refs_item_data in _tracking_category_refs or []:
            tracking_category_refs_item = CodatDataContractsDatasetsTrackingCategoryRef.from_dict(
                tracking_category_refs_item_data
            )

            tracking_category_refs.append(tracking_category_refs_item)

        deposited_record_refs = []
        _deposited_record_refs = d.pop("depositedRecordRefs", UNSET)
        for deposited_record_refs_item_data in _deposited_record_refs or []:
            deposited_record_refs_item = CodatDataContractsDatasetsRecordRef.from_dict(deposited_record_refs_item_data)

            deposited_record_refs.append(deposited_record_refs_item)

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

        _supplemental_data = d.pop("supplementalData", UNSET)
        supplemental_data: Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]
        if isinstance(_supplemental_data, Unset):
            supplemental_data = UNSET
        else:
            supplemental_data = CodatDataContractsDatasetsDataInterfacesSupplementalData.from_dict(_supplemental_data)

        codat_data_contracts_datasets_transfer = cls(
            id=id,
            description=description,
            contact_ref=contact_ref,
            date=date,
            from_=from_,
            to=to,
            tracking_category_refs=tracking_category_refs,
            deposited_record_refs=deposited_record_refs,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            metadata=metadata,
            supplemental_data=supplemental_data,
        )

        return codat_data_contracts_datasets_transfer
