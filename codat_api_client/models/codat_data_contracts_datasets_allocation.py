import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsAllocation")


@define
class CodatDataContractsDatasetsAllocation:
    """
    Attributes:
        currency (Union[Unset, None, str]):
        currency_rate (Union[Unset, None, float]):
        allocated_on_date (Union[Unset, None, datetime.datetime]):
        total_amount (Union[Unset, float]):
    """

    currency: Union[Unset, None, str] = UNSET
    currency_rate: Union[Unset, None, float] = UNSET
    allocated_on_date: Union[Unset, None, datetime.datetime] = UNSET
    total_amount: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency
        currency_rate = self.currency_rate
        allocated_on_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.allocated_on_date, Unset):
            allocated_on_date = self.allocated_on_date.isoformat() if self.allocated_on_date else None

        total_amount = self.total_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if allocated_on_date is not UNSET:
            field_dict["allocatedOnDate"] = allocated_on_date
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        _allocated_on_date = d.pop("allocatedOnDate", UNSET)
        allocated_on_date: Union[Unset, None, datetime.datetime]
        if _allocated_on_date is None:
            allocated_on_date = None
        elif isinstance(_allocated_on_date, Unset):
            allocated_on_date = UNSET
        else:
            allocated_on_date = isoparse(_allocated_on_date)

        total_amount = d.pop("totalAmount", UNSET)

        codat_data_contracts_datasets_allocation = cls(
            currency=currency,
            currency_rate=currency_rate,
            allocated_on_date=allocated_on_date,
            total_amount=total_amount,
        )

        return codat_data_contracts_datasets_allocation
