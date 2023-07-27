from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceProductVariantPrice")


@define
class CodatDataContractsDatasetsCommerceProductVariantPrice:
    """
    Attributes:
        currency (Union[Unset, None, str]):
        unit_price (Union[Unset, float]):
    """

    currency: Union[Unset, None, str] = UNSET
    unit_price: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency
        unit_price = self.unit_price

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        codat_data_contracts_datasets_commerce_product_variant_price = cls(
            currency=currency,
            unit_price=unit_price,
        )

        return codat_data_contracts_datasets_commerce_product_variant_price
