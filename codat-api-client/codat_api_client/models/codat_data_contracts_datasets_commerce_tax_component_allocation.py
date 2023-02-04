from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_tax_component_ref import (
        CodatDataContractsDatasetsCommerceTaxComponentRef,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceTaxComponentAllocation")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCommerceTaxComponentAllocation:
    """
    Attributes:
        tax_component_ref (Union[Unset, CodatDataContractsDatasetsCommerceTaxComponentRef]):
        tax_amount (Union[Unset, None, float]):
    """

    tax_component_ref: Union[Unset, "CodatDataContractsDatasetsCommerceTaxComponentRef"] = UNSET
    tax_amount: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        tax_component_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_component_ref, Unset):
            tax_component_ref = self.tax_component_ref.to_dict()

        tax_amount = self.tax_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if tax_component_ref is not UNSET:
            field_dict["taxComponentRef"] = tax_component_ref
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_commerce_tax_component_ref import (
            CodatDataContractsDatasetsCommerceTaxComponentRef,
        )

        d = src_dict.copy()
        _tax_component_ref = d.pop("taxComponentRef", UNSET)
        tax_component_ref: Union[Unset, CodatDataContractsDatasetsCommerceTaxComponentRef]
        if isinstance(_tax_component_ref, Unset):
            tax_component_ref = UNSET
        else:
            tax_component_ref = CodatDataContractsDatasetsCommerceTaxComponentRef.from_dict(_tax_component_ref)

        tax_amount = d.pop("taxAmount", UNSET)

        codat_data_contracts_datasets_commerce_tax_component_allocation = cls(
            tax_component_ref=tax_component_ref,
            tax_amount=tax_amount,
        )

        return codat_data_contracts_datasets_commerce_tax_component_allocation
