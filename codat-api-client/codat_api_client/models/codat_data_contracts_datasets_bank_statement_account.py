import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsBankStatementAccount")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsBankStatementAccount:
    """
    Attributes:
        id (Union[Unset, None, str]):
        account_name (Union[Unset, None, str]):
        from_date (Union[Unset, datetime.datetime]):
        to_date (Union[Unset, datetime.datetime]):
        nominal_code (Union[Unset, None, str]):
        sort_code (Union[Unset, None, str]):
        account_number (Union[Unset, None, str]):
        iban (Union[Unset, None, str]):
        currency (Union[Unset, None, str]):
        balance (Union[Unset, None, float]):
        available_balance (Union[Unset, None, float]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        overdraft_limit (Union[Unset, None, float]):
        institution (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    account_name: Union[Unset, None, str] = UNSET
    from_date: Union[Unset, datetime.datetime] = UNSET
    to_date: Union[Unset, datetime.datetime] = UNSET
    nominal_code: Union[Unset, None, str] = UNSET
    sort_code: Union[Unset, None, str] = UNSET
    account_number: Union[Unset, None, str] = UNSET
    iban: Union[Unset, None, str] = UNSET
    currency: Union[Unset, None, str] = UNSET
    balance: Union[Unset, None, float] = UNSET
    available_balance: Union[Unset, None, float] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    overdraft_limit: Union[Unset, None, float] = UNSET
    institution: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        account_name = self.account_name
        from_date: Union[Unset, str] = UNSET
        if not isinstance(self.from_date, Unset):
            from_date = self.from_date.isoformat()

        to_date: Union[Unset, str] = UNSET
        if not isinstance(self.to_date, Unset):
            to_date = self.to_date.isoformat()

        nominal_code = self.nominal_code
        sort_code = self.sort_code
        account_number = self.account_number
        iban = self.iban
        currency = self.currency
        balance = self.balance
        available_balance = self.available_balance
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        overdraft_limit = self.overdraft_limit
        institution = self.institution

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if from_date is not UNSET:
            field_dict["fromDate"] = from_date
        if to_date is not UNSET:
            field_dict["toDate"] = to_date
        if nominal_code is not UNSET:
            field_dict["nominalCode"] = nominal_code
        if sort_code is not UNSET:
            field_dict["sortCode"] = sort_code
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if iban is not UNSET:
            field_dict["iban"] = iban
        if currency is not UNSET:
            field_dict["currency"] = currency
        if balance is not UNSET:
            field_dict["balance"] = balance
        if available_balance is not UNSET:
            field_dict["availableBalance"] = available_balance
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if overdraft_limit is not UNSET:
            field_dict["overdraftLimit"] = overdraft_limit
        if institution is not UNSET:
            field_dict["institution"] = institution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        account_name = d.pop("accountName", UNSET)

        _from_date = d.pop("fromDate", UNSET)
        from_date: Union[Unset, datetime.datetime]
        if isinstance(_from_date, Unset):
            from_date = UNSET
        else:
            from_date = isoparse(_from_date)

        _to_date = d.pop("toDate", UNSET)
        to_date: Union[Unset, datetime.datetime]
        if isinstance(_to_date, Unset):
            to_date = UNSET
        else:
            to_date = isoparse(_to_date)

        nominal_code = d.pop("nominalCode", UNSET)

        sort_code = d.pop("sortCode", UNSET)

        account_number = d.pop("accountNumber", UNSET)

        iban = d.pop("iban", UNSET)

        currency = d.pop("currency", UNSET)

        balance = d.pop("balance", UNSET)

        available_balance = d.pop("availableBalance", UNSET)

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

        overdraft_limit = d.pop("overdraftLimit", UNSET)

        institution = d.pop("institution", UNSET)

        codat_data_contracts_datasets_bank_statement_account = cls(
            id=id,
            account_name=account_name,
            from_date=from_date,
            to_date=to_date,
            nominal_code=nominal_code,
            sort_code=sort_code,
            account_number=account_number,
            iban=iban,
            currency=currency,
            balance=balance,
            available_balance=available_balance,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            overdraft_limit=overdraft_limit,
            institution=institution,
        )

        return codat_data_contracts_datasets_bank_statement_account
