import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_commerce_dispute_status import (
    CodatDataContractsDatasetsCommerceDisputeStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_transaction_source_ref import (
        CodatDataContractsDatasetsCommerceTransactionSourceRef,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceDispute")


@define
class CodatDataContractsDatasetsCommerceDispute:
    """
    Attributes:
        id (Union[Unset, None, str]):
        disputed_transactions (Union[Unset, None, List['CodatDataContractsDatasetsCommerceTransactionSourceRef']]):
        total_amount (Union[Unset, float]):
        currency (Union[Unset, None, str]):
        status (Union[Unset, CodatDataContractsDatasetsCommerceDisputeStatus]):
        reason (Union[Unset, None, str]):
        due_date (Union[Unset, datetime.datetime]):
        created_date (Union[Unset, datetime.datetime]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    id: Union[Unset, None, str] = UNSET
    disputed_transactions: Union[Unset, None, List["CodatDataContractsDatasetsCommerceTransactionSourceRef"]] = UNSET
    total_amount: Union[Unset, float] = UNSET
    currency: Union[Unset, None, str] = UNSET
    status: Union[Unset, CodatDataContractsDatasetsCommerceDisputeStatus] = UNSET
    reason: Union[Unset, None, str] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        disputed_transactions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.disputed_transactions, Unset):
            if self.disputed_transactions is None:
                disputed_transactions = None
            else:
                disputed_transactions = []
                for disputed_transactions_item_data in self.disputed_transactions:
                    disputed_transactions_item = disputed_transactions_item_data.to_dict()

                    disputed_transactions.append(disputed_transactions_item)

        total_amount = self.total_amount
        currency = self.currency
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        reason = self.reason
        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

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
        if disputed_transactions is not UNSET:
            field_dict["disputedTransactions"] = disputed_transactions
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if status is not UNSET:
            field_dict["status"] = status
        if reason is not UNSET:
            field_dict["reason"] = reason
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_commerce_transaction_source_ref import (
            CodatDataContractsDatasetsCommerceTransactionSourceRef,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        disputed_transactions = []
        _disputed_transactions = d.pop("disputedTransactions", UNSET)
        for disputed_transactions_item_data in _disputed_transactions or []:
            disputed_transactions_item = CodatDataContractsDatasetsCommerceTransactionSourceRef.from_dict(
                disputed_transactions_item_data
            )

            disputed_transactions.append(disputed_transactions_item)

        total_amount = d.pop("totalAmount", UNSET)

        currency = d.pop("currency", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CodatDataContractsDatasetsCommerceDisputeStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodatDataContractsDatasetsCommerceDisputeStatus(_status)

        reason = d.pop("reason", UNSET)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

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

        codat_data_contracts_datasets_commerce_dispute = cls(
            id=id,
            disputed_transactions=disputed_transactions,
            total_amount=total_amount,
            currency=currency,
            status=status,
            reason=reason,
            due_date=due_date,
            created_date=created_date,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_commerce_dispute
