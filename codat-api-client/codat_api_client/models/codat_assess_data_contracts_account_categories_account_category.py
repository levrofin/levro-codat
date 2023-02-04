from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatAssessDataContractsAccountCategoriesAccountCategory")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsAccountCategoriesAccountCategory:
    """
    Attributes:
        type (Union[Unset, None, str]):
        subtype (Union[Unset, None, str]):
        subtype_display_name (Union[Unset, None, str]):
        detail_type (Union[Unset, None, str]):
        detail_type_display_name (Union[Unset, None, str]):
        detail_type_description (Union[Unset, None, str]):
    """

    type: Union[Unset, None, str] = UNSET
    subtype: Union[Unset, None, str] = UNSET
    subtype_display_name: Union[Unset, None, str] = UNSET
    detail_type: Union[Unset, None, str] = UNSET
    detail_type_display_name: Union[Unset, None, str] = UNSET
    detail_type_description: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        subtype = self.subtype
        subtype_display_name = self.subtype_display_name
        detail_type = self.detail_type
        detail_type_display_name = self.detail_type_display_name
        detail_type_description = self.detail_type_description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if subtype_display_name is not UNSET:
            field_dict["subtypeDisplayName"] = subtype_display_name
        if detail_type is not UNSET:
            field_dict["detailType"] = detail_type
        if detail_type_display_name is not UNSET:
            field_dict["detailTypeDisplayName"] = detail_type_display_name
        if detail_type_description is not UNSET:
            field_dict["detailTypeDescription"] = detail_type_description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        subtype = d.pop("subtype", UNSET)

        subtype_display_name = d.pop("subtypeDisplayName", UNSET)

        detail_type = d.pop("detailType", UNSET)

        detail_type_display_name = d.pop("detailTypeDisplayName", UNSET)

        detail_type_description = d.pop("detailTypeDescription", UNSET)

        codat_assess_data_contracts_account_categories_account_category = cls(
            type=type,
            subtype=subtype,
            subtype_display_name=subtype_display_name,
            detail_type=detail_type,
            detail_type_display_name=detail_type_display_name,
            detail_type_description=detail_type_description,
        )

        return codat_assess_data_contracts_account_categories_account_category
