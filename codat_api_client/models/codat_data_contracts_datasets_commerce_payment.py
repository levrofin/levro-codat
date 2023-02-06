import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_commerce_payment_status import (
    CodatDataContractsDatasetsCommercePaymentStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_payment_method_ref import (
        CodatDataContractsDatasetsCommercePaymentMethodRef,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsCommercePayment")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCommercePayment:
    """
    Attributes:
        id (Union[Unset, None, str]):
        amount (Union[Unset, float]):
        currency (Union[Unset, None, str]):
        payment_method_ref (Union[Unset, CodatDataContractsDatasetsCommercePaymentMethodRef]):
        status (Union[Unset, CodatDataContractsDatasetsCommercePaymentStatus]):
        payment_provider (Union[Unset, None, str]):
        due_date (Union[Unset, datetime.datetime]):
        created_date (Union[Unset, datetime.datetime]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    id: Union[Unset, None, str] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, None, str] = UNSET
    payment_method_ref: Union[Unset, "CodatDataContractsDatasetsCommercePaymentMethodRef"] = UNSET
    status: Union[Unset, CodatDataContractsDatasetsCommercePaymentStatus] = UNSET
    payment_provider: Union[Unset, None, str] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        amount = self.amount
        currency = self.currency
        payment_method_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_ref, Unset):
            payment_method_ref = self.payment_method_ref.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        payment_provider = self.payment_provider
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
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if payment_method_ref is not UNSET:
            field_dict["paymentMethodRef"] = payment_method_ref
        if status is not UNSET:
            field_dict["status"] = status
        if payment_provider is not UNSET:
            field_dict["paymentProvider"] = payment_provider
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
        from ..models.codat_data_contracts_datasets_commerce_payment_method_ref import (
            CodatDataContractsDatasetsCommercePaymentMethodRef,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        _payment_method_ref = d.pop("paymentMethodRef", UNSET)
        payment_method_ref: Union[Unset, CodatDataContractsDatasetsCommercePaymentMethodRef]
        if isinstance(_payment_method_ref, Unset):
            payment_method_ref = UNSET
        else:
            payment_method_ref = CodatDataContractsDatasetsCommercePaymentMethodRef.from_dict(_payment_method_ref)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CodatDataContractsDatasetsCommercePaymentStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodatDataContractsDatasetsCommercePaymentStatus(_status)

        payment_provider = d.pop("paymentProvider", UNSET)

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

        codat_data_contracts_datasets_commerce_payment = cls(
            id=id,
            amount=amount,
            currency=currency,
            payment_method_ref=payment_method_ref,
            status=status,
            payment_provider=payment_provider,
            due_date=due_date,
            created_date=created_date,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_commerce_payment
