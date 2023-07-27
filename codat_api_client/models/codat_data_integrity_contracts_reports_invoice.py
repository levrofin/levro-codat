import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_integrity_contracts_reports_customer_ref import (
        CodatDataIntegrityContractsReportsCustomerRef,
    )
    from ..models.codat_data_integrity_contracts_reports_payment import CodatDataIntegrityContractsReportsPayment


T = TypeVar("T", bound="CodatDataIntegrityContractsReportsInvoice")


@define
class CodatDataIntegrityContractsReportsInvoice:
    """
    Attributes:
        id (Union[Unset, None, str]):
        invoice_number (Union[Unset, None, str]):
        customer_ref (Union[Unset, CodatDataIntegrityContractsReportsCustomerRef]):
        issue_date (Union[Unset, datetime.datetime]):
        due_date (Union[Unset, None, datetime.datetime]):
        status (Union[Unset, None, str]):
        currency (Union[Unset, None, str]):
        total_amount (Union[Unset, float]):
        amount_due (Union[Unset, float]):
        paid_on_date (Union[Unset, None, datetime.datetime]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        payments (Union[Unset, None, List['CodatDataIntegrityContractsReportsPayment']]):
    """

    id: Union[Unset, None, str] = UNSET
    invoice_number: Union[Unset, None, str] = UNSET
    customer_ref: Union[Unset, "CodatDataIntegrityContractsReportsCustomerRef"] = UNSET
    issue_date: Union[Unset, datetime.datetime] = UNSET
    due_date: Union[Unset, None, datetime.datetime] = UNSET
    status: Union[Unset, None, str] = UNSET
    currency: Union[Unset, None, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    amount_due: Union[Unset, float] = UNSET
    paid_on_date: Union[Unset, None, datetime.datetime] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    payments: Union[Unset, None, List["CodatDataIntegrityContractsReportsPayment"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        invoice_number = self.invoice_number
        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        issue_date: Union[Unset, str] = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        due_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat() if self.due_date else None

        status = self.status
        currency = self.currency
        total_amount = self.total_amount
        amount_due = self.amount_due
        paid_on_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.paid_on_date, Unset):
            paid_on_date = self.paid_on_date.isoformat() if self.paid_on_date else None

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        payments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payments, Unset):
            if self.payments is None:
                payments = None
            else:
                payments = []
                for payments_item_data in self.payments:
                    payments_item = payments_item_data.to_dict()

                    payments.append(payments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if issue_date is not UNSET:
            field_dict["issueDate"] = issue_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if status is not UNSET:
            field_dict["status"] = status
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if amount_due is not UNSET:
            field_dict["amountDue"] = amount_due
        if paid_on_date is not UNSET:
            field_dict["paidOnDate"] = paid_on_date
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if payments is not UNSET:
            field_dict["payments"] = payments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_integrity_contracts_reports_customer_ref import (
            CodatDataIntegrityContractsReportsCustomerRef,
        )
        from ..models.codat_data_integrity_contracts_reports_payment import CodatDataIntegrityContractsReportsPayment

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        invoice_number = d.pop("invoiceNumber", UNSET)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CodatDataIntegrityContractsReportsCustomerRef]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CodatDataIntegrityContractsReportsCustomerRef.from_dict(_customer_ref)

        _issue_date = d.pop("issueDate", UNSET)
        issue_date: Union[Unset, datetime.datetime]
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = isoparse(_issue_date)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, None, datetime.datetime]
        if _due_date is None:
            due_date = None
        elif isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        status = d.pop("status", UNSET)

        currency = d.pop("currency", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        amount_due = d.pop("amountDue", UNSET)

        _paid_on_date = d.pop("paidOnDate", UNSET)
        paid_on_date: Union[Unset, None, datetime.datetime]
        if _paid_on_date is None:
            paid_on_date = None
        elif isinstance(_paid_on_date, Unset):
            paid_on_date = UNSET
        else:
            paid_on_date = isoparse(_paid_on_date)

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: Union[Unset, None, datetime.datetime]
        if _modified_date is None:
            modified_date = None
        elif isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, None, datetime.datetime]
        if _source_modified_date is None:
            source_modified_date = None
        elif isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        payments = []
        _payments = d.pop("payments", UNSET)
        for payments_item_data in _payments or []:
            payments_item = CodatDataIntegrityContractsReportsPayment.from_dict(payments_item_data)

            payments.append(payments_item)

        codat_data_integrity_contracts_reports_invoice = cls(
            id=id,
            invoice_number=invoice_number,
            customer_ref=customer_ref,
            issue_date=issue_date,
            due_date=due_date,
            status=status,
            currency=currency,
            total_amount=total_amount,
            amount_due=amount_due,
            paid_on_date=paid_on_date,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            payments=payments,
        )

        return codat_data_integrity_contracts_reports_invoice
