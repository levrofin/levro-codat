import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_ancestor_ref import (
        CodatDataContractsDatasetsCommerceAncestorRef,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceProductCategory")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCommerceProductCategory:
    """
    Attributes:
        id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        ancestor_refs (Union[Unset, None, List['CodatDataContractsDatasetsCommerceAncestorRef']]):
        has_children (Union[Unset, bool]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    ancestor_refs: Union[Unset, None, List["CodatDataContractsDatasetsCommerceAncestorRef"]] = UNSET
    has_children: Union[Unset, bool] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        ancestor_refs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ancestor_refs, Unset):
            if self.ancestor_refs is None:
                ancestor_refs = None
            else:
                ancestor_refs = []
                for ancestor_refs_item_data in self.ancestor_refs:
                    ancestor_refs_item = ancestor_refs_item_data.to_dict()

                    ancestor_refs.append(ancestor_refs_item)

        has_children = self.has_children
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if ancestor_refs is not UNSET:
            field_dict["ancestorRefs"] = ancestor_refs
        if has_children is not UNSET:
            field_dict["hasChildren"] = has_children
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_commerce_ancestor_ref import (
            CodatDataContractsDatasetsCommerceAncestorRef,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        ancestor_refs = []
        _ancestor_refs = d.pop("ancestorRefs", UNSET)
        for ancestor_refs_item_data in _ancestor_refs or []:
            ancestor_refs_item = CodatDataContractsDatasetsCommerceAncestorRef.from_dict(ancestor_refs_item_data)

            ancestor_refs.append(ancestor_refs_item)

        has_children = d.pop("hasChildren", UNSET)

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

        codat_data_contracts_datasets_commerce_product_category = cls(
            id=id,
            name=name,
            ancestor_refs=ancestor_refs,
            has_children=has_children,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_commerce_product_category
