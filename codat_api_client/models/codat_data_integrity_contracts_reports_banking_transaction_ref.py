import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataIntegrityContractsReportsBankingTransactionRef")


@define
class CodatDataIntegrityContractsReportsBankingTransactionRef:
    """
    Attributes:
        id (Union[Unset, None, str]):
        data_connection_id (Union[Unset, str]):
        account_id (Union[Unset, None, str]):
        account_name (Union[Unset, None, str]):
        date (Union[Unset, datetime.datetime]):
        description (Union[Unset, None, str]):
        amount (Union[Unset, float]):
    """

    id: Union[Unset, None, str] = UNSET
    data_connection_id: Union[Unset, str] = UNSET
    account_id: Union[Unset, None, str] = UNSET
    account_name: Union[Unset, None, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, None, str] = UNSET
    amount: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        data_connection_id = self.data_connection_id
        account_id = self.account_id
        account_name = self.account_name
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        description = self.description
        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if data_connection_id is not UNSET:
            field_dict["dataConnectionId"] = data_connection_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        data_connection_id = d.pop("dataConnectionId", UNSET)

        account_id = d.pop("accountId", UNSET)

        account_name = d.pop("accountName", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        description = d.pop("description", UNSET)

        amount = d.pop("amount", UNSET)

        codat_data_integrity_contracts_reports_banking_transaction_ref = cls(
            id=id,
            data_connection_id=data_connection_id,
            account_id=account_id,
            account_name=account_name,
            date=date,
            description=description,
            amount=amount,
        )

        return codat_data_integrity_contracts_reports_banking_transaction_ref
