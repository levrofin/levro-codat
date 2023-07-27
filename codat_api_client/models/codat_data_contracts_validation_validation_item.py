from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsValidationValidationItem")


@define
class CodatDataContractsValidationValidationItem:
    """
    Attributes:
        item_id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        validator_name (Union[Unset, None, str]):
    """

    item_id: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    validator_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_id = self.item_id
        message = self.message
        validator_name = self.validator_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if message is not UNSET:
            field_dict["message"] = message
        if validator_name is not UNSET:
            field_dict["validatorName"] = validator_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_id = d.pop("itemId", UNSET)

        message = d.pop("message", UNSET)

        validator_name = d.pop("validatorName", UNSET)

        codat_data_contracts_validation_validation_item = cls(
            item_id=item_id,
            message=message,
            validator_name=validator_name,
        )

        return codat_data_contracts_validation_validation_item
