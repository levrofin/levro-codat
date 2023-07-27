import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_bill_status import CodatDataContractsDatasetsBillStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_bill_line_item import CodatDataContractsDatasetsBillLineItem
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
        CodatDataContractsDatasetsDataInterfacesSupplementalData,
    )
    from ..models.codat_data_contracts_datasets_detailed_payment_allocation import (
        CodatDataContractsDatasetsDetailedPaymentAllocation,
    )
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
    from ..models.codat_data_contracts_datasets_purchase_order_ref import CodatDataContractsDatasetsPurchaseOrderRef
    from ..models.codat_data_contracts_datasets_supplier_ref import CodatDataContractsDatasetsSupplierRef
    from ..models.codat_data_contracts_datasets_withholding_tax import CodatDataContractsDatasetsWithholdingTax


T = TypeVar("T", bound="CodatDataContractsDatasetsBill")


@define
class CodatDataContractsDatasetsBill:
    """
    Attributes:
        issue_date (datetime.datetime):
        status (CodatDataContractsDatasetsBillStatus):
        sub_total (float):
        tax_amount (float):
        total_amount (float):
        id (Union[Unset, None, str]):
        reference (Union[Unset, None, str]):
        supplier_ref (Union[Unset, CodatDataContractsDatasetsSupplierRef]):
        purchase_order_refs (Union[Unset, None, List['CodatDataContractsDatasetsPurchaseOrderRef']]):
        due_date (Union[Unset, None, datetime.datetime]):
        currency (Union[Unset, None, str]):
        currency_rate (Union[Unset, None, float]):
        line_items (Union[Unset, None, List['CodatDataContractsDatasetsBillLineItem']]):
        withholding_tax (Union[Unset, None, List['CodatDataContractsDatasetsWithholdingTax']]):
        amount_due (Union[Unset, None, float]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        note (Union[Unset, None, str]):
        payment_allocations (Union[Unset, None, List['CodatDataContractsDatasetsDetailedPaymentAllocation']]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
        supplemental_data (Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]):
    """

    issue_date: datetime.datetime
    status: CodatDataContractsDatasetsBillStatus
    sub_total: float
    tax_amount: float
    total_amount: float
    id: Union[Unset, None, str] = UNSET
    reference: Union[Unset, None, str] = UNSET
    supplier_ref: Union[Unset, "CodatDataContractsDatasetsSupplierRef"] = UNSET
    purchase_order_refs: Union[Unset, None, List["CodatDataContractsDatasetsPurchaseOrderRef"]] = UNSET
    due_date: Union[Unset, None, datetime.datetime] = UNSET
    currency: Union[Unset, None, str] = UNSET
    currency_rate: Union[Unset, None, float] = UNSET
    line_items: Union[Unset, None, List["CodatDataContractsDatasetsBillLineItem"]] = UNSET
    withholding_tax: Union[Unset, None, List["CodatDataContractsDatasetsWithholdingTax"]] = UNSET
    amount_due: Union[Unset, None, float] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    note: Union[Unset, None, str] = UNSET
    payment_allocations: Union[Unset, None, List["CodatDataContractsDatasetsDetailedPaymentAllocation"]] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET
    supplemental_data: Union[Unset, "CodatDataContractsDatasetsDataInterfacesSupplementalData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        issue_date = self.issue_date.isoformat()

        status = self.status.value

        sub_total = self.sub_total
        tax_amount = self.tax_amount
        total_amount = self.total_amount
        id = self.id
        reference = self.reference
        supplier_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplier_ref, Unset):
            supplier_ref = self.supplier_ref.to_dict()

        purchase_order_refs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.purchase_order_refs, Unset):
            if self.purchase_order_refs is None:
                purchase_order_refs = None
            else:
                purchase_order_refs = []
                for purchase_order_refs_item_data in self.purchase_order_refs:
                    purchase_order_refs_item = purchase_order_refs_item_data.to_dict()

                    purchase_order_refs.append(purchase_order_refs_item)

        due_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat() if self.due_date else None

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

        withholding_tax: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.withholding_tax, Unset):
            if self.withholding_tax is None:
                withholding_tax = None
            else:
                withholding_tax = []
                for withholding_tax_item_data in self.withholding_tax:
                    withholding_tax_item = withholding_tax_item_data.to_dict()

                    withholding_tax.append(withholding_tax_item)

        amount_due = self.amount_due
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        note = self.note
        payment_allocations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payment_allocations, Unset):
            if self.payment_allocations is None:
                payment_allocations = None
            else:
                payment_allocations = []
                for payment_allocations_item_data in self.payment_allocations:
                    payment_allocations_item = payment_allocations_item_data.to_dict()

                    payment_allocations.append(payment_allocations_item)

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
                "status": status,
                "subTotal": sub_total,
                "taxAmount": tax_amount,
                "totalAmount": total_amount,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if supplier_ref is not UNSET:
            field_dict["supplierRef"] = supplier_ref
        if purchase_order_refs is not UNSET:
            field_dict["purchaseOrderRefs"] = purchase_order_refs
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items
        if withholding_tax is not UNSET:
            field_dict["withholdingTax"] = withholding_tax
        if amount_due is not UNSET:
            field_dict["amountDue"] = amount_due
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if note is not UNSET:
            field_dict["note"] = note
        if payment_allocations is not UNSET:
            field_dict["paymentAllocations"] = payment_allocations
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if supplemental_data is not UNSET:
            field_dict["supplementalData"] = supplemental_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_bill_line_item import CodatDataContractsDatasetsBillLineItem
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
            CodatDataContractsDatasetsDataInterfacesSupplementalData,
        )
        from ..models.codat_data_contracts_datasets_detailed_payment_allocation import (
            CodatDataContractsDatasetsDetailedPaymentAllocation,
        )
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
        from ..models.codat_data_contracts_datasets_purchase_order_ref import CodatDataContractsDatasetsPurchaseOrderRef
        from ..models.codat_data_contracts_datasets_supplier_ref import CodatDataContractsDatasetsSupplierRef
        from ..models.codat_data_contracts_datasets_withholding_tax import CodatDataContractsDatasetsWithholdingTax

        d = src_dict.copy()
        issue_date = isoparse(d.pop("issueDate"))

        status = CodatDataContractsDatasetsBillStatus(d.pop("status"))

        sub_total = d.pop("subTotal")

        tax_amount = d.pop("taxAmount")

        total_amount = d.pop("totalAmount")

        id = d.pop("id", UNSET)

        reference = d.pop("reference", UNSET)

        _supplier_ref = d.pop("supplierRef", UNSET)
        supplier_ref: Union[Unset, CodatDataContractsDatasetsSupplierRef]
        if isinstance(_supplier_ref, Unset):
            supplier_ref = UNSET
        else:
            supplier_ref = CodatDataContractsDatasetsSupplierRef.from_dict(_supplier_ref)

        purchase_order_refs = []
        _purchase_order_refs = d.pop("purchaseOrderRefs", UNSET)
        for purchase_order_refs_item_data in _purchase_order_refs or []:
            purchase_order_refs_item = CodatDataContractsDatasetsPurchaseOrderRef.from_dict(
                purchase_order_refs_item_data
            )

            purchase_order_refs.append(purchase_order_refs_item)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, None, datetime.datetime]
        if _due_date is None:
            due_date = None
        elif isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        line_items = []
        _line_items = d.pop("lineItems", UNSET)
        for line_items_item_data in _line_items or []:
            line_items_item = CodatDataContractsDatasetsBillLineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        withholding_tax = []
        _withholding_tax = d.pop("withholdingTax", UNSET)
        for withholding_tax_item_data in _withholding_tax or []:
            withholding_tax_item = CodatDataContractsDatasetsWithholdingTax.from_dict(withholding_tax_item_data)

            withholding_tax.append(withholding_tax_item)

        amount_due = d.pop("amountDue", UNSET)

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

        payment_allocations = []
        _payment_allocations = d.pop("paymentAllocations", UNSET)
        for payment_allocations_item_data in _payment_allocations or []:
            payment_allocations_item = CodatDataContractsDatasetsDetailedPaymentAllocation.from_dict(
                payment_allocations_item_data
            )

            payment_allocations.append(payment_allocations_item)

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

        codat_data_contracts_datasets_bill = cls(
            issue_date=issue_date,
            status=status,
            sub_total=sub_total,
            tax_amount=tax_amount,
            total_amount=total_amount,
            id=id,
            reference=reference,
            supplier_ref=supplier_ref,
            purchase_order_refs=purchase_order_refs,
            due_date=due_date,
            currency=currency,
            currency_rate=currency_rate,
            line_items=line_items,
            withholding_tax=withholding_tax,
            amount_due=amount_due,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            note=note,
            payment_allocations=payment_allocations,
            metadata=metadata,
            supplemental_data=supplemental_data,
        )

        return codat_data_contracts_datasets_bill
