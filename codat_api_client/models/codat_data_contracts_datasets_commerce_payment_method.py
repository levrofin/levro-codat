import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_commerce_payment_method_status import (
    CodatDataContractsDatasetsCommercePaymentMethodStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsCommercePaymentMethod")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCommercePaymentMethod:
    """
    Attributes:
        id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        status (Union[Unset, CodatDataContractsDatasetsCommercePaymentMethodStatus]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    status: Union[Unset, CodatDataContractsDatasetsCommercePaymentMethodStatus] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CodatDataContractsDatasetsCommercePaymentMethodStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodatDataContractsDatasetsCommercePaymentMethodStatus(_status)

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

        codat_data_contracts_datasets_commerce_payment_method = cls(
            id=id,
            name=name,
            status=status,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_commerce_payment_method
