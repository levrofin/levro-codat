import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_tracking_category_status import (
    CodatDataContractsDatasetsTrackingCategoryStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsDataTrackingCategoryTree")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsDataTrackingCategoryTree:
    """
    Attributes:
        sub_categories (Union[Unset, None, List['CodatPublicApiModelsDataTrackingCategoryTree']]):
        id (Union[Unset, None, str]): The identifier for the item, unique per tracking category
        parent_id (Union[Unset, None, str]): The identifier for this item's immediate parent
        modified_date (Union[Unset, None, datetime.datetime]): The date the record was last updated in the system cache
        source_modified_date (Union[Unset, None, datetime.datetime]): The date the record was last changed in the
            originating system
        name (Union[Unset, None, str]): The name of the tracking category
        has_children (Union[Unset, bool]): Boolean value indicating whether this category has SubCategories
        status (Union[Unset, CodatDataContractsDatasetsTrackingCategoryStatus]):
    """

    sub_categories: Union[Unset, None, List["CodatPublicApiModelsDataTrackingCategoryTree"]] = UNSET
    id: Union[Unset, None, str] = UNSET
    parent_id: Union[Unset, None, str] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, None, str] = UNSET
    has_children: Union[Unset, bool] = UNSET
    status: Union[Unset, CodatDataContractsDatasetsTrackingCategoryStatus] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        sub_categories: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sub_categories, Unset):
            if self.sub_categories is None:
                sub_categories = None
            else:
                sub_categories = []
                for sub_categories_item_data in self.sub_categories:
                    sub_categories_item = sub_categories_item_data.to_dict()

                    sub_categories.append(sub_categories_item)

        id = self.id
        parent_id = self.parent_id
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        name = self.name
        has_children = self.has_children
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if sub_categories is not UNSET:
            field_dict["subCategories"] = sub_categories
        if id is not UNSET:
            field_dict["id"] = id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if name is not UNSET:
            field_dict["name"] = name
        if has_children is not UNSET:
            field_dict["hasChildren"] = has_children
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sub_categories = []
        _sub_categories = d.pop("subCategories", UNSET)
        for sub_categories_item_data in _sub_categories or []:
            sub_categories_item = CodatPublicApiModelsDataTrackingCategoryTree.from_dict(sub_categories_item_data)

            sub_categories.append(sub_categories_item)

        id = d.pop("id", UNSET)

        parent_id = d.pop("parentId", UNSET)

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

        name = d.pop("name", UNSET)

        has_children = d.pop("hasChildren", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CodatDataContractsDatasetsTrackingCategoryStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodatDataContractsDatasetsTrackingCategoryStatus(_status)

        codat_public_api_models_data_tracking_category_tree = cls(
            sub_categories=sub_categories,
            id=id,
            parent_id=parent_id,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            name=name,
            has_children=has_children,
            status=status,
        )

        return codat_public_api_models_data_tracking_category_tree
