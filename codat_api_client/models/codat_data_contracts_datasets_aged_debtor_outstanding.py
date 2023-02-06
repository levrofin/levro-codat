from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_aged_currency_outstanding import (
        CodatDataContractsDatasetsAgedCurrencyOutstanding,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsAgedDebtorOutstanding")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsAgedDebtorOutstanding:
    """
    Attributes:
        customer_id (Union[Unset, None, str]):
        customer_name (Union[Unset, None, str]):
        aged_currency_outstanding (Union[Unset, None, List['CodatDataContractsDatasetsAgedCurrencyOutstanding']]):
    """

    customer_id: Union[Unset, None, str] = UNSET
    customer_name: Union[Unset, None, str] = UNSET
    aged_currency_outstanding: Union[Unset, None, List["CodatDataContractsDatasetsAgedCurrencyOutstanding"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id
        customer_name = self.customer_name
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
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name
        if aged_currency_outstanding is not UNSET:
            field_dict["agedCurrencyOutstanding"] = aged_currency_outstanding

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_aged_currency_outstanding import (
            CodatDataContractsDatasetsAgedCurrencyOutstanding,
        )

        d = src_dict.copy()
        customer_id = d.pop("customerId", UNSET)

        customer_name = d.pop("customerName", UNSET)

        aged_currency_outstanding = []
        _aged_currency_outstanding = d.pop("agedCurrencyOutstanding", UNSET)
        for aged_currency_outstanding_item_data in _aged_currency_outstanding or []:
            aged_currency_outstanding_item = CodatDataContractsDatasetsAgedCurrencyOutstanding.from_dict(
                aged_currency_outstanding_item_data
            )

            aged_currency_outstanding.append(aged_currency_outstanding_item)

        codat_data_contracts_datasets_aged_debtor_outstanding = cls(
            customer_id=customer_id,
            customer_name=customer_name,
            aged_currency_outstanding=aged_currency_outstanding,
        )

        return codat_data_contracts_datasets_aged_debtor_outstanding
