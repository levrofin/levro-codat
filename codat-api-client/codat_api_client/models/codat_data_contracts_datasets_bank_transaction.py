import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_transaction_type import CodatDataContractsDatasetsTransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsBankTransaction")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsBankTransaction:
    """
    Attributes:
        id (Union[Unset, None, str]):
        account_id (Union[Unset, None, str]):
        cleared_on_date (Union[Unset, datetime.datetime]):
        description (Union[Unset, None, str]):
        counterparty (Union[Unset, None, str]):
        reference (Union[Unset, None, str]):
        reconciled (Union[Unset, bool]):
        amount (Union[Unset, None, float]):
        balance (Union[Unset, None, float]):
        transaction_type (Union[Unset, CodatDataContractsDatasetsTransactionType]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    id: Union[Unset, None, str] = UNSET
    account_id: Union[Unset, None, str] = UNSET
    cleared_on_date: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, None, str] = UNSET
    counterparty: Union[Unset, None, str] = UNSET
    reference: Union[Unset, None, str] = UNSET
    reconciled: Union[Unset, bool] = UNSET
    amount: Union[Unset, None, float] = UNSET
    balance: Union[Unset, None, float] = UNSET
    transaction_type: Union[Unset, CodatDataContractsDatasetsTransactionType] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        account_id = self.account_id
        cleared_on_date: Union[Unset, str] = UNSET
        if not isinstance(self.cleared_on_date, Unset):
            cleared_on_date = self.cleared_on_date.isoformat()

        description = self.description
        counterparty = self.counterparty
        reference = self.reference
        reconciled = self.reconciled
        amount = self.amount
        balance = self.balance
        transaction_type: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = self.transaction_type.value

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if cleared_on_date is not UNSET:
            field_dict["clearedOnDate"] = cleared_on_date
        if description is not UNSET:
            field_dict["description"] = description
        if counterparty is not UNSET:
            field_dict["counterparty"] = counterparty
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reconciled is not UNSET:
            field_dict["reconciled"] = reconciled
        if amount is not UNSET:
            field_dict["amount"] = amount
        if balance is not UNSET:
            field_dict["balance"] = balance
        if transaction_type is not UNSET:
            field_dict["transactionType"] = transaction_type
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        account_id = d.pop("accountId", UNSET)

        _cleared_on_date = d.pop("clearedOnDate", UNSET)
        cleared_on_date: Union[Unset, datetime.datetime]
        if isinstance(_cleared_on_date, Unset):
            cleared_on_date = UNSET
        else:
            cleared_on_date = isoparse(_cleared_on_date)

        description = d.pop("description", UNSET)

        counterparty = d.pop("counterparty", UNSET)

        reference = d.pop("reference", UNSET)

        reconciled = d.pop("reconciled", UNSET)

        amount = d.pop("amount", UNSET)

        balance = d.pop("balance", UNSET)

        _transaction_type = d.pop("transactionType", UNSET)
        transaction_type: Union[Unset, CodatDataContractsDatasetsTransactionType]
        if isinstance(_transaction_type, Unset):
            transaction_type = UNSET
        else:
            transaction_type = CodatDataContractsDatasetsTransactionType(_transaction_type)

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

        codat_data_contracts_datasets_bank_transaction = cls(
            id=id,
            account_id=account_id,
            cleared_on_date=cleared_on_date,
            description=description,
            counterparty=counterparty,
            reference=reference,
            reconciled=reconciled,
            amount=amount,
            balance=balance,
            transaction_type=transaction_type,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_bank_transaction
