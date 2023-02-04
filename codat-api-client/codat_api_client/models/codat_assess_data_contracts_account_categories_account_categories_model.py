from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_account_categories_account_ref_model import (
        CodatAssessDataContractsAccountCategoriesAccountRefModel,
    )
    from ..models.codat_assess_data_contracts_account_categories_confirmed_account_category_model import (
        CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel,
    )
    from ..models.codat_assess_data_contracts_account_categories_suggested_account_category_model import (
        CodatAssessDataContractsAccountCategoriesSuggestedAccountCategoryModel,
    )


T = TypeVar("T", bound="CodatAssessDataContractsAccountCategoriesAccountCategoriesModel")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsAccountCategoriesAccountCategoriesModel:
    """
    Attributes:
        account_ref (Union[Unset, CodatAssessDataContractsAccountCategoriesAccountRefModel]):
        suggested (Union[Unset, CodatAssessDataContractsAccountCategoriesSuggestedAccountCategoryModel]):
        confirmed (Union[Unset, CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel]):
    """

    account_ref: Union[Unset, "CodatAssessDataContractsAccountCategoriesAccountRefModel"] = UNSET
    suggested: Union[Unset, "CodatAssessDataContractsAccountCategoriesSuggestedAccountCategoryModel"] = UNSET
    confirmed: Union[Unset, "CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        suggested: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.suggested, Unset):
            suggested = self.suggested.to_dict()

        confirmed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.confirmed, Unset):
            confirmed = self.confirmed.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if suggested is not UNSET:
            field_dict["suggested"] = suggested
        if confirmed is not UNSET:
            field_dict["confirmed"] = confirmed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_account_categories_account_ref_model import (
            CodatAssessDataContractsAccountCategoriesAccountRefModel,
        )
        from ..models.codat_assess_data_contracts_account_categories_confirmed_account_category_model import (
            CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel,
        )
        from ..models.codat_assess_data_contracts_account_categories_suggested_account_category_model import (
            CodatAssessDataContractsAccountCategoriesSuggestedAccountCategoryModel,
        )

        d = src_dict.copy()
        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, CodatAssessDataContractsAccountCategoriesAccountRefModel]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = CodatAssessDataContractsAccountCategoriesAccountRefModel.from_dict(_account_ref)

        _suggested = d.pop("suggested", UNSET)
        suggested: Union[Unset, CodatAssessDataContractsAccountCategoriesSuggestedAccountCategoryModel]
        if isinstance(_suggested, Unset):
            suggested = UNSET
        else:
            suggested = CodatAssessDataContractsAccountCategoriesSuggestedAccountCategoryModel.from_dict(_suggested)

        _confirmed = d.pop("confirmed", UNSET)
        confirmed: Union[Unset, CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel]
        if isinstance(_confirmed, Unset):
            confirmed = UNSET
        else:
            confirmed = CodatAssessDataContractsAccountCategoriesConfirmedAccountCategoryModel.from_dict(_confirmed)

        codat_assess_data_contracts_account_categories_account_categories_model = cls(
            account_ref=account_ref,
            suggested=suggested,
            confirmed=confirmed,
        )

        return codat_assess_data_contracts_account_categories_account_categories_model
