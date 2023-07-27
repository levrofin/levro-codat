import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_commerce_payment_status import (
    CodatDataContractsDatasetsCommercePaymentStatus,
)
from ..models.codat_data_contracts_datasets_commerce_payment_type import CodatDataContractsDatasetsCommercePaymentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
        CodatDataContractsDatasetsDataInterfacesSupplementalData,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsCommercePaymentRef")


@define
class CodatDataContractsDatasetsCommercePaymentRef:
    """
    Attributes:
        id (Union[Unset, None, str]):
        amount (Union[Unset, None, float]):
        currency (Union[Unset, None, str]):
        type (Union[Unset, CodatDataContractsDatasetsCommercePaymentType]):
        status (Union[Unset, CodatDataContractsDatasetsCommercePaymentStatus]):
        payment_provider (Union[Unset, None, str]):
        due_date (Union[Unset, None, datetime.datetime]):
        created_date (Union[Unset, None, datetime.datetime]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        supplemental_data (Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]):
    """

    id: Union[Unset, None, str] = UNSET
    amount: Union[Unset, None, float] = UNSET
    currency: Union[Unset, None, str] = UNSET
    type: Union[Unset, CodatDataContractsDatasetsCommercePaymentType] = UNSET
    status: Union[Unset, CodatDataContractsDatasetsCommercePaymentStatus] = UNSET
    payment_provider: Union[Unset, None, str] = UNSET
    due_date: Union[Unset, None, datetime.datetime] = UNSET
    created_date: Union[Unset, None, datetime.datetime] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    supplemental_data: Union[Unset, "CodatDataContractsDatasetsDataInterfacesSupplementalData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        amount = self.amount
        currency = self.currency
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        payment_provider = self.payment_provider
        due_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat() if self.due_date else None

        created_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat() if self.created_date else None

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        supplemental_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplemental_data, Unset):
            supplemental_data = self.supplemental_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if type is not UNSET:
            field_dict["type"] = type
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
        if supplemental_data is not UNSET:
            field_dict["supplementalData"] = supplemental_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
            CodatDataContractsDatasetsDataInterfacesSupplementalData,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CodatDataContractsDatasetsCommercePaymentType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodatDataContractsDatasetsCommercePaymentType(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CodatDataContractsDatasetsCommercePaymentStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodatDataContractsDatasetsCommercePaymentStatus(_status)

        payment_provider = d.pop("paymentProvider", UNSET)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, None, datetime.datetime]
        if _due_date is None:
            due_date = None
        elif isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, None, datetime.datetime]
        if _created_date is None:
            created_date = None
        elif isinstance(_created_date, Unset):
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

        _supplemental_data = d.pop("supplementalData", UNSET)
        supplemental_data: Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]
        if isinstance(_supplemental_data, Unset):
            supplemental_data = UNSET
        else:
            supplemental_data = CodatDataContractsDatasetsDataInterfacesSupplementalData.from_dict(_supplemental_data)

        codat_data_contracts_datasets_commerce_payment_ref = cls(
            id=id,
            amount=amount,
            currency=currency,
            type=type,
            status=status,
            payment_provider=payment_provider,
            due_date=due_date,
            created_date=created_date,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            supplemental_data=supplemental_data,
        )

        return codat_data_contracts_datasets_commerce_payment_ref
