from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataIntegrityContractsSummaryMatchCountSummary")


@define
class CodatDataIntegrityContractsSummaryMatchCountSummary:
    """
    Attributes:
        match_percentage (Union[Unset, float]):
        unmatched (Union[Unset, int]):
        matched (Union[Unset, int]):
        total (Union[Unset, int]):
    """

    match_percentage: Union[Unset, float] = UNSET
    unmatched: Union[Unset, int] = UNSET
    matched: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        match_percentage = self.match_percentage
        unmatched = self.unmatched
        matched = self.matched
        total = self.total

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        match_percentage = d.pop("matchPercentage", UNSET)

        unmatched = d.pop("unmatched", UNSET)

        matched = d.pop("matched", UNSET)

        total = d.pop("total", UNSET)

        codat_data_integrity_contracts_summary_match_count_summary = cls(
            match_percentage=match_percentage,
            unmatched=unmatched,
            matched=matched,
            total=total,
        )

        return codat_data_integrity_contracts_summary_match_count_summary
