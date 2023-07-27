from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_aged_outstanding_amount import (
        CodatDataContractsDatasetsAgedOutstandingAmount,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsAgedCurrencyOutstanding")


@define
class CodatDataContractsDatasetsAgedCurrencyOutstanding:
    """
    Attributes:
        currency (Union[Unset, None, str]):
        aged_outstanding_amounts (Union[Unset, None, List['CodatDataContractsDatasetsAgedOutstandingAmount']]):
    """

    currency: Union[Unset, None, str] = UNSET
    aged_outstanding_amounts: Union[Unset, None, List["CodatDataContractsDatasetsAgedOutstandingAmount"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency
        aged_outstanding_amounts: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aged_outstanding_amounts, Unset):
            if self.aged_outstanding_amounts is None:
                aged_outstanding_amounts = None
            else:
                aged_outstanding_amounts = []
                for aged_outstanding_amounts_item_data in self.aged_outstanding_amounts:
                    aged_outstanding_amounts_item = aged_outstanding_amounts_item_data.to_dict()

                    aged_outstanding_amounts.append(aged_outstanding_amounts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if aged_outstanding_amounts is not UNSET:
            field_dict["agedOutstandingAmounts"] = aged_outstanding_amounts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_aged_outstanding_amount import (
            CodatDataContractsDatasetsAgedOutstandingAmount,
        )

        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        aged_outstanding_amounts = []
        _aged_outstanding_amounts = d.pop("agedOutstandingAmounts", UNSET)
        for aged_outstanding_amounts_item_data in _aged_outstanding_amounts or []:
            aged_outstanding_amounts_item = CodatDataContractsDatasetsAgedOutstandingAmount.from_dict(
                aged_outstanding_amounts_item_data
            )

            aged_outstanding_amounts.append(aged_outstanding_amounts_item)

        codat_data_contracts_datasets_aged_currency_outstanding = cls(
            currency=currency,
            aged_outstanding_amounts=aged_outstanding_amounts,
        )

        return codat_data_contracts_datasets_aged_currency_outstanding
