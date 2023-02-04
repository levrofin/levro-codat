import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_credit_note_status import CodatDataContractsDatasetsCreditNoteStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_credit_note_line_item import (
        CodatDataContractsDatasetsCreditNoteLineItem,
    )
    from ..models.codat_data_contracts_datasets_customer_ref import CodatDataContractsDatasetsCustomerRef
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
        CodatDataContractsDatasetsDataInterfacesSupplementalData,
    )
    from ..models.codat_data_contracts_datasets_detailed_payment_allocation import (
        CodatDataContractsDatasetsDetailedPaymentAllocation,
    )
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
    from ..models.codat_data_contracts_datasets_withholding_tax import CodatDataContractsDatasetsWithholdingTax


T = TypeVar("T", bound="CodatDataContractsDatasetsCreditNote")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCreditNote:
    """
    Attributes:
        total_amount (float):
        total_discount (float):
        sub_total (float):
        total_tax_amount (float):
        discount_percentage (float):
        remaining_credit (float):
        status (CodatDataContractsDatasetsCreditNoteStatus):
        id (Union[Unset, None, str]):
        credit_note_number (Union[Unset, None, str]):
        customer_ref (Union[Unset, CodatDataContractsDatasetsCustomerRef]):
        withholding_tax (Union[Unset, None, List['CodatDataContractsDatasetsWithholdingTax']]):
        additional_tax_amount (Union[Unset, float]):
        additional_tax_percentage (Union[Unset, float]):
        issue_date (Union[Unset, datetime.datetime]):
        allocated_on_date (Union[Unset, None, datetime.datetime]):
        currency (Union[Unset, None, str]):
        currency_rate (Union[Unset, None, float]):
        line_items (Union[Unset, None, List['CodatDataContractsDatasetsCreditNoteLineItem']]):
        payment_allocations (Union[Unset, None, List['CodatDataContractsDatasetsDetailedPaymentAllocation']]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        note (Union[Unset, None, str]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
        supplemental_data (Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]):
    """

    total_amount: float
    total_discount: float
    sub_total: float
    total_tax_amount: float
    discount_percentage: float
    remaining_credit: float
    status: CodatDataContractsDatasetsCreditNoteStatus
    id: Union[Unset, None, str] = UNSET
    credit_note_number: Union[Unset, None, str] = UNSET
    customer_ref: Union[Unset, "CodatDataContractsDatasetsCustomerRef"] = UNSET
    withholding_tax: Union[Unset, None, List["CodatDataContractsDatasetsWithholdingTax"]] = UNSET
    additional_tax_amount: Union[Unset, float] = UNSET
    additional_tax_percentage: Union[Unset, float] = UNSET
    issue_date: Union[Unset, datetime.datetime] = UNSET
    allocated_on_date: Union[Unset, None, datetime.datetime] = UNSET
    currency: Union[Unset, None, str] = UNSET
    currency_rate: Union[Unset, None, float] = UNSET
    line_items: Union[Unset, None, List["CodatDataContractsDatasetsCreditNoteLineItem"]] = UNSET
    payment_allocations: Union[Unset, None, List["CodatDataContractsDatasetsDetailedPaymentAllocation"]] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    note: Union[Unset, None, str] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET
    supplemental_data: Union[Unset, "CodatDataContractsDatasetsDataInterfacesSupplementalData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        total_amount = self.total_amount
        total_discount = self.total_discount
        sub_total = self.sub_total
        total_tax_amount = self.total_tax_amount
        discount_percentage = self.discount_percentage
        remaining_credit = self.remaining_credit
        status = self.status.value

        id = self.id
        credit_note_number = self.credit_note_number
        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        withholding_tax: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.withholding_tax, Unset):
            if self.withholding_tax is None:
                withholding_tax = None
            else:
                withholding_tax = []
                for withholding_tax_item_data in self.withholding_tax:
                    withholding_tax_item = withholding_tax_item_data.to_dict()

                    withholding_tax.append(withholding_tax_item)

        additional_tax_amount = self.additional_tax_amount
        additional_tax_percentage = self.additional_tax_percentage
        issue_date: Union[Unset, str] = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        allocated_on_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.allocated_on_date, Unset):
            allocated_on_date = self.allocated_on_date.isoformat() if self.allocated_on_date else None

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

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

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
                "totalAmount": total_amount,
                "totalDiscount": total_discount,
                "subTotal": sub_total,
                "totalTaxAmount": total_tax_amount,
                "discountPercentage": discount_percentage,
                "remainingCredit": remaining_credit,
                "status": status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if credit_note_number is not UNSET:
            field_dict["creditNoteNumber"] = credit_note_number
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if withholding_tax is not UNSET:
            field_dict["withholdingTax"] = withholding_tax
        if additional_tax_amount is not UNSET:
            field_dict["additionalTaxAmount"] = additional_tax_amount
        if additional_tax_percentage is not UNSET:
            field_dict["additionalTaxPercentage"] = additional_tax_percentage
        if issue_date is not UNSET:
            field_dict["issueDate"] = issue_date
        if allocated_on_date is not UNSET:
            field_dict["allocatedOnDate"] = allocated_on_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items
        if payment_allocations is not UNSET:
            field_dict["paymentAllocations"] = payment_allocations
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if note is not UNSET:
            field_dict["note"] = note
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if supplemental_data is not UNSET:
            field_dict["supplementalData"] = supplemental_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_credit_note_line_item import (
            CodatDataContractsDatasetsCreditNoteLineItem,
        )
        from ..models.codat_data_contracts_datasets_customer_ref import CodatDataContractsDatasetsCustomerRef
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
            CodatDataContractsDatasetsDataInterfacesSupplementalData,
        )
        from ..models.codat_data_contracts_datasets_detailed_payment_allocation import (
            CodatDataContractsDatasetsDetailedPaymentAllocation,
        )
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
        from ..models.codat_data_contracts_datasets_withholding_tax import CodatDataContractsDatasetsWithholdingTax

        d = src_dict.copy()
        total_amount = d.pop("totalAmount")

        total_discount = d.pop("totalDiscount")

        sub_total = d.pop("subTotal")

        total_tax_amount = d.pop("totalTaxAmount")

        discount_percentage = d.pop("discountPercentage")

        remaining_credit = d.pop("remainingCredit")

        status = CodatDataContractsDatasetsCreditNoteStatus(d.pop("status"))

        id = d.pop("id", UNSET)

        credit_note_number = d.pop("creditNoteNumber", UNSET)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CodatDataContractsDatasetsCustomerRef]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CodatDataContractsDatasetsCustomerRef.from_dict(_customer_ref)

        withholding_tax = []
        _withholding_tax = d.pop("withholdingTax", UNSET)
        for withholding_tax_item_data in _withholding_tax or []:
            withholding_tax_item = CodatDataContractsDatasetsWithholdingTax.from_dict(withholding_tax_item_data)

            withholding_tax.append(withholding_tax_item)

        additional_tax_amount = d.pop("additionalTaxAmount", UNSET)

        additional_tax_percentage = d.pop("additionalTaxPercentage", UNSET)

        _issue_date = d.pop("issueDate", UNSET)
        issue_date: Union[Unset, datetime.datetime]
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = isoparse(_issue_date)

        _allocated_on_date = d.pop("allocatedOnDate", UNSET)
        allocated_on_date: Union[Unset, None, datetime.datetime]
        if _allocated_on_date is None:
            allocated_on_date = None
        elif isinstance(_allocated_on_date, Unset):
            allocated_on_date = UNSET
        else:
            allocated_on_date = isoparse(_allocated_on_date)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        line_items = []
        _line_items = d.pop("lineItems", UNSET)
        for line_items_item_data in _line_items or []:
            line_items_item = CodatDataContractsDatasetsCreditNoteLineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        payment_allocations = []
        _payment_allocations = d.pop("paymentAllocations", UNSET)
        for payment_allocations_item_data in _payment_allocations or []:
            payment_allocations_item = CodatDataContractsDatasetsDetailedPaymentAllocation.from_dict(
                payment_allocations_item_data
            )

            payment_allocations.append(payment_allocations_item)

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

        codat_data_contracts_datasets_credit_note = cls(
            total_amount=total_amount,
            total_discount=total_discount,
            sub_total=sub_total,
            total_tax_amount=total_tax_amount,
            discount_percentage=discount_percentage,
            remaining_credit=remaining_credit,
            status=status,
            id=id,
            credit_note_number=credit_note_number,
            customer_ref=customer_ref,
            withholding_tax=withholding_tax,
            additional_tax_amount=additional_tax_amount,
            additional_tax_percentage=additional_tax_percentage,
            issue_date=issue_date,
            allocated_on_date=allocated_on_date,
            currency=currency,
            currency_rate=currency_rate,
            line_items=line_items,
            payment_allocations=payment_allocations,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            note=note,
            metadata=metadata,
            supplemental_data=supplemental_data,
        )

        return codat_data_contracts_datasets_credit_note
