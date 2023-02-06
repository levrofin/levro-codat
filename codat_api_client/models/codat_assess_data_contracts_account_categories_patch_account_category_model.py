from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_account_categories_confirmed_account_category_model import (
        CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel,
    )
    from ..models.codat_assess_data_contracts_account_categories_patch_account_ref_model import (
        CodatAssessDataContractsAccountCategoriesPatchAccountRefModel,
    )


T = TypeVar("T", bound="CodatAssessDataContractsAccountCategoriesPatchAccountCategoryModel")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsAccountCategoriesPatchAccountCategoryModel:
    """
    Attributes:
        account_ref (Union[Unset, CodatAssessDataContractsAccountCategoriesPatchAccountRefModel]):
        confirmed (Union[Unset, CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel]):
    """

    account_ref: Union[Unset, "CodatAssessDataContractsAccountCategoriesPatchAccountRefModel"] = UNSET
    confirmed: Union[Unset, "CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        confirmed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.confirmed, Unset):
            confirmed = self.confirmed.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if confirmed is not UNSET:
            field_dict["confirmed"] = confirmed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_account_categories_confirmed_account_category_model import (
            CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel,
        )
        from ..models.codat_assess_data_contracts_account_categories_patch_account_ref_model import (
            CodatAssessDataContractsAccountCategoriesPatchAccountRefModel,
        )

        d = src_dict.copy()
        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, CodatAssessDataContractsAccountCategoriesPatchAccountRefModel]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = CodatAssessDataContractsAccountCategoriesPatchAccountRefModel.from_dict(_account_ref)

        _confirmed = d.pop("confirmed", UNSET)
        confirmed: Union[Unset, CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel]
        if isinstance(_confirmed, Unset):
            confirmed = UNSET
        else:
            confirmed = CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel.from_dict(_confirmed)

        codat_assess_data_contracts_account_categories_patch_account_category_model = cls(
            account_ref=account_ref,
            confirmed=confirmed,
        )

        return codat_assess_data_contracts_account_categories_patch_account_category_model
