import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_customer_status import CodatDataContractsDatasetsCustomerStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_address import CodatDataContractsDatasetsAddress
    from ..models.codat_data_contracts_datasets_phone import CodatDataContractsDatasetsPhone


T = TypeVar("T", bound="CodatDataContractsDatasetsContact")


@define
class CodatDataContractsDatasetsContact:
    """
    Attributes:
        status (CodatDataContractsDatasetsCustomerStatus):
        name (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        phone (Union[Unset, None, List['CodatDataContractsDatasetsPhone']]):
        address (Union[Unset, CodatDataContractsDatasetsAddress]):
        modified_date (Union[Unset, None, datetime.datetime]):
    """

    status: CodatDataContractsDatasetsCustomerStatus
    name: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    phone: Union[Unset, None, List["CodatDataContractsDatasetsPhone"]] = UNSET
    address: Union[Unset, "CodatDataContractsDatasetsAddress"] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        name = self.name
        email = self.email
        phone: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.phone, Unset):
            if self.phone is None:
                phone = None
            else:
                phone = []
                for phone_item_data in self.phone:
                    phone_item = phone_item_data.to_dict()

                    phone.append(phone_item)

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "status": status,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if address is not UNSET:
            field_dict["address"] = address
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_address import CodatDataContractsDatasetsAddress
        from ..models.codat_data_contracts_datasets_phone import CodatDataContractsDatasetsPhone

        d = src_dict.copy()
        status = CodatDataContractsDatasetsCustomerStatus(d.pop("status"))

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        phone = []
        _phone = d.pop("phone", UNSET)
        for phone_item_data in _phone or []:
            phone_item = CodatDataContractsDatasetsPhone.from_dict(phone_item_data)

            phone.append(phone_item)

        _address = d.pop("address", UNSET)
        address: Union[Unset, CodatDataContractsDatasetsAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = CodatDataContractsDatasetsAddress.from_dict(_address)

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: Union[Unset, None, datetime.datetime]
        if _modified_date is None:
            modified_date = None
        elif isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        codat_data_contracts_datasets_contact = cls(
            status=status,
            name=name,
            email=email,
            phone=phone,
            address=address,
            modified_date=modified_date,
        )

        return codat_data_contracts_datasets_contact
