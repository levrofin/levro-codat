import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_payment_line_link import CodatDataContractsDatasetsPaymentLineLink


T = TypeVar("T", bound="CodatDataContractsDatasetsPaymentLine")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsPaymentLine:
    """
    Attributes:
        amount (float):
        links (Union[Unset, None, List['CodatDataContractsDatasetsPaymentLineLink']]):
        allocated_on_date (Union[Unset, None, datetime.datetime]):
    """

    amount: float
    links: Union[Unset, None, List["CodatDataContractsDatasetsPaymentLineLink"]] = UNSET
    allocated_on_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            if self.links is None:
                links = None
            else:
                links = []
                for links_item_data in self.links:
                    links_item = links_item_data.to_dict()

                    links.append(links_item)

        allocated_on_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.allocated_on_date, Unset):
            allocated_on_date = self.allocated_on_date.isoformat() if self.allocated_on_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "amount": amount,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if allocated_on_date is not UNSET:
            field_dict["allocatedOnDate"] = allocated_on_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_payment_line_link import CodatDataContractsDatasetsPaymentLineLink

        d = src_dict.copy()
        amount = d.pop("amount")

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = CodatDataContractsDatasetsPaymentLineLink.from_dict(links_item_data)

            links.append(links_item)

        _allocated_on_date = d.pop("allocatedOnDate", UNSET)
        allocated_on_date: Union[Unset, None, datetime.datetime]
        if _allocated_on_date is None:
            allocated_on_date = None
        elif isinstance(_allocated_on_date, Unset):
            allocated_on_date = UNSET
        else:
            allocated_on_date = isoparse(_allocated_on_date)

        codat_data_contracts_datasets_payment_line = cls(
            amount=amount,
            links=links,
            allocated_on_date=allocated_on_date,
        )

        return codat_data_contracts_datasets_payment_line
