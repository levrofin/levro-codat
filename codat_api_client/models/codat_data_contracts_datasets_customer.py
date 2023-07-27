import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_customer_status import CodatDataContractsDatasetsCustomerStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_address import CodatDataContractsDatasetsAddress
    from ..models.codat_data_contracts_datasets_contact import CodatDataContractsDatasetsContact
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
        CodatDataContractsDatasetsDataInterfacesSupplementalData,
    )
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata


T = TypeVar("T", bound="CodatDataContractsDatasetsCustomer")


@define
class CodatDataContractsDatasetsCustomer:
    """
    Attributes:
        status (CodatDataContractsDatasetsCustomerStatus):
        id (Union[Unset, None, str]):
        customer_name (Union[Unset, None, str]):
        contact_name (Union[Unset, None, str]):
        email_address (Union[Unset, None, str]):
        default_currency (Union[Unset, None, str]):
        phone (Union[Unset, None, str]):
        addresses (Union[Unset, None, List['CodatDataContractsDatasetsAddress']]):
        contacts (Union[Unset, None, List['CodatDataContractsDatasetsContact']]):
        registration_number (Union[Unset, None, str]):
        tax_number (Union[Unset, None, str]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
        supplemental_data (Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]):
    """

    status: CodatDataContractsDatasetsCustomerStatus
    id: Union[Unset, None, str] = UNSET
    customer_name: Union[Unset, None, str] = UNSET
    contact_name: Union[Unset, None, str] = UNSET
    email_address: Union[Unset, None, str] = UNSET
    default_currency: Union[Unset, None, str] = UNSET
    phone: Union[Unset, None, str] = UNSET
    addresses: Union[Unset, None, List["CodatDataContractsDatasetsAddress"]] = UNSET
    contacts: Union[Unset, None, List["CodatDataContractsDatasetsContact"]] = UNSET
    registration_number: Union[Unset, None, str] = UNSET
    tax_number: Union[Unset, None, str] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET
    supplemental_data: Union[Unset, "CodatDataContractsDatasetsDataInterfacesSupplementalData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        id = self.id
        customer_name = self.customer_name
        contact_name = self.contact_name
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

        contacts: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            if self.contacts is None:
                contacts = None
            else:
                contacts = []
                for contacts_item_data in self.contacts:
                    contacts_item = contacts_item_data.to_dict()

                    contacts.append(contacts_item)

        registration_number = self.registration_number
        tax_number = self.tax_number
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        supplemental_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplemental_data, Unset):
            supplemental_data = self.supplemental_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "status": status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if default_currency is not UNSET:
            field_dict["defaultCurrency"] = default_currency
        if phone is not UNSET:
            field_dict["phone"] = phone
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if registration_number is not UNSET:
            field_dict["registrationNumber"] = registration_number
        if tax_number is not UNSET:
            field_dict["taxNumber"] = tax_number
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if supplemental_data is not UNSET:
            field_dict["supplementalData"] = supplemental_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_address import CodatDataContractsDatasetsAddress
        from ..models.codat_data_contracts_datasets_contact import CodatDataContractsDatasetsContact
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
            CodatDataContractsDatasetsDataInterfacesSupplementalData,
        )
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata

        d = src_dict.copy()
        status = CodatDataContractsDatasetsCustomerStatus(d.pop("status"))

        id = d.pop("id", UNSET)

        customer_name = d.pop("customerName", UNSET)

        contact_name = d.pop("contactName", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        default_currency = d.pop("defaultCurrency", UNSET)

        phone = d.pop("phone", UNSET)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = CodatDataContractsDatasetsAddress.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = CodatDataContractsDatasetsContact.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        registration_number = d.pop("registrationNumber", UNSET)

        tax_number = d.pop("taxNumber", UNSET)

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

        _supplemental_data = d.pop("supplementalData", UNSET)
        supplemental_data: Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]
        if isinstance(_supplemental_data, Unset):
            supplemental_data = UNSET
        else:
            supplemental_data = CodatDataContractsDatasetsDataInterfacesSupplementalData.from_dict(_supplemental_data)

        codat_data_contracts_datasets_customer = cls(
            status=status,
            id=id,
            customer_name=customer_name,
            contact_name=contact_name,
            email_address=email_address,
            default_currency=default_currency,
            phone=phone,
            addresses=addresses,
            contacts=contacts,
            registration_number=registration_number,
            tax_number=tax_number,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            metadata=metadata,
            supplemental_data=supplemental_data,
        )

        return codat_data_contracts_datasets_customer
