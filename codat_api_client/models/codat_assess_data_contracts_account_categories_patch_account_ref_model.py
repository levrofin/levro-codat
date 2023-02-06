from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatAssessDataContractsAccountCategoriesPatchAccountRefModel")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsAccountCategoriesPatchAccountRefModel:
    """
    Attributes:
        id (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        codat_assess_data_contracts_account_categories_patch_account_ref_model = cls(
            id=id,
        )

        return codat_assess_data_contracts_account_categories_patch_account_ref_model
