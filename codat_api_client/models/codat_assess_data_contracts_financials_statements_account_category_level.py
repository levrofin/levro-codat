from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatAssessDataContractsFinancialsStatementsAccountCategoryLevel")


@define
class CodatAssessDataContractsFinancialsStatementsAccountCategoryLevel:
    """
    Attributes:
        level_name (Union[Unset, None, str]):
        confidence (Union[Unset, None, float]):
    """

    level_name: Union[Unset, None, str] = UNSET
    confidence: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        level_name = self.level_name
        confidence = self.confidence

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if level_name is not UNSET:
            field_dict["levelName"] = level_name
        if confidence is not UNSET:
            field_dict["confidence"] = confidence

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        level_name = d.pop("levelName", UNSET)

        confidence = d.pop("confidence", UNSET)

        codat_assess_data_contracts_financials_statements_account_category_level = cls(
            level_name=level_name,
            confidence=confidence,
        )

        return codat_assess_data_contracts_financials_statements_account_category_level
