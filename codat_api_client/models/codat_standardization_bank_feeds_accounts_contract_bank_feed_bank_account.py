import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount")


@attr.s(auto_attribs=True)
class CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount:
    """
    Attributes:
        id (Union[Unset, None, str]):
        account_name (Union[Unset, None, str]):
        account_type (Union[Unset, None, str]):
        account_number (Union[Unset, None, str]):
        sort_code (Union[Unset, None, str]):
        currency (Union[Unset, None, str]):
        balance (Union[Unset, None, float]):
        modified_date (Union[Unset, None, datetime.datetime]):
        status (Union[Unset, None, str]):
        feed_start_date (Union[Unset, None, datetime.datetime]):
    """

    id: Union[Unset, None, str] = UNSET
    account_name: Union[Unset, None, str] = UNSET
    account_type: Union[Unset, None, str] = UNSET
    account_number: Union[Unset, None, str] = UNSET
    sort_code: Union[Unset, None, str] = UNSET
    currency: Union[Unset, None, str] = UNSET
    balance: Union[Unset, None, float] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    status: Union[Unset, None, str] = UNSET
    feed_start_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        account_name = self.account_name
        account_type = self.account_type
        account_number = self.account_number
        sort_code = self.sort_code
        currency = self.currency
        balance = self.balance
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        status = self.status
        feed_start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.feed_start_date, Unset):
            feed_start_date = self.feed_start_date.isoformat() if self.feed_start_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if sort_code is not UNSET:
            field_dict["sortCode"] = sort_code
        if currency is not UNSET:
            field_dict["currency"] = currency
        if balance is not UNSET:
            field_dict["balance"] = balance
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if status is not UNSET:
            field_dict["status"] = status
        if feed_start_date is not UNSET:
            field_dict["feedStartDate"] = feed_start_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        account_name = d.pop("accountName", UNSET)

        account_type = d.pop("accountType", UNSET)

        account_number = d.pop("accountNumber", UNSET)

        sort_code = d.pop("sortCode", UNSET)

        currency = d.pop("currency", UNSET)

        balance = d.pop("balance", UNSET)

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: Union[Unset, None, datetime.datetime]
        if _modified_date is None:
            modified_date = None
        elif isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        status = d.pop("status", UNSET)

        _feed_start_date = d.pop("feedStartDate", UNSET)
        feed_start_date: Union[Unset, None, datetime.datetime]
        if _feed_start_date is None:
            feed_start_date = None
        elif isinstance(_feed_start_date, Unset):
            feed_start_date = UNSET
        else:
            feed_start_date = isoparse(_feed_start_date)

        codat_standardization_bank_feeds_accounts_contract_bank_feed_bank_account = cls(
            id=id,
            account_name=account_name,
            account_type=account_type,
            account_number=account_number,
            sort_code=sort_code,
            currency=currency,
            balance=balance,
            modified_date=modified_date,
            status=status,
            feed_start_date=feed_start_date,
        )

        return codat_standardization_bank_feeds_accounts_contract_bank_feed_bank_account
