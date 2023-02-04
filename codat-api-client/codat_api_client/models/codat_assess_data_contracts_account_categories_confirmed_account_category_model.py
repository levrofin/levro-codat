import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel:
    """
    Attributes:
        type (Union[Unset, None, str]):
        subtype (Union[Unset, None, str]):
        detail_type (Union[Unset, None, str]):
        modified_date (Union[Unset, None, datetime.datetime]):
    """

    type: Union[Unset, None, str] = UNSET
    subtype: Union[Unset, None, str] = UNSET
    detail_type: Union[Unset, None, str] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        subtype = self.subtype
        detail_type = self.detail_type
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if detail_type is not UNSET:
            field_dict["detailType"] = detail_type
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        subtype = d.pop("subtype", UNSET)

        detail_type = d.pop("detailType", UNSET)

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: Union[Unset, None, datetime.datetime]
        if _modified_date is None:
            modified_date = None
        elif isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        codat_assess_data_contracts_account_categories_confirmed_account_category_model = cls(
            type=type,
            subtype=subtype,
            detail_type=detail_type,
            modified_date=modified_date,
        )

        return codat_assess_data_contracts_account_categories_confirmed_account_category_model
