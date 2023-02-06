from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsBankingAccountBalanceAmounts")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsBankingAccountBalanceAmounts:
    """
    Attributes:
        current (float):
        available (Union[Unset, None, float]):
        limit (Union[Unset, None, float]):
    """

    current: float
    available: Union[Unset, None, float] = UNSET
    limit: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        current = self.current
        available = self.available
        limit = self.limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "current": current,
            }
        )
        if available is not UNSET:
            field_dict["available"] = available
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current = d.pop("current")

        available = d.pop("available", UNSET)

        limit = d.pop("limit", UNSET)

        codat_data_contracts_datasets_banking_account_balance_amounts = cls(
            current=current,
            available=available,
            limit=limit,
        )

        return codat_data_contracts_datasets_banking_account_balance_amounts
