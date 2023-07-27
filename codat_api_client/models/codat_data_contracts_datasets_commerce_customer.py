import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_address import CodatDataContractsDatasetsCommerceAddress


T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceCustomer")


@define
class CodatDataContractsDatasetsCommerceCustomer:
    """
    Attributes:
        id (Union[Unset, None, str]):
        customer_name (Union[Unset, None, str]):
        email_address (Union[Unset, None, str]):
        default_currency (Union[Unset, None, str]):
        phone (Union[Unset, None, str]):
        addresses (Union[Unset, None, List['CodatDataContractsDatasetsCommerceAddress']]):
        note (Union[Unset, None, str]):
        created_date (Union[Unset, datetime.datetime]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    id: Union[Unset, None, str] = UNSET
    customer_name: Union[Unset, None, str] = UNSET
    email_address: Union[Unset, None, str] = UNSET
    default_currency: Union[Unset, None, str] = UNSET
    phone: Union[Unset, None, str] = UNSET
    addresses: Union[Unset, None, List["CodatDataContractsDatasetsCommerceAddress"]] = UNSET
    note: Union[Unset, None, str] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        customer_name = self.customer_name
        email_address = self.email_address
        default_currency = self.default_currency
        phone = self.phone
        addresses: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            if self.addresses is None:
                addresses = None
            else:
                addresses = []
                for addresses_item_data in self.addresses:
                    addresses_item = addresses_item_data.to_dict()

                    addresses.append(addresses_item)

        note = self.note
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
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if default_currency is not UNSET:
            field_dict["defaultCurrency"] = default_currency
        if phone is not UNSET:
            field_dict["phone"] = phone
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if note is not UNSET:
            field_dict["note"] = note
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_commerce_address import CodatDataContractsDatasetsCommerceAddress

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        customer_name = d.pop("customerName", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        default_currency = d.pop("defaultCurrency", UNSET)

        phone = d.pop("phone", UNSET)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = CodatDataContractsDatasetsCommerceAddress.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        note = d.pop("note", UNSET)

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

        codat_data_contracts_datasets_commerce_customer = cls(
            id=id,
            customer_name=customer_name,
            email_address=email_address,
            default_currency=default_currency,
            phone=phone,
            addresses=addresses,
            note=note,
            created_date=created_date,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_commerce_customer
