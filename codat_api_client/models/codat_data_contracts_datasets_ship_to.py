from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_address import CodatDataContractsDatasetsAddress
    from ..models.codat_data_contracts_datasets_ship_to_contact import CodatDataContractsDatasetsShipToContact


T = TypeVar("T", bound="CodatDataContractsDatasetsShipTo")


@define
class CodatDataContractsDatasetsShipTo:
    """
    Attributes:
        contact (Union[Unset, CodatDataContractsDatasetsShipToContact]):
        address (Union[Unset, CodatDataContractsDatasetsAddress]):
    """

    contact: Union[Unset, "CodatDataContractsDatasetsShipToContact"] = UNSET
    address: Union[Unset, "CodatDataContractsDatasetsAddress"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if contact is not UNSET:
            field_dict["contact"] = contact
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_address import CodatDataContractsDatasetsAddress
        from ..models.codat_data_contracts_datasets_ship_to_contact import CodatDataContractsDatasetsShipToContact

        d = src_dict.copy()
        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, CodatDataContractsDatasetsShipToContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = CodatDataContractsDatasetsShipToContact.from_dict(_contact)

        _address = d.pop("address", UNSET)
        address: Union[Unset, CodatDataContractsDatasetsAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = CodatDataContractsDatasetsAddress.from_dict(_address)

        codat_data_contracts_datasets_ship_to = cls(
            contact=contact,
            address=address,
        )

        return codat_data_contracts_datasets_ship_to
