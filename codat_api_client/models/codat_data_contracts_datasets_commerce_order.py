import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_customer_ref import (
        CodatDataContractsDatasetsCommerceCustomerRef,
    )
    from ..models.codat_data_contracts_datasets_commerce_location_ref import (
        CodatDataContractsDatasetsCommerceLocationRef,
    )
    from ..models.codat_data_contracts_datasets_commerce_order_line_item import (
        CodatDataContractsDatasetsCommerceOrderLineItem,
    )
    from ..models.codat_data_contracts_datasets_commerce_payment_ref import CodatDataContractsDatasetsCommercePaymentRef
    from ..models.codat_data_contracts_datasets_commerce_service_charge import (
        CodatDataContractsDatasetsCommerceServiceCharge,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceOrder")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCommerceOrder:
    """
    Attributes:
        id (Union[Unset, None, str]):
        order_number (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        currency (Union[Unset, None, str]):
        created_date (Union[Unset, datetime.datetime]):
        closed_date (Union[Unset, None, datetime.datetime]):
        total_amount (Union[Unset, float]):
        total_refund (Union[Unset, float]):
        total_tax_amount (Union[Unset, float]):
        total_discount (Union[Unset, float]):
        total_gratuity (Union[Unset, float]):
        order_line_items (Union[Unset, None, List['CodatDataContractsDatasetsCommerceOrderLineItem']]):
        payments (Union[Unset, None, List['CodatDataContractsDatasetsCommercePaymentRef']]):
        service_charges (Union[Unset, None, List['CodatDataContractsDatasetsCommerceServiceCharge']]):
        location_ref (Union[Unset, CodatDataContractsDatasetsCommerceLocationRef]):
        customer_ref (Union[Unset, CodatDataContractsDatasetsCommerceCustomerRef]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    id: Union[Unset, None, str] = UNSET
    order_number: Union[Unset, None, str] = UNSET
    country: Union[Unset, None, str] = UNSET
    currency: Union[Unset, None, str] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    closed_date: Union[Unset, None, datetime.datetime] = UNSET
    total_amount: Union[Unset, float] = UNSET
    total_refund: Union[Unset, float] = UNSET
    total_tax_amount: Union[Unset, float] = UNSET
    total_discount: Union[Unset, float] = UNSET
    total_gratuity: Union[Unset, float] = UNSET
    order_line_items: Union[Unset, None, List["CodatDataContractsDatasetsCommerceOrderLineItem"]] = UNSET
    payments: Union[Unset, None, List["CodatDataContractsDatasetsCommercePaymentRef"]] = UNSET
    service_charges: Union[Unset, None, List["CodatDataContractsDatasetsCommerceServiceCharge"]] = UNSET
    location_ref: Union[Unset, "CodatDataContractsDatasetsCommerceLocationRef"] = UNSET
    customer_ref: Union[Unset, "CodatDataContractsDatasetsCommerceCustomerRef"] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        order_number = self.order_number
        country = self.country
        currency = self.currency
        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        closed_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.closed_date, Unset):
            closed_date = self.closed_date.isoformat() if self.closed_date else None

        total_amount = self.total_amount
        total_refund = self.total_refund
        total_tax_amount = self.total_tax_amount
        total_discount = self.total_discount
        total_gratuity = self.total_gratuity
        order_line_items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_line_items, Unset):
            if self.order_line_items is None:
                order_line_items = None
            else:
                order_line_items = []
                for order_line_items_item_data in self.order_line_items:
                    order_line_items_item = order_line_items_item_data.to_dict()

                    order_line_items.append(order_line_items_item)

        payments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payments, Unset):
            if self.payments is None:
                payments = None
            else:
                payments = []
                for payments_item_data in self.payments:
                    payments_item = payments_item_data.to_dict()

                    payments.append(payments_item)

        service_charges: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.service_charges, Unset):
            if self.service_charges is None:
                service_charges = None
            else:
                service_charges = []
                for service_charges_item_data in self.service_charges:
                    service_charges_item = service_charges_item_data.to_dict()

                    service_charges.append(service_charges_item)

        location_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location_ref, Unset):
            location_ref = self.location_ref.to_dict()

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if order_number is not UNSET:
            field_dict["orderNumber"] = order_number
        if country is not UNSET:
            field_dict["country"] = country
        if currency is not UNSET:
            field_dict["currency"] = currency
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if closed_date is not UNSET:
            field_dict["closedDate"] = closed_date
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if total_refund is not UNSET:
            field_dict["totalRefund"] = total_refund
        if total_tax_amount is not UNSET:
            field_dict["totalTaxAmount"] = total_tax_amount
        if total_discount is not UNSET:
            field_dict["totalDiscount"] = total_discount
        if total_gratuity is not UNSET:
            field_dict["totalGratuity"] = total_gratuity
        if order_line_items is not UNSET:
            field_dict["orderLineItems"] = order_line_items
        if payments is not UNSET:
            field_dict["payments"] = payments
        if service_charges is not UNSET:
            field_dict["serviceCharges"] = service_charges
        if location_ref is not UNSET:
            field_dict["locationRef"] = location_ref
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_commerce_customer_ref import (
            CodatDataContractsDatasetsCommerceCustomerRef,
        )
        from ..models.codat_data_contracts_datasets_commerce_location_ref import (
            CodatDataContractsDatasetsCommerceLocationRef,
        )
        from ..models.codat_data_contracts_datasets_commerce_order_line_item import (
            CodatDataContractsDatasetsCommerceOrderLineItem,
        )
        from ..models.codat_data_contracts_datasets_commerce_payment_ref import (
            CodatDataContractsDatasetsCommercePaymentRef,
        )
        from ..models.codat_data_contracts_datasets_commerce_service_charge import (
            CodatDataContractsDatasetsCommerceServiceCharge,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        order_number = d.pop("orderNumber", UNSET)

        country = d.pop("country", UNSET)

        currency = d.pop("currency", UNSET)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        _closed_date = d.pop("closedDate", UNSET)
        closed_date: Union[Unset, None, datetime.datetime]
        if _closed_date is None:
            closed_date = None
        elif isinstance(_closed_date, Unset):
            closed_date = UNSET
        else:
            closed_date = isoparse(_closed_date)

        total_amount = d.pop("totalAmount", UNSET)

        total_refund = d.pop("totalRefund", UNSET)

        total_tax_amount = d.pop("totalTaxAmount", UNSET)

        total_discount = d.pop("totalDiscount", UNSET)

        total_gratuity = d.pop("totalGratuity", UNSET)

        order_line_items = []
        _order_line_items = d.pop("orderLineItems", UNSET)
        for order_line_items_item_data in _order_line_items or []:
            order_line_items_item = CodatDataContractsDatasetsCommerceOrderLineItem.from_dict(
                order_line_items_item_data
            )

            order_line_items.append(order_line_items_item)

        payments = []
        _payments = d.pop("payments", UNSET)
        for payments_item_data in _payments or []:
            payments_item = CodatDataContractsDatasetsCommercePaymentRef.from_dict(payments_item_data)

            payments.append(payments_item)

        service_charges = []
        _service_charges = d.pop("serviceCharges", UNSET)
        for service_charges_item_data in _service_charges or []:
            service_charges_item = CodatDataContractsDatasetsCommerceServiceCharge.from_dict(service_charges_item_data)

            service_charges.append(service_charges_item)

        _location_ref = d.pop("locationRef", UNSET)
        location_ref: Union[Unset, CodatDataContractsDatasetsCommerceLocationRef]
        if isinstance(_location_ref, Unset):
            location_ref = UNSET
        else:
            location_ref = CodatDataContractsDatasetsCommerceLocationRef.from_dict(_location_ref)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CodatDataContractsDatasetsCommerceCustomerRef]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CodatDataContractsDatasetsCommerceCustomerRef.from_dict(_customer_ref)

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

        codat_data_contracts_datasets_commerce_order = cls(
            id=id,
            order_number=order_number,
            country=country,
            currency=currency,
            created_date=created_date,
            closed_date=closed_date,
            total_amount=total_amount,
            total_refund=total_refund,
            total_tax_amount=total_tax_amount,
            total_discount=total_discount,
            total_gratuity=total_gratuity,
            order_line_items=order_line_items,
            payments=payments,
            service_charges=service_charges,
            location_ref=location_ref,
            customer_ref=customer_ref,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_commerce_order
