from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_integrity_contracts_metadata_match_metadata import (
        CodatDataIntegrityContractsMetadataMatchMetadata,
    )


T = TypeVar("T", bound="CodatDataIntegrityContractsMetadataMatchMetadataResponse")


@define
class CodatDataIntegrityContractsMetadataMatchMetadataResponse:
    """
    Attributes:
        metadata (Union[Unset, None, List['CodatDataIntegrityContractsMetadataMatchMetadata']]):
    """

    metadata: Union[Unset, None, List["CodatDataIntegrityContractsMetadataMatchMetadata"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        metadata: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata, Unset):
            if self.metadata is None:
                metadata = None
            else:
                metadata = []
                for metadata_item_data in self.metadata:
                    metadata_item = metadata_item_data.to_dict()

                    metadata.append(metadata_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_integrity_contracts_metadata_match_metadata import (
            CodatDataIntegrityContractsMetadataMatchMetadata,
        )

        d = src_dict.copy()
        metadata = []
        _metadata = d.pop("metadata", UNSET)
        for metadata_item_data in _metadata or []:
            metadata_item = CodatDataIntegrityContractsMetadataMatchMetadata.from_dict(metadata_item_data)

            metadata.append(metadata_item)

        codat_data_integrity_contracts_metadata_match_metadata_response = cls(
            metadata=metadata,
        )

        return codat_data_integrity_contracts_metadata_match_metadata_response
