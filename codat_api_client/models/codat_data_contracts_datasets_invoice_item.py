from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_account_ref import CodatDataContractsDatasetsAccountRef
    from ..models.codat_data_contracts_datasets_tax_rate_ref import CodatDataContractsDatasetsTaxRateRef


T = TypeVar("T", bound="CodatDataContractsDatasetsInvoiceItem")


@define
class CodatDataContractsDatasetsInvoiceItem:
    """
    Attributes:
        description (Union[Unset, None, str]):
        unit_price (Union[Unset, None, float]):
        account_ref (Union[Unset, CodatDataContractsDatasetsAccountRef]):
        tax_rate_ref (Union[Unset, CodatDataContractsDatasetsTaxRateRef]):
    """

    description: Union[Unset, None, str] = UNSET
    unit_price: Union[Unset, None, float] = UNSET
    account_ref: Union[Unset, "CodatDataContractsDatasetsAccountRef"] = UNSET
    tax_rate_ref: Union[Unset, "CodatDataContractsDatasetsTaxRateRef"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        unit_price = self.unit_price
        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_account_ref import CodatDataContractsDatasetsAccountRef
        from ..models.codat_data_contracts_datasets_tax_rate_ref import CodatDataContractsDatasetsTaxRateRef

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, CodatDataContractsDatasetsAccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = CodatDataContractsDatasetsAccountRef.from_dict(_account_ref)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, CodatDataContractsDatasetsTaxRateRef]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = CodatDataContractsDatasetsTaxRateRef.from_dict(_tax_rate_ref)

        codat_data_contracts_datasets_invoice_item = cls(
            description=description,
            unit_price=unit_price,
            account_ref=account_ref,
            tax_rate_ref=tax_rate_ref,
        )

        return codat_data_contracts_datasets_invoice_item
