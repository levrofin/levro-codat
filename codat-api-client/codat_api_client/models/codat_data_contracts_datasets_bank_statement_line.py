import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_transaction_type import CodatDataContractsDatasetsTransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsBankStatementLine")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsBankStatementLine:
    """
    Attributes:
        date (datetime.datetime):
        reconciled (bool):
        amount (float):
        balance (float):
        transaction_type (CodatDataContractsDatasetsTransactionType):
        id (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        counterparty (Union[Unset, None, str]):
        reference (Union[Unset, None, str]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    date: datetime.datetime
    reconciled: bool
    amount: float
    balance: float
    transaction_type: CodatDataContractsDatasetsTransactionType
    id: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    counterparty: Union[Unset, None, str] = UNSET
    reference: Union[Unset, None, str] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        date = self.date.isoformat()

        reconciled = self.reconciled
        amount = self.amount
        balance = self.balance
        transaction_type = self.transaction_type.value

        id = self.id
        description = self.description
        counterparty = self.counterparty
        reference = self.reference
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "date": date,
                "reconciled": reconciled,
                "amount": amount,
                "balance": balance,
                "transactionType": transaction_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if counterparty is not UNSET:
            field_dict["counterparty"] = counterparty
        if reference is not UNSET:
            field_dict["reference"] = reference
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = isoparse(d.pop("date"))

        reconciled = d.pop("reconciled")

        amount = d.pop("amount")

        balance = d.pop("balance")

        transaction_type = CodatDataContractsDatasetsTransactionType(d.pop("transactionType"))

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        counterparty = d.pop("counterparty", UNSET)

        reference = d.pop("reference", UNSET)

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

        codat_data_contracts_datasets_bank_statement_line = cls(
            date=date,
            reconciled=reconciled,
            amount=amount,
            balance=balance,
            transaction_type=transaction_type,
            id=id,
            description=description,
            counterparty=counterparty,
            reference=reference,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_bank_statement_line
