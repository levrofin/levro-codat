from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..models.codat_data_contracts_datasets_commerce_service_charge_type import (
    CodatDataContractsDatasetsCommerceServiceChargeType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_tax_component_allocation import (
        CodatDataContractsDatasetsCommerceTaxComponentAllocation,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceServiceCharge")


@define
class CodatDataContractsDatasetsCommerceServiceCharge:
    """
    Attributes:
        description (Union[Unset, None, str]):
        total_amount (Union[Unset, float]):
        tax_percentage (Union[Unset, float]):
        tax_amount (Union[Unset, float]):
        taxes (Union[Unset, None, List['CodatDataContractsDatasetsCommerceTaxComponentAllocation']]):
        quantity (Union[Unset, int]):
        type (Union[Unset, CodatDataContractsDatasetsCommerceServiceChargeType]):
    """

    description: Union[Unset, None, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    tax_percentage: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    taxes: Union[Unset, None, List["CodatDataContractsDatasetsCommerceTaxComponentAllocation"]] = UNSET
    quantity: Union[Unset, int] = UNSET
    type: Union[Unset, CodatDataContractsDatasetsCommerceServiceChargeType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        total_amount = self.total_amount
        tax_percentage = self.tax_percentage
        tax_amount = self.tax_amount
        taxes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.taxes, Unset):
            if self.taxes is None:
                taxes = None
            else:
                taxes = []
                for taxes_item_data in self.taxes:
                    taxes_item = taxes_item_data.to_dict()

                    taxes.append(taxes_item)

        quantity = self.quantity
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if tax_percentage is not UNSET:
            field_dict["taxPercentage"] = tax_percentage
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_commerce_tax_component_allocation import (
            CodatDataContractsDatasetsCommerceTaxComponentAllocation,
        )

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        tax_percentage = d.pop("taxPercentage", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = CodatDataContractsDatasetsCommerceTaxComponentAllocation.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        quantity = d.pop("quantity", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CodatDataContractsDatasetsCommerceServiceChargeType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodatDataContractsDatasetsCommerceServiceChargeType(_type)

        codat_data_contracts_datasets_commerce_service_charge = cls(
            description=description,
            total_amount=total_amount,
            tax_percentage=tax_percentage,
            tax_amount=tax_amount,
            taxes=taxes,
            quantity=quantity,
            type=type,
        )

        return codat_data_contracts_datasets_commerce_service_charge
