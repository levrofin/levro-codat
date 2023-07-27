from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsPushPushOperationRecordRef")


@define
class CodatDataContractsPushPushOperationRecordRef:
    """
    Attributes:
        id (Union[Unset, None, str]):
        data_type (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    data_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        data_type = self.data_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if data_type is not UNSET:
            field_dict["dataType"] = data_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        data_type = d.pop("dataType", UNSET)

        codat_data_contracts_push_push_operation_record_ref = cls(
            id=id,
            data_type=data_type,
        )

        return codat_data_contracts_push_push_operation_record_ref
