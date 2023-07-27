import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_invoicing_status import CodatDataContractsDatasetsInvoicingStatus
from ..models.codat_data_contracts_datasets_sales_order_status import CodatDataContractsDatasetsSalesOrderStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_customer_ref import CodatDataContractsDatasetsCustomerRef
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
        CodatDataContractsDatasetsDataInterfacesSupplementalData,
    )
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
    from ..models.codat_data_contracts_datasets_sales_order_line_item import (
        CodatDataContractsDatasetsSalesOrderLineItem,
    )
    from ..models.codat_data_contracts_datasets_ship_to import CodatDataContractsDatasetsShipTo


T = TypeVar("T", bound="CodatDataContractsDatasetsSalesOrder")


@define
class CodatDataContractsDatasetsSalesOrder:
    """
    Attributes:
        id (Union[Unset, None, str]):
        sales_order_number (Union[Unset, None, str]):
        customer_purchase_order_number (Union[Unset, None, str]):
        issue_date (Union[Unset, datetime.datetime]):
        expected_delivery_date (Union[Unset, None, datetime.datetime]):
        note (Union[Unset, None, str]):
        ship_to (Union[Unset, CodatDataContractsDatasetsShipTo]):
        customer_ref (Union[Unset, CodatDataContractsDatasetsCustomerRef]):
        status (Union[Unset, CodatDataContractsDatasetsSalesOrderStatus]):
        invoicing_status (Union[Unset, CodatDataContractsDatasetsInvoicingStatus]):
        currency (Union[Unset, None, str]):
        currency_rate (Union[Unset, None, float]):
        line_items (Union[Unset, None, List['CodatDataContractsDatasetsSalesOrderLineItem']]):
        total_discount (Union[Unset, float]):
        sub_total (Union[Unset, float]):
        total_tax_amount (Union[Unset, float]):
        total_amount (Union[Unset, float]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        supplemental_data (Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
    """

    id: Union[Unset, None, str] = UNSET
    sales_order_number: Union[Unset, None, str] = UNSET
    customer_purchase_order_number: Union[Unset, None, str] = UNSET
    issue_date: Union[Unset, datetime.datetime] = UNSET
    expected_delivery_date: Union[Unset, None, datetime.datetime] = UNSET
    note: Union[Unset, None, str] = UNSET
    ship_to: Union[Unset, "CodatDataContractsDatasetsShipTo"] = UNSET
    customer_ref: Union[Unset, "CodatDataContractsDatasetsCustomerRef"] = UNSET
    status: Union[Unset, CodatDataContractsDatasetsSalesOrderStatus] = UNSET
    invoicing_status: Union[Unset, CodatDataContractsDatasetsInvoicingStatus] = UNSET
    currency: Union[Unset, None, str] = UNSET
    currency_rate: Union[Unset, None, float] = UNSET
    line_items: Union[Unset, None, List["CodatDataContractsDatasetsSalesOrderLineItem"]] = UNSET
    total_discount: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    total_tax_amount: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    supplemental_data: Union[Unset, "CodatDataContractsDatasetsDataInterfacesSupplementalData"] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        sales_order_number = self.sales_order_number
        customer_purchase_order_number = self.customer_purchase_order_number
        issue_date: Union[Unset, str] = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        expected_delivery_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.expected_delivery_date, Unset):
            expected_delivery_date = self.expected_delivery_date.isoformat() if self.expected_delivery_date else None

        note = self.note
        ship_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ship_to, Unset):
            ship_to = self.ship_to.to_dict()

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        invoicing_status: Union[Unset, str] = UNSET
        if not isinstance(self.invoicing_status, Unset):
            invoicing_status = self.invoicing_status.value

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

        total_discount = self.total_discount
        sub_total = self.sub_total
        total_tax_amount = self.total_tax_amount
        total_amount = self.total_amount
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        supplemental_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplemental_data, Unset):
            supplemental_data = self.supplemental_data.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if sales_order_number is not UNSET:
            field_dict["salesOrderNumber"] = sales_order_number
        if customer_purchase_order_number is not UNSET:
            field_dict["customerPurchaseOrderNumber"] = customer_purchase_order_number
        if issue_date is not UNSET:
            field_dict["issueDate"] = issue_date
        if expected_delivery_date is not UNSET:
            field_dict["expectedDeliveryDate"] = expected_delivery_date
        if note is not UNSET:
            field_dict["note"] = note
        if ship_to is not UNSET:
            field_dict["shipTo"] = ship_to
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if status is not UNSET:
            field_dict["status"] = status
        if invoicing_status is not UNSET:
            field_dict["invoicingStatus"] = invoicing_status
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items
        if total_discount is not UNSET:
            field_dict["totalDiscount"] = total_discount
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if total_tax_amount is not UNSET:
            field_dict["totalTaxAmount"] = total_tax_amount
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if supplemental_data is not UNSET:
            field_dict["supplementalData"] = supplemental_data
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_customer_ref import CodatDataContractsDatasetsCustomerRef
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
            CodatDataContractsDatasetsDataInterfacesSupplementalData,
        )
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
        from ..models.codat_data_contracts_datasets_sales_order_line_item import (
            CodatDataContractsDatasetsSalesOrderLineItem,
        )
        from ..models.codat_data_contracts_datasets_ship_to import CodatDataContractsDatasetsShipTo

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        sales_order_number = d.pop("salesOrderNumber", UNSET)

        customer_purchase_order_number = d.pop("customerPurchaseOrderNumber", UNSET)

        _issue_date = d.pop("issueDate", UNSET)
        issue_date: Union[Unset, datetime.datetime]
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = isoparse(_issue_date)

        _expected_delivery_date = d.pop("expectedDeliveryDate", UNSET)
        expected_delivery_date: Union[Unset, None, datetime.datetime]
        if _expected_delivery_date is None:
            expected_delivery_date = None
        elif isinstance(_expected_delivery_date, Unset):
            expected_delivery_date = UNSET
        else:
            expected_delivery_date = isoparse(_expected_delivery_date)

        note = d.pop("note", UNSET)

        _ship_to = d.pop("shipTo", UNSET)
        ship_to: Union[Unset, CodatDataContractsDatasetsShipTo]
        if isinstance(_ship_to, Unset):
            ship_to = UNSET
        else:
            ship_to = CodatDataContractsDatasetsShipTo.from_dict(_ship_to)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CodatDataContractsDatasetsCustomerRef]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CodatDataContractsDatasetsCustomerRef.from_dict(_customer_ref)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CodatDataContractsDatasetsSalesOrderStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodatDataContractsDatasetsSalesOrderStatus(_status)

        _invoicing_status = d.pop("invoicingStatus", UNSET)
        invoicing_status: Union[Unset, CodatDataContractsDatasetsInvoicingStatus]
        if isinstance(_invoicing_status, Unset):
            invoicing_status = UNSET
        else:
            invoicing_status = CodatDataContractsDatasetsInvoicingStatus(_invoicing_status)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        line_items = []
        _line_items = d.pop("lineItems", UNSET)
        for line_items_item_data in _line_items or []:
            line_items_item = CodatDataContractsDatasetsSalesOrderLineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        total_discount = d.pop("totalDiscount", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        total_tax_amount = d.pop("totalTaxAmount", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

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

        _supplemental_data = d.pop("supplementalData", UNSET)
        supplemental_data: Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]
        if isinstance(_supplemental_data, Unset):
            supplemental_data = UNSET
        else:
            supplemental_data = CodatDataContractsDatasetsDataInterfacesSupplementalData.from_dict(_supplemental_data)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CodatDataContractsDatasetsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CodatDataContractsDatasetsMetadata.from_dict(_metadata)

        codat_data_contracts_datasets_sales_order = cls(
            id=id,
            sales_order_number=sales_order_number,
            customer_purchase_order_number=customer_purchase_order_number,
            issue_date=issue_date,
            expected_delivery_date=expected_delivery_date,
            note=note,
            ship_to=ship_to,
            customer_ref=customer_ref,
            status=status,
            invoicing_status=invoicing_status,
            currency=currency,
            currency_rate=currency_rate,
            line_items=line_items,
            total_discount=total_discount,
            sub_total=sub_total,
            total_tax_amount=total_tax_amount,
            total_amount=total_amount,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            supplemental_data=supplemental_data,
            metadata=metadata,
        )

        return codat_data_contracts_datasets_sales_order
