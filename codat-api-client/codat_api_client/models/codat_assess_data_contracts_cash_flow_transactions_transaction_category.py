from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatAssessDataContractsCashFlowTransactionsTransactionCategory")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsCashFlowTransactionsTransactionCategory:
    """
    Attributes:
        confidence (Union[Unset, None, float]):
        levels (Union[Unset, None, List[str]]):
    """

    confidence: Union[Unset, None, float] = UNSET
    levels: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        confidence = self.confidence
        levels: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.levels, Unset):
            if self.levels is None:
                levels = None
            else:
                levels = self.levels

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if levels is not UNSET:
            field_dict["levels"] = levels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        confidence = d.pop("confidence", UNSET)

        levels = cast(List[str], d.pop("levels", UNSET))

        codat_assess_data_contracts_cash_flow_transactions_transaction_category = cls(
            confidence=confidence,
            levels=levels,
        )

        return codat_assess_data_contracts_cash_flow_transactions_transaction_category
