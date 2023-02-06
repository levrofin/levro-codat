import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_address import CodatDataContractsDatasetsCommerceAddress


T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceLocation")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCommerceLocation:
    """
    Attributes:
        id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        address (Union[Unset, CodatDataContractsDatasetsCommerceAddress]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    address: Union[Unset, "CodatDataContractsDatasetsCommerceAddress"] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

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
        if address is not UNSET:
            field_dict["address"] = address
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

        name = d.pop("name", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, CodatDataContractsDatasetsCommerceAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = CodatDataContractsDatasetsCommerceAddress.from_dict(_address)

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

        codat_data_contracts_datasets_commerce_location = cls(
            id=id,
            name=name,
            address=address,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_commerce_location
