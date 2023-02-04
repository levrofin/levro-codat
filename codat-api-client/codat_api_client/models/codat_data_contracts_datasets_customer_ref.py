from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsCustomerRef")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCustomerRef:
    """
    Attributes:
        id (str):
        company_name (Union[Unset, None, str]):
    """

    id: str
    company_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        company_name = self.company_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if company_name is not UNSET:
            field_dict["companyName"] = company_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        company_name = d.pop("companyName", UNSET)

        codat_data_contracts_datasets_customer_ref = cls(
            id=id,
            company_name=company_name,
        )

        return codat_data_contracts_datasets_customer_ref
