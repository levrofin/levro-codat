import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_invoice_status import CodatDataContractsDatasetsInvoiceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_customer_ref import CodatDataContractsDatasetsCustomerRef
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
        CodatDataContractsDatasetsDataInterfacesSupplementalData,
    )
    from ..models.codat_data_contracts_datasets_detailed_payment_allocation import (
        CodatDataContractsDatasetsDetailedPaymentAllocation,
    )
    from ..models.codat_data_contracts_datasets_invoice_line_item import CodatDataContractsDatasetsInvoiceLineItem
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
    from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef
    from ..models.codat_data_contracts_datasets_withholding_tax import CodatDataContractsDatasetsWithholdingTax


T = TypeVar("T", bound="CodatDataContractsDatasetsInvoice")


@define
class CodatDataContractsDatasetsInvoice:
    """
    Attributes:
        issue_date (datetime.datetime):
        total_tax_amount (float):
        total_amount (float):
        amount_due (float):
        status (CodatDataContractsDatasetsInvoiceStatus):
        id (Union[Unset, None, str]):
        invoice_number (Union[Unset, None, str]):
        customer_ref (Union[Unset, CodatDataContractsDatasetsCustomerRef]):
        sales_order_refs (Union[Unset, None, List['CodatDataContractsDatasetsRecordRef']]):
        due_date (Union[Unset, None, datetime.datetime]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        paid_on_date (Union[Unset, None, datetime.datetime]):
        currency (Union[Unset, None, str]):
        currency_rate (Union[Unset, None, float]):
        line_items (Union[Unset, None, List['CodatDataContractsDatasetsInvoiceLineItem']]):
        payment_allocations (Union[Unset, None, List['CodatDataContractsDatasetsDetailedPaymentAllocation']]):
        withholding_tax (Union[Unset, None, List['CodatDataContractsDatasetsWithholdingTax']]):
        total_discount (Union[Unset, None, float]):
        sub_total (Union[Unset, None, float]):
        additional_tax_amount (Union[Unset, float]):
        additional_tax_percentage (Union[Unset, float]):
        discount_percentage (Union[Unset, None, float]):
        note (Union[Unset, None, str]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
        supplemental_data (Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]):
    """

    issue_date: datetime.datetime
    total_tax_amount: float
    total_amount: float
    amount_due: float
    status: CodatDataContractsDatasetsInvoiceStatus
    id: Union[Unset, None, str] = UNSET
    invoice_number: Union[Unset, None, str] = UNSET
    customer_ref: Union[Unset, "CodatDataContractsDatasetsCustomerRef"] = UNSET
    sales_order_refs: Union[Unset, None, List["CodatDataContractsDatasetsRecordRef"]] = UNSET
    due_date: Union[Unset, None, datetime.datetime] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    paid_on_date: Union[Unset, None, datetime.datetime] = UNSET
    currency: Union[Unset, None, str] = UNSET
    currency_rate: Union[Unset, None, float] = UNSET
    line_items: Union[Unset, None, List["CodatDataContractsDatasetsInvoiceLineItem"]] = UNSET
    payment_allocations: Union[Unset, None, List["CodatDataContractsDatasetsDetailedPaymentAllocation"]] = UNSET
    withholding_tax: Union[Unset, None, List["CodatDataContractsDatasetsWithholdingTax"]] = UNSET
    total_discount: Union[Unset, None, float] = UNSET
    sub_total: Union[Unset, None, float] = UNSET
    additional_tax_amount: Union[Unset, float] = UNSET
    additional_tax_percentage: Union[Unset, float] = UNSET
    discount_percentage: Union[Unset, None, float] = UNSET
    note: Union[Unset, None, str] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET
    supplemental_data: Union[Unset, "CodatDataContractsDatasetsDataInterfacesSupplementalData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        issue_date = self.issue_date.isoformat()

        total_tax_amount = self.total_tax_amount
        total_amount = self.total_amount
        amount_due = self.amount_due
        status = self.status.value

        id = self.id
        invoice_number = self.invoice_number
        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        sales_order_refs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sales_order_refs, Unset):
            if self.sales_order_refs is None:
                sales_order_refs = None
            else:
                sales_order_refs = []
                for sales_order_refs_item_data in self.sales_order_refs:
                    sales_order_refs_item = sales_order_refs_item_data.to_dict()

                    sales_order_refs.append(sales_order_refs_item)

        due_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat() if self.due_date else None

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        paid_on_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.paid_on_date, Unset):
            paid_on_date = self.paid_on_date.isoformat() if self.paid_on_date else None

        currency = self.currency
        currency_rate = self.currency_rate
        line_items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_items, Unset):
            if self.line_items is None:
                line_items = None
            else:
                line_items = []
                for line_items_item_data in self.line_items:
                    line_items_item = line_items_item_data.to_dict()

                    line_items.append(line_items_item)

        payment_allocations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payment_allocations, Unset):
            if self.payment_allocations is None:
                payment_allocations = None
            else:
                payment_allocations = []
                for payment_allocations_item_data in self.payment_allocations:
                    payment_allocations_item = payment_allocations_item_data.to_dict()

                    payment_allocations.append(payment_allocations_item)

        withholding_tax: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.withholding_tax, Unset):
            if self.withholding_tax is None:
                withholding_tax = None
            else:
                withholding_tax = []
                for withholding_tax_item_data in self.withholding_tax:
                    withholding_tax_item = withholding_tax_item_data.to_dict()

                    withholding_tax.append(withholding_tax_item)

        total_discount = self.total_discount
        sub_total = self.sub_total
        additional_tax_amount = self.additional_tax_amount
        additional_tax_percentage = self.additional_tax_percentage
        discount_percentage = self.discount_percentage
        note = self.note
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        supplemental_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplemental_data, Unset):
            supplemental_data = self.supplemental_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "issueDate": issue_date,
                "totalTaxAmount": total_tax_amount,
                "totalAmount": total_amount,
                "amountDue": amount_due,
                "status": status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if sales_order_refs is not UNSET:
            field_dict["salesOrderRefs"] = sales_order_refs
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if paid_on_date is not UNSET:
            field_dict["paidOnDate"] = paid_on_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items
        if payment_allocations is not UNSET:
            field_dict["paymentAllocations"] = payment_allocations
        if withholding_tax is not UNSET:
            field_dict["withholdingTax"] = withholding_tax
        if total_discount is not UNSET:
            field_dict["totalDiscount"] = total_discount
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if additional_tax_amount is not UNSET:
            field_dict["additionalTaxAmount"] = additional_tax_amount
        if additional_tax_percentage is not UNSET:
            field_dict["additionalTaxPercentage"] = additional_tax_percentage
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if note is not UNSET:
            field_dict["note"] = note
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if supplemental_data is not UNSET:
            field_dict["supplementalData"] = supplemental_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_customer_ref import CodatDataContractsDatasetsCustomerRef
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
            CodatDataContractsDatasetsDataInterfacesSupplementalData,
        )
        from ..models.codat_data_contracts_datasets_detailed_payment_allocation import (
            CodatDataContractsDatasetsDetailedPaymentAllocation,
        )
        from ..models.codat_data_contracts_datasets_invoice_line_item import CodatDataContractsDatasetsInvoiceLineItem
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
        from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef
        from ..models.codat_data_contracts_datasets_withholding_tax import CodatDataContractsDatasetsWithholdingTax

        d = src_dict.copy()
        issue_date = isoparse(d.pop("issueDate"))

        total_tax_amount = d.pop("totalTaxAmount")

        total_amount = d.pop("totalAmount")

        amount_due = d.pop("amountDue")

        status = CodatDataContractsDatasetsInvoiceStatus(d.pop("status"))

        id = d.pop("id", UNSET)

        invoice_number = d.pop("invoiceNumber", UNSET)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CodatDataContractsDatasetsCustomerRef]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CodatDataContractsDatasetsCustomerRef.from_dict(_customer_ref)

        sales_order_refs = []
        _sales_order_refs = d.pop("salesOrderRefs", UNSET)
        for sales_order_refs_item_data in _sales_order_refs or []:
            sales_order_refs_item = CodatDataContractsDatasetsRecordRef.from_dict(sales_order_refs_item_data)

            sales_order_refs.append(sales_order_refs_item)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, None, datetime.datetime]
        if _due_date is None:
            due_date = None
        elif isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

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

        _paid_on_date = d.pop("paidOnDate", UNSET)
        paid_on_date: Union[Unset, None, datetime.datetime]
        if _paid_on_date is None:
            paid_on_date = None
        elif isinstance(_paid_on_date, Unset):
            paid_on_date = UNSET
        else:
            paid_on_date = isoparse(_paid_on_date)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        line_items = []
        _line_items = d.pop("lineItems", UNSET)
        for line_items_item_data in _line_items or []:
            line_items_item = CodatDataContractsDatasetsInvoiceLineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        payment_allocations = []
        _payment_allocations = d.pop("paymentAllocations", UNSET)
        for payment_allocations_item_data in _payment_allocations or []:
            payment_allocations_item = CodatDataContractsDatasetsDetailedPaymentAllocation.from_dict(
                payment_allocations_item_data
            )

            payment_allocations.append(payment_allocations_item)

        withholding_tax = []
        _withholding_tax = d.pop("withholdingTax", UNSET)
        for withholding_tax_item_data in _withholding_tax or []:
            withholding_tax_item = CodatDataContractsDatasetsWithholdingTax.from_dict(withholding_tax_item_data)

            withholding_tax.append(withholding_tax_item)

        total_discount = d.pop("totalDiscount", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        additional_tax_amount = d.pop("additionalTaxAmount", UNSET)

        additional_tax_percentage = d.pop("additionalTaxPercentage", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        note = d.pop("note", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CodatDataContractsDatasetsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CodatDataContractsDatasetsMetadata.from_dict(_metadata)

        _supplemental_data = d.pop("supplementalData", UNSET)
        supplemental_data: Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]
        if isinstance(_supplemental_data, Unset):
            supplemental_data = UNSET
        else:
            supplemental_data = CodatDataContractsDatasetsDataInterfacesSupplementalData.from_dict(_supplemental_data)

        codat_data_contracts_datasets_invoice = cls(
            issue_date=issue_date,
            total_tax_amount=total_tax_amount,
            total_amount=total_amount,
            amount_due=amount_due,
            status=status,
            id=id,
            invoice_number=invoice_number,
            customer_ref=customer_ref,
            sales_order_refs=sales_order_refs,
            due_date=due_date,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            paid_on_date=paid_on_date,
            currency=currency,
            currency_rate=currency_rate,
            line_items=line_items,
            payment_allocations=payment_allocations,
            withholding_tax=withholding_tax,
            total_discount=total_discount,
            sub_total=sub_total,
            additional_tax_amount=additional_tax_amount,
            additional_tax_percentage=additional_tax_percentage,
            discount_percentage=discount_percentage,
            note=note,
            metadata=metadata,
            supplemental_data=supplemental_data,
        )

        return codat_data_contracts_datasets_invoice
