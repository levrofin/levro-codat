from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_account_categories_patch_account_category_model import (
        CodatAssessDataContractsAccountCategoriesPatchAccountCategoryModel,
    )


T = TypeVar("T", bound="CodatAssessDataContractsAccountCategoriesPatchAccountCategoriesModel")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsAccountCategoriesPatchAccountCategoriesModel:
    """
    Attributes:
        categories (Union[Unset, None, List['CodatAssessDataContractsAccountCategoriesPatchAccountCategoryModel']]):
    """

    categories: Union[Unset, None, List["CodatAssessDataContractsAccountCategoriesPatchAccountCategoryModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        categories: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            if self.categories is None:
                categories = None
            else:
                categories = []
                for categories_item_data in self.categories:
                    categories_item = categories_item_data.to_dict()

                    categories.append(categories_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_account_categories_patch_account_category_model import (
            CodatAssessDataContractsAccountCategoriesPatchAccountCategoryModel,
        )

        d = src_dict.copy()
        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = CodatAssessDataContractsAccountCategoriesPatchAccountCategoryModel.from_dict(
                categories_item_data
            )

            categories.append(categories_item)

        codat_assess_data_contracts_account_categories_patch_account_categories_model = cls(
            categories=categories,
        )

        return codat_assess_data_contracts_account_categories_patch_account_categories_model
