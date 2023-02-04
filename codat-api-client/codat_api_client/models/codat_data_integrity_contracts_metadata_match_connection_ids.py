from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataIntegrityContractsMetadataMatchConnectionIds")


@attr.s(auto_attribs=True)
class CodatDataIntegrityContractsMetadataMatchConnectionIds:
    """
    Attributes:
        source (Union[Unset, None, List[str]]):
        target (Union[Unset, None, List[str]]):
    """

    source: Union[Unset, None, List[str]] = UNSET
    target: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        source: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.source, Unset):
            if self.source is None:
                source = None
            else:
                source = self.source

        target: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.target, Unset):
            if self.target is None:
                target = None
            else:
                target = self.target

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source = cast(List[str], d.pop("source", UNSET))

        target = cast(List[str], d.pop("target", UNSET))

        codat_data_integrity_contracts_metadata_match_connection_ids = cls(
            source=source,
            target=target,
        )

        return codat_data_integrity_contracts_metadata_match_connection_ids
