import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_supplier_status import CodatDataContractsDatasetsSupplierStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_address import CodatDataContractsDatasetsAddress
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
        CodatDataContractsDatasetsDataInterfacesSupplementalData,
    )
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata


T = TypeVar("T", bound="CodatDataContractsDatasetsSupplier")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsSupplier:
    """
    Attributes:
        status (CodatDataContractsDatasetsSupplierStatus):
        id (Union[Unset, None, str]):
        supplier_name (Union[Unset, None, str]):
        contact_name (Union[Unset, None, str]):
        email_address (Union[Unset, None, str]):
        phone (Union[Unset, None, str]):
        addresses (Union[Unset, None, List['CodatDataContractsDatasetsAddress']]):
        registration_number (Union[Unset, None, str]):
        tax_number (Union[Unset, None, str]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        default_currency (Union[Unset, None, str]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
        supplemental_data (Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]):
    """

    status: CodatDataContractsDatasetsSupplierStatus
    id: Union[Unset, None, str] = UNSET
    supplier_name: Union[Unset, None, str] = UNSET
    contact_name: Union[Unset, None, str] = UNSET
    email_address: Union[Unset, None, str] = UNSET
    phone: Union[Unset, None, str] = UNSET
    addresses: Union[Unset, None, List["CodatDataContractsDatasetsAddress"]] = UNSET
    registration_number: Union[Unset, None, str] = UNSET
    tax_number: Union[Unset, None, str] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    default_currency: Union[Unset, None, str] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET
    supplemental_data: Union[Unset, "CodatDataContractsDatasetsDataInterfacesSupplementalData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        id = self.id
        supplier_name = self.supplier_name
        contact_name = self.contact_name
        email_address = self.email_address
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

        registration_number = self.registration_number
        tax_number = self.tax_number
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        default_currency = self.default_currency
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
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if phone is not UNSET:
            field_dict["phone"] = phone
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if registration_number is not UNSET:
            field_dict["registrationNumber"] = registration_number
        if tax_number is not UNSET:
            field_dict["taxNumber"] = tax_number
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if default_currency is not UNSET:
            field_dict["defaultCurrency"] = default_currency
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if supplemental_data is not UNSET:
            field_dict["supplementalData"] = supplemental_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_address import CodatDataContractsDatasetsAddress
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
            CodatDataContractsDatasetsDataInterfacesSupplementalData,
        )
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata

        d = src_dict.copy()
        status = CodatDataContractsDatasetsSupplierStatus(d.pop("status"))

        id = d.pop("id", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        contact_name = d.pop("contactName", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        phone = d.pop("phone", UNSET)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = CodatDataContractsDatasetsAddress.from_dict(addresses_item_data)

            addresses.append(addresses_item)

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

        default_currency = d.pop("defaultCurrency", UNSET)

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

        codat_data_contracts_datasets_supplier = cls(
            status=status,
            id=id,
            supplier_name=supplier_name,
            contact_name=contact_name,
            email_address=email_address,
            phone=phone,
            addresses=addresses,
            registration_number=registration_number,
            tax_number=tax_number,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            default_currency=default_currency,
            metadata=metadata,
            supplemental_data=supplemental_data,
        )

        return codat_data_contracts_datasets_supplier
