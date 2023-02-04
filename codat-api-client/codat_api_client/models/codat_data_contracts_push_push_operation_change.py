from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.codat_data_contracts_push_push_change_type import CodatDataContractsPushPushChangeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_push_push_operation_record_ref import (
        CodatDataContractsPushPushOperationRecordRef,
    )


T = TypeVar("T", bound="CodatDataContractsPushPushOperationChange")


@attr.s(auto_attribs=True)
class CodatDataContractsPushPushOperationChange:
    """
    Attributes:
        type (Union[Unset, CodatDataContractsPushPushChangeType]):
        record_ref (Union[Unset, CodatDataContractsPushPushOperationRecordRef]):
        attachment_id (Union[Unset, None, str]):
    """

    type: Union[Unset, CodatDataContractsPushPushChangeType] = UNSET
    record_ref: Union[Unset, "CodatDataContractsPushPushOperationRecordRef"] = UNSET
    attachment_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        record_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_ref, Unset):
            record_ref = self.record_ref.to_dict()

        attachment_id = self.attachment_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if record_ref is not UNSET:
            field_dict["recordRef"] = record_ref
        if attachment_id is not UNSET:
            field_dict["attachmentId"] = attachment_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_push_push_operation_record_ref import (
            CodatDataContractsPushPushOperationRecordRef,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, CodatDataContractsPushPushChangeType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodatDataContractsPushPushChangeType(_type)

        _record_ref = d.pop("recordRef", UNSET)
        record_ref: Union[Unset, CodatDataContractsPushPushOperationRecordRef]
        if isinstance(_record_ref, Unset):
            record_ref = UNSET
        else:
            record_ref = CodatDataContractsPushPushOperationRecordRef.from_dict(_record_ref)

        attachment_id = d.pop("attachmentId", UNSET)

        codat_data_contracts_push_push_operation_change = cls(
            type=type,
            record_ref=record_ref,
            attachment_id=attachment_id,
        )

        return codat_data_contracts_push_push_operation_change
