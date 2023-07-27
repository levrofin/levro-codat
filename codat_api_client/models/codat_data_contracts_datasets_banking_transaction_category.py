import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_banking_transaction_category_status import (
    CodatDataContractsDatasetsBankingTransactionCategoryStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsBankingTransactionCategory")


@define
class CodatDataContractsDatasetsBankingTransactionCategory:
    """
    Attributes:
        id (str):
        name (str):
        parent_id (Union[Unset, None, str]):
        has_children (Union[Unset, bool]):
        status (Union[Unset, CodatDataContractsDatasetsBankingTransactionCategoryStatus]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    id: str
    name: str
    parent_id: Union[Unset, None, str] = UNSET
    has_children: Union[Unset, bool] = UNSET
    status: Union[Unset, CodatDataContractsDatasetsBankingTransactionCategoryStatus] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        parent_id = self.parent_id
        has_children = self.has_children
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if has_children is not UNSET:
            field_dict["hasChildren"] = has_children
        if status is not UNSET:
            field_dict["status"] = status
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        parent_id = d.pop("parentId", UNSET)

        has_children = d.pop("hasChildren", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CodatDataContractsDatasetsBankingTransactionCategoryStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodatDataContractsDatasetsBankingTransactionCategoryStatus(_status)

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

        codat_data_contracts_datasets_banking_transaction_category = cls(
            id=id,
            name=name,
            parent_id=parent_id,
            has_children=has_children,
            status=status,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_banking_transaction_category
