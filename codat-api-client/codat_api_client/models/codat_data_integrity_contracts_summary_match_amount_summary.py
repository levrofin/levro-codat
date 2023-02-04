from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataIntegrityContractsSummaryMatchAmountSummary")


@attr.s(auto_attribs=True)
class CodatDataIntegrityContractsSummaryMatchAmountSummary:
    """
    Attributes:
        match_percentage (Union[Unset, float]):
        unmatched (Union[Unset, float]):
        matched (Union[Unset, float]):
        total (Union[Unset, float]):
        currency (Union[Unset, None, str]):
    """

    match_percentage: Union[Unset, float] = UNSET
    unmatched: Union[Unset, float] = UNSET
    matched: Union[Unset, float] = UNSET
    total: Union[Unset, float] = UNSET
    currency: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        match_percentage = self.match_percentage
        unmatched = self.unmatched
        matched = self.matched
        total = self.total
        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if match_percentage is not UNSET:
            field_dict["matchPercentage"] = match_percentage
        if unmatched is not UNSET:
            field_dict["unmatched"] = unmatched
        if matched is not UNSET:
            field_dict["matched"] = matched
        if total is not UNSET:
            field_dict["total"] = total
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        match_percentage = d.pop("matchPercentage", UNSET)

        unmatched = d.pop("unmatched", UNSET)

        matched = d.pop("matched", UNSET)

        total = d.pop("total", UNSET)

        currency = d.pop("currency", UNSET)

        codat_data_integrity_contracts_summary_match_amount_summary = cls(
            match_percentage=match_percentage,
            unmatched=unmatched,
            matched=matched,
            total=total,
            currency=currency,
        )

        return codat_data_integrity_contracts_summary_match_amount_summary
