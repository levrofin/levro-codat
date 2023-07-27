from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_aged_currency_outstanding import (
        CodatDataContractsDatasetsAgedCurrencyOutstanding,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsAgedCreditorOutstanding")


@define
class CodatDataContractsDatasetsAgedCreditorOutstanding:
    """
    Attributes:
        supplier_id (Union[Unset, None, str]):
        supplier_name (Union[Unset, None, str]):
        aged_currency_outstanding (Union[Unset, None, List['CodatDataContractsDatasetsAgedCurrencyOutstanding']]):
    """

    supplier_id: Union[Unset, None, str] = UNSET
    supplier_name: Union[Unset, None, str] = UNSET
    aged_currency_outstanding: Union[Unset, None, List["CodatDataContractsDatasetsAgedCurrencyOutstanding"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        supplier_id = self.supplier_id
        supplier_name = self.supplier_name
        aged_currency_outstanding: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aged_currency_outstanding, Unset):
            if self.aged_currency_outstanding is None:
                aged_currency_outstanding = None
            else:
                aged_currency_outstanding = []
                for aged_currency_outstanding_item_data in self.aged_currency_outstanding:
                    aged_currency_outstanding_item = aged_currency_outstanding_item_data.to_dict()

                    aged_currency_outstanding.append(aged_currency_outstanding_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if supplier_id is not UNSET:
            field_dict["supplierId"] = supplier_id
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if aged_currency_outstanding is not UNSET:
            field_dict["agedCurrencyOutstanding"] = aged_currency_outstanding

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_aged_currency_outstanding import (
            CodatDataContractsDatasetsAgedCurrencyOutstanding,
        )

        d = src_dict.copy()
        supplier_id = d.pop("supplierId", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        aged_currency_outstanding = []
        _aged_currency_outstanding = d.pop("agedCurrencyOutstanding", UNSET)
        for aged_currency_outstanding_item_data in _aged_currency_outstanding or []:
            aged_currency_outstanding_item = CodatDataContractsDatasetsAgedCurrencyOutstanding.from_dict(
                aged_currency_outstanding_item_data
            )

            aged_currency_outstanding.append(aged_currency_outstanding_item)

        codat_data_contracts_datasets_aged_creditor_outstanding = cls(
            supplier_id=supplier_id,
            supplier_name=supplier_name,
            aged_currency_outstanding=aged_currency_outstanding,
        )

        return codat_data_contracts_datasets_aged_creditor_outstanding
