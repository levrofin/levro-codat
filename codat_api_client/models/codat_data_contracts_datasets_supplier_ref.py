from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsSupplierRef")


@define
class CodatDataContractsDatasetsSupplierRef:
    """
    Attributes:
        id (str):
        supplier_name (Union[Unset, None, str]):
    """

    id: str
    supplier_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        supplier_name = self.supplier_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        supplier_name = d.pop("supplierName", UNSET)

        codat_data_contracts_datasets_supplier_ref = cls(
            id=id,
            supplier_name=supplier_name,
        )

        return codat_data_contracts_datasets_supplier_ref
