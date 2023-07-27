from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..models.codat_assess_data_contracts_cash_flow_transactions_source_type import (
    CodatAssessDataContractsCashFlowTransactionsSourceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatAssessDataContractsCashFlowTransactionsSourceRef")


@define
class CodatAssessDataContractsCashFlowTransactionsSourceRef:
    """
    Attributes:
        source_type (Union[Unset, CodatAssessDataContractsCashFlowTransactionsSourceType]):
    """

    source_type: Union[Unset, CodatAssessDataContractsCashFlowTransactionsSourceType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        source_type: Union[Unset, str] = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _source_type = d.pop("sourceType", UNSET)
        source_type: Union[Unset, CodatAssessDataContractsCashFlowTransactionsSourceType]
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = CodatAssessDataContractsCashFlowTransactionsSourceType(_source_type)

        codat_assess_data_contracts_cash_flow_transactions_source_ref = cls(
            source_type=source_type,
        )

        return codat_assess_data_contracts_cash_flow_transactions_source_ref
