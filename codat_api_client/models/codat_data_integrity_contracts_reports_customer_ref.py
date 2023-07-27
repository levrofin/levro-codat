from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataIntegrityContractsReportsCustomerRef")


@define
class CodatDataIntegrityContractsReportsCustomerRef:
    """
    Attributes:
        id (Union[Unset, None, str]):
        customer_name (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    customer_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        customer_name = self.customer_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        customer_name = d.pop("customerName", UNSET)

        codat_data_integrity_contracts_reports_customer_ref = cls(
            id=id,
            customer_name=customer_name,
        )

        return codat_data_integrity_contracts_reports_customer_ref
