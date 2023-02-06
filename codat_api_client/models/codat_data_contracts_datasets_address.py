from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.codat_data_contracts_datasets_address_type import CodatDataContractsDatasetsAddressType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsAddress")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsAddress:
    """
    Attributes:
        type (CodatDataContractsDatasetsAddressType):
        line1 (Union[Unset, None, str]):
        line2 (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        region (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        postal_code (Union[Unset, None, str]):
    """

    type: CodatDataContractsDatasetsAddressType
    line1: Union[Unset, None, str] = UNSET
    line2: Union[Unset, None, str] = UNSET
    city: Union[Unset, None, str] = UNSET
    region: Union[Unset, None, str] = UNSET
    country: Union[Unset, None, str] = UNSET
    postal_code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        line1 = self.line1
        line2 = self.line2
        city = self.city
        region = self.region
        country = self.country
        postal_code = self.postal_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if line1 is not UNSET:
            field_dict["line1"] = line1
        if line2 is not UNSET:
            field_dict["line2"] = line2
        if city is not UNSET:
            field_dict["city"] = city
        if region is not UNSET:
            field_dict["region"] = region
        if country is not UNSET:
            field_dict["country"] = country
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = CodatDataContractsDatasetsAddressType(d.pop("type"))

        line1 = d.pop("line1", UNSET)

        line2 = d.pop("line2", UNSET)

        city = d.pop("city", UNSET)

        region = d.pop("region", UNSET)

        country = d.pop("country", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        codat_data_contracts_datasets_address = cls(
            type=type,
            line1=line1,
            line2=line2,
            city=city,
            region=region,
            country=country,
            postal_code=postal_code,
        )

        return codat_data_contracts_datasets_address
