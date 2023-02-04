from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_account_categories_confirmed_account_category_model import (
        CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel,
    )


T = TypeVar("T", bound="CodatAssessDataContractsAccountCategoriesPatchSingleAccountCategoryModel")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsAccountCategoriesPatchSingleAccountCategoryModel:
    """
    Attributes:
        confirmed (Union[Unset, CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel]):
    """

    confirmed: Union[Unset, "CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        confirmed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.confirmed, Unset):
            confirmed = self.confirmed.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if confirmed is not UNSET:
            field_dict["confirmed"] = confirmed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_account_categories_confirmed_account_category_model import (
            CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel,
        )

        d = src_dict.copy()
        _confirmed = d.pop("confirmed", UNSET)
        confirmed: Union[Unset, CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel]
        if isinstance(_confirmed, Unset):
            confirmed = UNSET
        else:
            confirmed = CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel.from_dict(_confirmed)

        codat_assess_data_contracts_account_categories_patch_single_account_category_model = cls(
            confirmed=confirmed,
        )

        return codat_assess_data_contracts_account_categories_patch_single_account_category_model
