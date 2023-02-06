import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_inventory import CodatDataContractsDatasetsCommerceInventory
    from ..models.codat_data_contracts_datasets_commerce_product_variant_price import (
        CodatDataContractsDatasetsCommerceProductVariantPrice,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceProductVariant")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCommerceProductVariant:
    """
    Attributes:
        id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        quantity (Union[Unset, float]):
        is_tax_enabled (Union[Unset, bool]):
        sku (Union[Unset, None, str]):
        barcode (Union[Unset, None, str]):
        unit_of_measure (Union[Unset, None, str]):
        vat_percentage (Union[Unset, float]):
        prices (Union[Unset, None, List['CodatDataContractsDatasetsCommerceProductVariantPrice']]):
        inventory (Union[Unset, CodatDataContractsDatasetsCommerceInventory]):
        shipping_required (Union[Unset, bool]):
        created_date (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    is_tax_enabled: Union[Unset, bool] = UNSET
    sku: Union[Unset, None, str] = UNSET
    barcode: Union[Unset, None, str] = UNSET
    unit_of_measure: Union[Unset, None, str] = UNSET
    vat_percentage: Union[Unset, float] = UNSET
    prices: Union[Unset, None, List["CodatDataContractsDatasetsCommerceProductVariantPrice"]] = UNSET
    inventory: Union[Unset, "CodatDataContractsDatasetsCommerceInventory"] = UNSET
    shipping_required: Union[Unset, bool] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        quantity = self.quantity
        is_tax_enabled = self.is_tax_enabled
        sku = self.sku
        barcode = self.barcode
        unit_of_measure = self.unit_of_measure
        vat_percentage = self.vat_percentage
        prices: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.prices, Unset):
            if self.prices is None:
                prices = None
            else:
                prices = []
                for prices_item_data in self.prices:
                    prices_item = prices_item_data.to_dict()

                    prices.append(prices_item)

        inventory: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = self.inventory.to_dict()

        shipping_required = self.shipping_required
        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if is_tax_enabled is not UNSET:
            field_dict["isTaxEnabled"] = is_tax_enabled
        if sku is not UNSET:
            field_dict["sku"] = sku
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if unit_of_measure is not UNSET:
            field_dict["unitOfMeasure"] = unit_of_measure
        if vat_percentage is not UNSET:
            field_dict["vatPercentage"] = vat_percentage
        if prices is not UNSET:
            field_dict["prices"] = prices
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if shipping_required is not UNSET:
            field_dict["shippingRequired"] = shipping_required
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_commerce_inventory import (
            CodatDataContractsDatasetsCommerceInventory,
        )
        from ..models.codat_data_contracts_datasets_commerce_product_variant_price import (
            CodatDataContractsDatasetsCommerceProductVariantPrice,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        quantity = d.pop("quantity", UNSET)

        is_tax_enabled = d.pop("isTaxEnabled", UNSET)

        sku = d.pop("sku", UNSET)

        barcode = d.pop("barcode", UNSET)

        unit_of_measure = d.pop("unitOfMeasure", UNSET)

        vat_percentage = d.pop("vatPercentage", UNSET)

        prices = []
        _prices = d.pop("prices", UNSET)
        for prices_item_data in _prices or []:
            prices_item = CodatDataContractsDatasetsCommerceProductVariantPrice.from_dict(prices_item_data)

            prices.append(prices_item)

        _inventory = d.pop("inventory", UNSET)
        inventory: Union[Unset, CodatDataContractsDatasetsCommerceInventory]
        if isinstance(_inventory, Unset):
            inventory = UNSET
        else:
            inventory = CodatDataContractsDatasetsCommerceInventory.from_dict(_inventory)

        shipping_required = d.pop("shippingRequired", UNSET)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        codat_data_contracts_datasets_commerce_product_variant = cls(
            id=id,
            name=name,
            quantity=quantity,
            is_tax_enabled=is_tax_enabled,
            sku=sku,
            barcode=barcode,
            unit_of_measure=unit_of_measure,
            vat_percentage=vat_percentage,
            prices=prices,
            inventory=inventory,
            shipping_required=shipping_required,
            created_date=created_date,
        )

        return codat_data_contracts_datasets_commerce_product_variant
