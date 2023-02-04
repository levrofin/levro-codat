from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsMetadata")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsMetadata:
    """
    Attributes:
        is_deleted (Union[Unset, None, bool]):
    """

    is_deleted: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_deleted = self.is_deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_deleted = d.pop("isDeleted", UNSET)

        codat_data_contracts_datasets_metadata = cls(
            is_deleted=is_deleted,
        )

        return codat_data_contracts_datasets_metadata
