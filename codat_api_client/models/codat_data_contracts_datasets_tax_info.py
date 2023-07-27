from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_tax_rate_ref import CodatDataContractsDatasetsTaxRateRef


T = TypeVar("T", bound="CodatDataContractsDatasetsTaxInfo")


@define
class CodatDataContractsDatasetsTaxInfo:
    """
    Attributes:
        tax_rate_ref (CodatDataContractsDatasetsTaxRateRef):
        tax_amount (float):
    """

    tax_rate_ref: "CodatDataContractsDatasetsTaxRateRef"
    tax_amount: float

    def to_dict(self) -> Dict[str, Any]:
        tax_rate_ref = self.tax_rate_ref.to_dict()

        tax_amount = self.tax_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "taxRateRef": tax_rate_ref,
                "taxAmount": tax_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_tax_rate_ref import CodatDataContractsDatasetsTaxRateRef

        d = src_dict.copy()
        tax_rate_ref = CodatDataContractsDatasetsTaxRateRef.from_dict(d.pop("taxRateRef"))

        tax_amount = d.pop("taxAmount")

        codat_data_contracts_datasets_tax_info = cls(
            tax_rate_ref=tax_rate_ref,
            tax_amount=tax_amount,
        )

        return codat_data_contracts_datasets_tax_info
