from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..models.codat_data_contracts_datasets_commerce_transaction_ref_type import (
    CodatDataContractsDatasetsCommerceTransactionRefType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceTransactionSourceRef")


@define
class CodatDataContractsDatasetsCommerceTransactionSourceRef:
    """
    Attributes:
        id (Union[Unset, None, str]):
        type (Union[Unset, CodatDataContractsDatasetsCommerceTransactionRefType]):
    """

    id: Union[Unset, None, str] = UNSET
    type: Union[Unset, CodatDataContractsDatasetsCommerceTransactionRefType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CodatDataContractsDatasetsCommerceTransactionRefType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodatDataContractsDatasetsCommerceTransactionRefType(_type)

        codat_data_contracts_datasets_commerce_transaction_source_ref = cls(
            id=id,
            type=type,
        )

        return codat_data_contracts_datasets_commerce_transaction_source_ref
