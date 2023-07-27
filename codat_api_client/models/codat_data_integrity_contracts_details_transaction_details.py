import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataIntegrityContractsDetailsTransactionDetails")


@define
class CodatDataIntegrityContractsDetailsTransactionDetails:
    """
    Attributes:
        type (Union[Unset, None, str]):
        connection_id (Union[Unset, str]):
        id (Union[Unset, None, str]):
        date (Union[Unset, datetime.datetime]):
        description (Union[Unset, None, str]):
        amount (Union[Unset, None, float]):
        currency (Union[Unset, None, str]):
        matches (Union[Unset, None, List['CodatDataIntegrityContractsDetailsTransactionDetails']]):
    """

    type: Union[Unset, None, str] = UNSET
    connection_id: Union[Unset, str] = UNSET
    id: Union[Unset, None, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, None, str] = UNSET
    amount: Union[Unset, None, float] = UNSET
    currency: Union[Unset, None, str] = UNSET
    matches: Union[Unset, None, List["CodatDataIntegrityContractsDetailsTransactionDetails"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        connection_id = self.connection_id
        id = self.id
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        description = self.description
        amount = self.amount
        currency = self.currency
        matches: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.matches, Unset):
            if self.matches is None:
                matches = None
            else:
                matches = []
                for matches_item_data in self.matches:
                    matches_item = matches_item_data.to_dict()

                    matches.append(matches_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if id is not UNSET:
            field_dict["id"] = id
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if matches is not UNSET:
            field_dict["matches"] = matches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        connection_id = d.pop("connectionId", UNSET)

        id = d.pop("id", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        description = d.pop("description", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        matches = []
        _matches = d.pop("matches", UNSET)
        for matches_item_data in _matches or []:
            matches_item = CodatDataIntegrityContractsDetailsTransactionDetails.from_dict(matches_item_data)

            matches.append(matches_item)

        codat_data_integrity_contracts_details_transaction_details = cls(
            type=type,
            connection_id=connection_id,
            id=id,
            date=date,
            description=description,
            amount=amount,
            currency=currency,
            matches=matches,
        )

        return codat_data_integrity_contracts_details_transaction_details
