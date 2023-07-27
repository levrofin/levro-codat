from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatAssessDataContractsLoansRecordRef")


@define
class CodatAssessDataContractsLoansRecordRef:
    """
    Attributes:
        id (Union[Unset, None, str]):
        data_connection_id (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    data_connection_id: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        data_connection_id = self.data_connection_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if data_connection_id is not UNSET:
            field_dict["dataConnectionId"] = data_connection_id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        data_connection_id = d.pop("dataConnectionId", UNSET)

        type = d.pop("type", UNSET)

        codat_assess_data_contracts_loans_record_ref = cls(
            id=id,
            data_connection_id=data_connection_id,
            type=type,
        )

        return codat_assess_data_contracts_loans_record_ref
