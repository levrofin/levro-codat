from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_integrity_contracts_summary_match_summary import (
        CodatDataIntegrityContractsSummaryMatchSummary,
    )


T = TypeVar("T", bound="CodatDataIntegrityContractsSummaryMatchSummariesResponse")


@define
class CodatDataIntegrityContractsSummaryMatchSummariesResponse:
    """
    Attributes:
        summaries (Union[Unset, None, List['CodatDataIntegrityContractsSummaryMatchSummary']]):
    """

    summaries: Union[Unset, None, List["CodatDataIntegrityContractsSummaryMatchSummary"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        summaries: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.summaries, Unset):
            if self.summaries is None:
                summaries = None
            else:
                summaries = []
                for summaries_item_data in self.summaries:
                    summaries_item = summaries_item_data.to_dict()

                    summaries.append(summaries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if summaries is not UNSET:
            field_dict["summaries"] = summaries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_integrity_contracts_summary_match_summary import (
            CodatDataIntegrityContractsSummaryMatchSummary,
        )

        d = src_dict.copy()
        summaries = []
        _summaries = d.pop("summaries", UNSET)
        for summaries_item_data in _summaries or []:
            summaries_item = CodatDataIntegrityContractsSummaryMatchSummary.from_dict(summaries_item_data)

            summaries.append(summaries_item)

        codat_data_integrity_contracts_summary_match_summaries_response = cls(
            summaries=summaries,
        )

        return codat_data_integrity_contracts_summary_match_summaries_response
