import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_account_ref import CodatDataContractsDatasetsAccountRef


T = TypeVar("T", bound="CodatDataContractsDatasetsPaymentAllocationPayment")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsPaymentAllocationPayment:
    """
    Attributes:
        id (Union[Unset, None, str]):
        note (Union[Unset, None, str]):
        reference (Union[Unset, None, str]):
        account_ref (Union[Unset, CodatDataContractsDatasetsAccountRef]):
        currency (Union[Unset, None, str]):
        currency_rate (Union[Unset, None, float]):
        paid_on_date (Union[Unset, datetime.datetime]):
        total_amount (Union[Unset, float]):
    """

    id: Union[Unset, None, str] = UNSET
    note: Union[Unset, None, str] = UNSET
    reference: Union[Unset, None, str] = UNSET
    account_ref: Union[Unset, "CodatDataContractsDatasetsAccountRef"] = UNSET
    currency: Union[Unset, None, str] = UNSET
    currency_rate: Union[Unset, None, float] = UNSET
    paid_on_date: Union[Unset, datetime.datetime] = UNSET
    total_amount: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        note = self.note
        reference = self.reference
        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        currency = self.currency
        currency_rate = self.currency_rate
        paid_on_date: Union[Unset, str] = UNSET
        if not isinstance(self.paid_on_date, Unset):
            paid_on_date = self.paid_on_date.isoformat()

        total_amount = self.total_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if note is not UNSET:
            field_dict["note"] = note
        if reference is not UNSET:
            field_dict["reference"] = reference
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if paid_on_date is not UNSET:
            field_dict["paidOnDate"] = paid_on_date
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_account_ref import CodatDataContractsDatasetsAccountRef

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        note = d.pop("note", UNSET)

        reference = d.pop("reference", UNSET)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, CodatDataContractsDatasetsAccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = CodatDataContractsDatasetsAccountRef.from_dict(_account_ref)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        _paid_on_date = d.pop("paidOnDate", UNSET)
        paid_on_date: Union[Unset, datetime.datetime]
        if isinstance(_paid_on_date, Unset):
            paid_on_date = UNSET
        else:
            paid_on_date = isoparse(_paid_on_date)

        total_amount = d.pop("totalAmount", UNSET)

        codat_data_contracts_datasets_payment_allocation_payment = cls(
            id=id,
            note=note,
            reference=reference,
            account_ref=account_ref,
            currency=currency,
            currency_rate=currency_rate,
            paid_on_date=paid_on_date,
            total_amount=total_amount,
        )

        return codat_data_contracts_datasets_payment_allocation_payment
