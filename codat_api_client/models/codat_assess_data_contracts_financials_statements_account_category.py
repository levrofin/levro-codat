from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..models.codat_assess_data_contracts_financials_statements_account_category_status import (
    CodatAssessDataContractsFinancialsStatementsAccountCategoryStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_financials_statements_account_category_level import (
        CodatAssessDataContractsFinancialsStatementsAccountCategoryLevel,
    )


T = TypeVar("T", bound="CodatAssessDataContractsFinancialsStatementsAccountCategory")


@define
class CodatAssessDataContractsFinancialsStatementsAccountCategory:
    """
    Attributes:
        status (Union[Unset, CodatAssessDataContractsFinancialsStatementsAccountCategoryStatus]):
        levels (Union[Unset, None, List['CodatAssessDataContractsFinancialsStatementsAccountCategoryLevel']]):
    """

    status: Union[Unset, CodatAssessDataContractsFinancialsStatementsAccountCategoryStatus] = UNSET
    levels: Union[Unset, None, List["CodatAssessDataContractsFinancialsStatementsAccountCategoryLevel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        levels: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.levels, Unset):
            if self.levels is None:
                levels = None
            else:
                levels = []
                for levels_item_data in self.levels:
                    levels_item = levels_item_data.to_dict()

                    levels.append(levels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if levels is not UNSET:
            field_dict["levels"] = levels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_financials_statements_account_category_level import (
            CodatAssessDataContractsFinancialsStatementsAccountCategoryLevel,
        )

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, CodatAssessDataContractsFinancialsStatementsAccountCategoryStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodatAssessDataContractsFinancialsStatementsAccountCategoryStatus(_status)

        levels = []
        _levels = d.pop("levels", UNSET)
        for levels_item_data in _levels or []:
            levels_item = CodatAssessDataContractsFinancialsStatementsAccountCategoryLevel.from_dict(levels_item_data)

            levels.append(levels_item)

        codat_assess_data_contracts_financials_statements_account_category = cls(
            status=status,
            levels=levels,
        )

        return codat_assess_data_contracts_financials_statements_account_category
