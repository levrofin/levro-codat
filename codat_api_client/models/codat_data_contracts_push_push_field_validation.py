from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsPushPushFieldValidation")


@define
class CodatDataContractsPushPushFieldValidation:
    """
    Attributes:
        field (str):
        details (str):
        ref (Union[Unset, None, str]):
    """

    field: str
    details: str
    ref: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field = self.field
        details = self.details
        ref = self.ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "field": field,
                "details": details,
            }
        )
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field = d.pop("field")

        details = d.pop("details")

        ref = d.pop("ref", UNSET)

        codat_data_contracts_push_push_field_validation = cls(
            field=field,
            details=details,
            ref=ref,
        )

        return codat_data_contracts_push_push_field_validation
