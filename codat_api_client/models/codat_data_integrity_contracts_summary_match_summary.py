from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_integrity_contracts_summary_match_amount_summary import (
        CodatDataIntegrityContractsSummaryMatchAmountSummary,
    )
    from ..models.codat_data_integrity_contracts_summary_match_count_summary import (
        CodatDataIntegrityContractsSummaryMatchCountSummary,
    )


T = TypeVar("T", bound="CodatDataIntegrityContractsSummaryMatchSummary")


@define
class CodatDataIntegrityContractsSummaryMatchSummary:
    """
    Attributes:
        type (Union[Unset, None, str]):
        by_amount (Union[Unset, CodatDataIntegrityContractsSummaryMatchAmountSummary]):
        by_count (Union[Unset, CodatDataIntegrityContractsSummaryMatchCountSummary]):
    """

    type: Union[Unset, None, str] = UNSET
    by_amount: Union[Unset, "CodatDataIntegrityContractsSummaryMatchAmountSummary"] = UNSET
    by_count: Union[Unset, "CodatDataIntegrityContractsSummaryMatchCountSummary"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        by_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by_amount, Unset):
            by_amount = self.by_amount.to_dict()

        by_count: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by_count, Unset):
            by_count = self.by_count.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if by_amount is not UNSET:
            field_dict["byAmount"] = by_amount
        if by_count is not UNSET:
            field_dict["byCount"] = by_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_integrity_contracts_summary_match_amount_summary import (
            CodatDataIntegrityContractsSummaryMatchAmountSummary,
        )
        from ..models.codat_data_integrity_contracts_summary_match_count_summary import (
            CodatDataIntegrityContractsSummaryMatchCountSummary,
        )

        d = src_dict.copy()
        type = d.pop("type", UNSET)

        _by_amount = d.pop("byAmount", UNSET)
        by_amount: Union[Unset, CodatDataIntegrityContractsSummaryMatchAmountSummary]
        if isinstance(_by_amount, Unset):
            by_amount = UNSET
        else:
            by_amount = CodatDataIntegrityContractsSummaryMatchAmountSummary.from_dict(_by_amount)

        _by_count = d.pop("byCount", UNSET)
        by_count: Union[Unset, CodatDataIntegrityContractsSummaryMatchCountSummary]
        if isinstance(_by_count, Unset):
            by_count = UNSET
        else:
            by_count = CodatDataIntegrityContractsSummaryMatchCountSummary.from_dict(_by_count)

        codat_data_integrity_contracts_summary_match_summary = cls(
            type=type,
            by_amount=by_amount,
            by_count=by_count,
        )

        return codat_data_integrity_contracts_summary_match_summary
