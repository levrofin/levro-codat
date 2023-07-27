import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_account_transaction_status import (
    CodatDataContractsDatasetsAccountTransactionStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_account_ref import CodatDataContractsDatasetsAccountRef
    from ..models.codat_data_contracts_datasets_account_transaction_line import (
        CodatDataContractsDatasetsAccountTransactionLine,
    )
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata


T = TypeVar("T", bound="CodatDataContractsDatasetsAccountTransaction")


@define
class CodatDataContractsDatasetsAccountTransaction:
    """
    Attributes:
        id (Union[Unset, None, str]):
        transaction_id (Union[Unset, None, str]):
        note (Union[Unset, None, str]):
        bank_account_ref (Union[Unset, CodatDataContractsDatasetsAccountRef]):
        date (Union[Unset, datetime.datetime]):
        status (Union[Unset, CodatDataContractsDatasetsAccountTransactionStatus]):
        currency (Union[Unset, None, str]):
        currency_rate (Union[Unset, None, float]):
        lines (Union[Unset, None, List['CodatDataContractsDatasetsAccountTransactionLine']]):
        total_amount (Union[Unset, float]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
    """

    id: Union[Unset, None, str] = UNSET
    transaction_id: Union[Unset, None, str] = UNSET
    note: Union[Unset, None, str] = UNSET
    bank_account_ref: Union[Unset, "CodatDataContractsDatasetsAccountRef"] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, CodatDataContractsDatasetsAccountTransactionStatus] = UNSET
    currency: Union[Unset, None, str] = UNSET
    currency_rate: Union[Unset, None, float] = UNSET
    lines: Union[Unset, None, List["CodatDataContractsDatasetsAccountTransactionLine"]] = UNSET
    total_amount: Union[Unset, float] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        transaction_id = self.transaction_id
        note = self.note
        bank_account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bank_account_ref, Unset):
            bank_account_ref = self.bank_account_ref.to_dict()

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        currency = self.currency
        currency_rate = self.currency_rate
        lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            if self.lines is None:
                lines = None
            else:
                lines = []
                for lines_item_data in self.lines:
                    lines_item = lines_item_data.to_dict()

                    lines.append(lines_item)

        total_amount = self.total_amount
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if note is not UNSET:
            field_dict["note"] = note
        if bank_account_ref is not UNSET:
            field_dict["bankAccountRef"] = bank_account_ref
        if date is not UNSET:
            field_dict["date"] = date
        if status is not UNSET:
            field_dict["status"] = status
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if lines is not UNSET:
            field_dict["lines"] = lines
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_account_ref import CodatDataContractsDatasetsAccountRef
        from ..models.codat_data_contracts_datasets_account_transaction_line import (
            CodatDataContractsDatasetsAccountTransactionLine,
        )
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        note = d.pop("note", UNSET)

        _bank_account_ref = d.pop("bankAccountRef", UNSET)
        bank_account_ref: Union[Unset, CodatDataContractsDatasetsAccountRef]
        if isinstance(_bank_account_ref, Unset):
            bank_account_ref = UNSET
        else:
            bank_account_ref = CodatDataContractsDatasetsAccountRef.from_dict(_bank_account_ref)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CodatDataContractsDatasetsAccountTransactionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodatDataContractsDatasetsAccountTransactionStatus(_status)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = CodatDataContractsDatasetsAccountTransactionLine.from_dict(lines_item_data)

            lines.append(lines_item)

        total_amount = d.pop("totalAmount", UNSET)

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

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CodatDataContractsDatasetsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CodatDataContractsDatasetsMetadata.from_dict(_metadata)

        codat_data_contracts_datasets_account_transaction = cls(
            id=id,
            transaction_id=transaction_id,
            note=note,
            bank_account_ref=bank_account_ref,
            date=date,
            status=status,
            currency=currency,
            currency_rate=currency_rate,
            lines=lines,
            total_amount=total_amount,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            metadata=metadata,
        )

        return codat_data_contracts_datasets_account_transaction
