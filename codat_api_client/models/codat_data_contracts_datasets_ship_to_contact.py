from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsShipToContact")


@define
class CodatDataContractsDatasetsShipToContact:
    """
    Attributes:
        name (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        phone (Union[Unset, None, str]):
    """

    name: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    phone: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        email = self.email
        phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        codat_data_contracts_datasets_ship_to_contact = cls(
            name=name,
            email=email,
            phone=phone,
        )

        return codat_data_contracts_datasets_ship_to_contact
