import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_integrity_contracts_reports_banking_transaction_ref import (
        CodatDataIntegrityContractsReportsBankingTransactionRef,
    )


T = TypeVar("T", bound="CodatDataIntegrityContractsReportsPayment")


@define
class CodatDataIntegrityContractsReportsPayment:
    """
    Attributes:
        id (Union[Unset, None, str]):
        date (Union[Unset, datetime.datetime]):
        payment_type (Union[Unset, None, str]):
        amount (Union[Unset, float]):
        currency (Union[Unset, None, str]):
        currency_rate (Union[Unset, None, float]):
        banking_transaction_refs (Union[Unset, None, List['CodatDataIntegrityContractsReportsBankingTransactionRef']]):
    """

    id: Union[Unset, None, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    payment_type: Union[Unset, None, str] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, None, str] = UNSET
    currency_rate: Union[Unset, None, float] = UNSET
    banking_transaction_refs: Union[
        Unset, None, List["CodatDataIntegrityContractsReportsBankingTransactionRef"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        payment_type = self.payment_type
        amount = self.amount
        currency = self.currency
        currency_rate = self.currency_rate
        banking_transaction_refs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.banking_transaction_refs, Unset):
            if self.banking_transaction_refs is None:
                banking_transaction_refs = None
            else:
                banking_transaction_refs = []
                for banking_transaction_refs_item_data in self.banking_transaction_refs:
                    banking_transaction_refs_item = banking_transaction_refs_item_data.to_dict()

                    banking_transaction_refs.append(banking_transaction_refs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if date is not UNSET:
            field_dict["date"] = date
        if payment_type is not UNSET:
            field_dict["paymentType"] = payment_type
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if banking_transaction_refs is not UNSET:
            field_dict["bankingTransactionRefs"] = banking_transaction_refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_integrity_contracts_reports_banking_transaction_ref import (
            CodatDataIntegrityContractsReportsBankingTransactionRef,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        payment_type = d.pop("paymentType", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        banking_transaction_refs = []
        _banking_transaction_refs = d.pop("bankingTransactionRefs", UNSET)
        for banking_transaction_refs_item_data in _banking_transaction_refs or []:
            banking_transaction_refs_item = CodatDataIntegrityContractsReportsBankingTransactionRef.from_dict(
                banking_transaction_refs_item_data
            )

            banking_transaction_refs.append(banking_transaction_refs_item)

        codat_data_integrity_contracts_reports_payment = cls(
            id=id,
            date=date,
            payment_type=payment_type,
            amount=amount,
            currency=currency,
            currency_rate=currency_rate,
            banking_transaction_refs=banking_transaction_refs,
        )

        return codat_data_integrity_contracts_reports_payment
