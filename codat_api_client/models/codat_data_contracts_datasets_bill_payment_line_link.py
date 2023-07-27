from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..models.codat_data_contracts_datasets_bill_payment_link_type import CodatDataContractsDatasetsBillPaymentLinkType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsBillPaymentLineLink")


@define
class CodatDataContractsDatasetsBillPaymentLineLink:
    """
    Attributes:
        type (CodatDataContractsDatasetsBillPaymentLinkType):
        id (Union[Unset, None, str]):
        amount (Union[Unset, None, float]):
        currency_rate (Union[Unset, None, float]):
    """

    type: CodatDataContractsDatasetsBillPaymentLinkType
    id: Union[Unset, None, str] = UNSET
    amount: Union[Unset, None, float] = UNSET
    currency_rate: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id
        amount = self.amount
        currency_rate = self.currency_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = CodatDataContractsDatasetsBillPaymentLinkType(d.pop("type"))

        id = d.pop("id", UNSET)

        amount = d.pop("amount", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        codat_data_contracts_datasets_bill_payment_line_link = cls(
            type=type,
            id=id,
            amount=amount,
            currency_rate=currency_rate,
        )

        return codat_data_contracts_datasets_bill_payment_line_link
