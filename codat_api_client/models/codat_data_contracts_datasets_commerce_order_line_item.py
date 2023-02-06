from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_discount_allocation import (
        CodatDataContractsDatasetsCommerceDiscountAllocation,
    )
    from ..models.codat_data_contracts_datasets_commerce_product_ref import CodatDataContractsDatasetsCommerceProductRef
    from ..models.codat_data_contracts_datasets_commerce_tax_component_allocation import (
        CodatDataContractsDatasetsCommerceTaxComponentAllocation,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceOrderLineItem")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCommerceOrderLineItem:
    """
    Attributes:
        id (Union[Unset, None, str]):
        quantity (Union[Unset, float]):
        tax_percentage (Union[Unset, float]):
        total_amount (Union[Unset, float]):
        total_tax_amount (Union[Unset, float]):
        unit_price (Union[Unset, float]):
        taxes (Union[Unset, None, List['CodatDataContractsDatasetsCommerceTaxComponentAllocation']]):
        product_ref (Union[Unset, CodatDataContractsDatasetsCommerceProductRef]):
        product_variant_ref (Union[Unset, CodatDataContractsDatasetsCommerceProductRef]):
        discount_allocations (Union[Unset, None, List['CodatDataContractsDatasetsCommerceDiscountAllocation']]):
    """

    id: Union[Unset, None, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    tax_percentage: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    total_tax_amount: Union[Unset, float] = UNSET
    unit_price: Union[Unset, float] = UNSET
    taxes: Union[Unset, None, List["CodatDataContractsDatasetsCommerceTaxComponentAllocation"]] = UNSET
    product_ref: Union[Unset, "CodatDataContractsDatasetsCommerceProductRef"] = UNSET
    product_variant_ref: Union[Unset, "CodatDataContractsDatasetsCommerceProductRef"] = UNSET
    discount_allocations: Union[Unset, None, List["CodatDataContractsDatasetsCommerceDiscountAllocation"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        quantity = self.quantity
        tax_percentage = self.tax_percentage
        total_amount = self.total_amount
        total_tax_amount = self.total_tax_amount
        unit_price = self.unit_price
        taxes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.taxes, Unset):
            if self.taxes is None:
                taxes = None
            else:
                taxes = []
                for taxes_item_data in self.taxes:
                    taxes_item = taxes_item_data.to_dict()

                    taxes.append(taxes_item)

        product_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product_ref, Unset):
            product_ref = self.product_ref.to_dict()

        product_variant_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product_variant_ref, Unset):
            product_variant_ref = self.product_variant_ref.to_dict()

        discount_allocations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.discount_allocations, Unset):
            if self.discount_allocations is None:
                discount_allocations = None
            else:
                discount_allocations = []
                for discount_allocations_item_data in self.discount_allocations:
                    discount_allocations_item = discount_allocations_item_data.to_dict()

                    discount_allocations.append(discount_allocations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if tax_percentage is not UNSET:
            field_dict["taxPercentage"] = tax_percentage
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if total_tax_amount is not UNSET:
            field_dict["totalTaxAmount"] = total_tax_amount
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if product_ref is not UNSET:
            field_dict["productRef"] = product_ref
        if product_variant_ref is not UNSET:
            field_dict["productVariantRef"] = product_variant_ref
        if discount_allocations is not UNSET:
            field_dict["discountAllocations"] = discount_allocations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_commerce_discount_allocation import (
            CodatDataContractsDatasetsCommerceDiscountAllocation,
        )
        from ..models.codat_data_contracts_datasets_commerce_product_ref import (
            CodatDataContractsDatasetsCommerceProductRef,
        )
        from ..models.codat_data_contracts_datasets_commerce_tax_component_allocation import (
            CodatDataContractsDatasetsCommerceTaxComponentAllocation,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        quantity = d.pop("quantity", UNSET)

        tax_percentage = d.pop("taxPercentage", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        total_tax_amount = d.pop("totalTaxAmount", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = CodatDataContractsDatasetsCommerceTaxComponentAllocation.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        _product_ref = d.pop("productRef", UNSET)
        product_ref: Union[Unset, CodatDataContractsDatasetsCommerceProductRef]
        if isinstance(_product_ref, Unset):
            product_ref = UNSET
        else:
            product_ref = CodatDataContractsDatasetsCommerceProductRef.from_dict(_product_ref)

        _product_variant_ref = d.pop("productVariantRef", UNSET)
        product_variant_ref: Union[Unset, CodatDataContractsDatasetsCommerceProductRef]
        if isinstance(_product_variant_ref, Unset):
            product_variant_ref = UNSET
        else:
            product_variant_ref = CodatDataContractsDatasetsCommerceProductRef.from_dict(_product_variant_ref)

        discount_allocations = []
        _discount_allocations = d.pop("discountAllocations", UNSET)
        for discount_allocations_item_data in _discount_allocations or []:
            discount_allocations_item = CodatDataContractsDatasetsCommerceDiscountAllocation.from_dict(
                discount_allocations_item_data
            )

            discount_allocations.append(discount_allocations_item)

        codat_data_contracts_datasets_commerce_order_line_item = cls(
            id=id,
            quantity=quantity,
            tax_percentage=tax_percentage,
            total_amount=total_amount,
            total_tax_amount=total_tax_amount,
            unit_price=unit_price,
            taxes=taxes,
            product_ref=product_ref,
            product_variant_ref=product_variant_ref,
            discount_allocations=discount_allocations,
        )

        return codat_data_contracts_datasets_commerce_order_line_item
