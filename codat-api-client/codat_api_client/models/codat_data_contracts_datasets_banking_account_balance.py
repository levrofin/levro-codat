import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_banking_account_balance_amounts import (
        CodatDataContractsDatasetsBankingAccountBalanceAmounts,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsBankingAccountBalance")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsBankingAccountBalance:
    """
    Attributes:
        account_id (str):
        balance (CodatDataContractsDatasetsBankingAccountBalanceAmounts):
        date (datetime.datetime):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    account_id: str
    balance: "CodatDataContractsDatasetsBankingAccountBalanceAmounts"
    date: datetime.datetime
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        balance = self.balance.to_dict()

        date = self.date.isoformat()

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "accountId": account_id,
                "balance": balance,
                "date": date,
            }
        )
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_banking_account_balance_amounts import (
            CodatDataContractsDatasetsBankingAccountBalanceAmounts,
        )

        d = src_dict.copy()
        account_id = d.pop("accountId")

        balance = CodatDataContractsDatasetsBankingAccountBalanceAmounts.from_dict(d.pop("balance"))

        date = isoparse(d.pop("date"))

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: Union[Unset, None, datetime.datetime]
        if _modified_date is None:
            modified_date = None
        elif isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, None, datetime.datetime]
        if _source_modified_date is None:
            source_modified_date = None
        elif isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        codat_data_contracts_datasets_banking_account_balance = cls(
            account_id=account_id,
            balance=balance,
            date=date,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_banking_account_balance
