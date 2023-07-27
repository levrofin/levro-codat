from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsContactRef")


@define
class CodatDataContractsDatasetsContactRef:
    """
    Attributes:
        id (str):
        data_type (Union[Unset, None, str]):
    """

    id: str
    data_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        data_type = self.data_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if data_type is not UNSET:
            field_dict["dataType"] = data_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        data_type = d.pop("dataType", UNSET)

        codat_data_contracts_datasets_contact_ref = cls(
            id=id,
            data_type=data_type,
        )

        return codat_data_contracts_datasets_contact_ref
