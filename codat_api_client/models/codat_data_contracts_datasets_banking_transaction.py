import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_banking_banking_transaction_code import (
    CodatDataContractsDatasetsBankingBankingTransactionCode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_banking_transaction_category_ref import (
        CodatDataContractsDatasetsBankingTransactionCategoryRef,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsBankingTransaction")


@define
class CodatDataContractsDatasetsBankingTransaction:
    """
    Attributes:
        id (str):
        account_id (str):
        currency (str):
        description (Union[Unset, None, str]):
        amount (Union[Unset, float]):
        posted_date (Union[Unset, datetime.datetime]):
        authorized_date (Union[Unset, None, datetime.datetime]):
        code (Union[Unset, CodatDataContractsDatasetsBankingBankingTransactionCode]):
        merchant_name (Union[Unset, None, str]):
        transaction_category_ref (Union[Unset, CodatDataContractsDatasetsBankingTransactionCategoryRef]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    id: str
    account_id: str
    currency: str
    description: Union[Unset, None, str] = UNSET
    amount: Union[Unset, float] = UNSET
    posted_date: Union[Unset, datetime.datetime] = UNSET
    authorized_date: Union[Unset, None, datetime.datetime] = UNSET
    code: Union[Unset, CodatDataContractsDatasetsBankingBankingTransactionCode] = UNSET
    merchant_name: Union[Unset, None, str] = UNSET
    transaction_category_ref: Union[Unset, "CodatDataContractsDatasetsBankingTransactionCategoryRef"] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        account_id = self.account_id
        currency = self.currency
        description = self.description
        amount = self.amount
        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        authorized_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.authorized_date, Unset):
            authorized_date = self.authorized_date.isoformat() if self.authorized_date else None

        code: Union[Unset, str] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        merchant_name = self.merchant_name
        transaction_category_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transaction_category_ref, Unset):
            transaction_category_ref = self.transaction_category_ref.to_dict()

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "accountId": account_id,
                "currency": currency,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if amount is not UNSET:
            field_dict["amount"] = amount
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date
        if authorized_date is not UNSET:
            field_dict["authorizedDate"] = authorized_date
        if code is not UNSET:
            field_dict["code"] = code
        if merchant_name is not UNSET:
            field_dict["merchantName"] = merchant_name
        if transaction_category_ref is not UNSET:
            field_dict["transactionCategoryRef"] = transaction_category_ref
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_banking_transaction_category_ref import (
            CodatDataContractsDatasetsBankingTransactionCategoryRef,
        )

        d = src_dict.copy()
        id = d.pop("id")

        account_id = d.pop("accountId")

        currency = d.pop("currency")

        description = d.pop("description", UNSET)

        amount = d.pop("amount", UNSET)

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.datetime]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date)

        _authorized_date = d.pop("authorizedDate", UNSET)
        authorized_date: Union[Unset, None, datetime.datetime]
        if _authorized_date is None:
            authorized_date = None
        elif isinstance(_authorized_date, Unset):
            authorized_date = UNSET
        else:
            authorized_date = isoparse(_authorized_date)

        _code = d.pop("code", UNSET)
        code: Union[Unset, CodatDataContractsDatasetsBankingBankingTransactionCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = CodatDataContractsDatasetsBankingBankingTransactionCode(_code)

        merchant_name = d.pop("merchantName", UNSET)

        _transaction_category_ref = d.pop("transactionCategoryRef", UNSET)
        transaction_category_ref: Union[Unset, CodatDataContractsDatasetsBankingTransactionCategoryRef]
        if isinstance(_transaction_category_ref, Unset):
            transaction_category_ref = UNSET
        else:
            transaction_category_ref = CodatDataContractsDatasetsBankingTransactionCategoryRef.from_dict(
                _transaction_category_ref
            )

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

        codat_data_contracts_datasets_banking_transaction = cls(
            id=id,
            account_id=account_id,
            currency=currency,
            description=description,
            amount=amount,
            posted_date=posted_date,
            authorized_date=authorized_date,
            code=code,
            merchant_name=merchant_name,
            transaction_category_ref=transaction_category_ref,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_banking_transaction
