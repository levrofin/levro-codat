from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataIntegrityContractsMetadataMatchAmountInfo")


@attr.s(auto_attribs=True)
class CodatDataIntegrityContractsMetadataMatchAmountInfo:
    """
    Attributes:
        min_ (Union[Unset, None, float]):
        max_ (Union[Unset, None, float]):
        currency (Union[Unset, None, str]):
    """

    min_: Union[Unset, None, float] = UNSET
    max_: Union[Unset, None, float] = UNSET
    currency: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        min_ = self.min_
        max_ = self.max_
        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        currency = d.pop("currency", UNSET)

        codat_data_integrity_contracts_metadata_match_amount_info = cls(
            min_=min_,
            max_=max_,
            currency=currency,
        )

        return codat_data_integrity_contracts_metadata_match_amount_info
