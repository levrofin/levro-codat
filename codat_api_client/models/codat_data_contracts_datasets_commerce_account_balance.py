from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceAccountBalance")


@define
class CodatDataContractsDatasetsCommerceAccountBalance:
    """
    Attributes:
        available (Union[Unset, None, float]):
        pending (Union[Unset, None, float]):
        reserved (Union[Unset, None, float]):
        currency (Union[Unset, None, str]):
    """

    available: Union[Unset, None, float] = UNSET
    pending: Union[Unset, None, float] = UNSET
    reserved: Union[Unset, None, float] = UNSET
    currency: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        available = self.available
        pending = self.pending
        reserved = self.reserved
        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if available is not UNSET:
            field_dict["available"] = available
        if pending is not UNSET:
            field_dict["pending"] = pending
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        available = d.pop("available", UNSET)

        pending = d.pop("pending", UNSET)

        reserved = d.pop("reserved", UNSET)

        currency = d.pop("currency", UNSET)

        codat_data_contracts_datasets_commerce_account_balance = cls(
            available=available,
            pending=pending,
            reserved=reserved,
            currency=currency,
        )

        return codat_data_contracts_datasets_commerce_account_balance
