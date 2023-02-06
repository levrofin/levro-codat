from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_attachments_dataset_attachment import (
        CodatDataContractsDatasetsAttachmentsDatasetAttachment,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsAttachmentsDataset")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsAttachmentsDataset:
    """
    Attributes:
        attachments (Union[Unset, None, List['CodatDataContractsDatasetsAttachmentsDatasetAttachment']]):
    """

    attachments: Union[Unset, None, List["CodatDataContractsDatasetsAttachmentsDatasetAttachment"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        attachments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            if self.attachments is None:
                attachments = None
            else:
                attachments = []
                for attachments_item_data in self.attachments:
                    attachments_item = attachments_item_data.to_dict()

                    attachments.append(attachments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_attachments_dataset_attachment import (
            CodatDataContractsDatasetsAttachmentsDatasetAttachment,
        )

        d = src_dict.copy()
        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = CodatDataContractsDatasetsAttachmentsDatasetAttachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        codat_data_contracts_datasets_attachments_dataset = cls(
            attachments=attachments,
        )

        return codat_data_contracts_datasets_attachments_dataset
