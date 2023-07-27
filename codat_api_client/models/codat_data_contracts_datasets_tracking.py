from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef


T = TypeVar("T", bound="CodatDataContractsDatasetsTracking")


@define
class CodatDataContractsDatasetsTracking:
    """
    Attributes:
        record_refs (Union[Unset, None, List['CodatDataContractsDatasetsRecordRef']]):
    """

    record_refs: Union[Unset, None, List["CodatDataContractsDatasetsRecordRef"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        record_refs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.record_refs, Unset):
            if self.record_refs is None:
                record_refs = None
            else:
                record_refs = []
                for record_refs_item_data in self.record_refs:
                    record_refs_item = record_refs_item_data.to_dict()

                    record_refs.append(record_refs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if record_refs is not UNSET:
            field_dict["recordRefs"] = record_refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef

        d = src_dict.copy()
        record_refs = []
        _record_refs = d.pop("recordRefs", UNSET)
        for record_refs_item_data in _record_refs or []:
            record_refs_item = CodatDataContractsDatasetsRecordRef.from_dict(record_refs_item_data)

            record_refs.append(record_refs_item)

        codat_data_contracts_datasets_tracking = cls(
            record_refs=record_refs,
        )

        return codat_data_contracts_datasets_tracking
