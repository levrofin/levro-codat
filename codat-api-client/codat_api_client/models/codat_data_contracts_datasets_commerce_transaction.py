import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_commerce_platform_transaction_type import (
    CodatDataContractsDatasetsCommercePlatformTransactionType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_transaction_source_ref import (
        CodatDataContractsDatasetsCommerceTransactionSourceRef,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceTransaction")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCommerceTransaction:
    """
    Attributes:
        id (Union[Unset, None, str]):
        total_amount (Union[Unset, float]):
        currency (Union[Unset, None, str]):
        type (Union[Unset, CodatDataContractsDatasetsCommercePlatformTransactionType]):
        sub_type (Union[Unset, None, str]):
        transaction_source_ref (Union[Unset, CodatDataContractsDatasetsCommerceTransactionSourceRef]):
        created_date (Union[Unset, datetime.datetime]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    id: Union[Unset, None, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    currency: Union[Unset, None, str] = UNSET
    type: Union[Unset, CodatDataContractsDatasetsCommercePlatformTransactionType] = UNSET
    sub_type: Union[Unset, None, str] = UNSET
    transaction_source_ref: Union[Unset, "CodatDataContractsDatasetsCommerceTransactionSourceRef"] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        total_amount = self.total_amount
        currency = self.currency
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        sub_type = self.sub_type
        transaction_source_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transaction_source_ref, Unset):
            transaction_source_ref = self.transaction_source_ref.to_dict()

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
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if type is not UNSET:
            field_dict["type"] = type
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if transaction_source_ref is not UNSET:
            field_dict["transactionSourceRef"] = transaction_source_ref
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

        total_amount = d.pop("totalAmount", UNSET)

        currency = d.pop("currency", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CodatDataContractsDatasetsCommercePlatformTransactionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodatDataContractsDatasetsCommercePlatformTransactionType(_type)

        sub_type = d.pop("subType", UNSET)

        _transaction_source_ref = d.pop("transactionSourceRef", UNSET)
        transaction_source_ref: Union[Unset, CodatDataContractsDatasetsCommerceTransactionSourceRef]
        if isinstance(_transaction_source_ref, Unset):
            transaction_source_ref = UNSET
        else:
            transaction_source_ref = CodatDataContractsDatasetsCommerceTransactionSourceRef.from_dict(
                _transaction_source_ref
            )

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

        codat_data_contracts_datasets_commerce_transaction = cls(
            id=id,
            total_amount=total_amount,
            currency=currency,
            type=type,
            sub_type=sub_type,
            transaction_source_ref=transaction_source_ref,
            created_date=created_date,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_commerce_transaction
