from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef


T = TypeVar("T", bound="CodatDataContractsDatasetsInvoiceableTracking")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsInvoiceableTracking:
    """
    Attributes:
        record_refs (List['CodatDataContractsDatasetsRecordRef']):
        invoice_to (Union[Unset, CodatDataContractsDatasetsRecordRef]):
    """

    record_refs: List["CodatDataContractsDatasetsRecordRef"]
    invoice_to: Union[Unset, "CodatDataContractsDatasetsRecordRef"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        record_refs = []
        for record_refs_item_data in self.record_refs:
            record_refs_item = record_refs_item_data.to_dict()

            record_refs.append(record_refs_item)

        invoice_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_to, Unset):
            invoice_to = self.invoice_to.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "recordRefs": record_refs,
            }
        )
        if invoice_to is not UNSET:
            field_dict["invoiceTo"] = invoice_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef

        d = src_dict.copy()
        record_refs = []
        _record_refs = d.pop("recordRefs")
        for record_refs_item_data in _record_refs:
            record_refs_item = CodatDataContractsDatasetsRecordRef.from_dict(record_refs_item_data)

            record_refs.append(record_refs_item)

        _invoice_to = d.pop("invoiceTo", UNSET)
        invoice_to: Union[Unset, CodatDataContractsDatasetsRecordRef]
        if isinstance(_invoice_to, Unset):
            invoice_to = UNSET
        else:
            invoice_to = CodatDataContractsDatasetsRecordRef.from_dict(_invoice_to)

        codat_data_contracts_datasets_invoiceable_tracking = cls(
            record_refs=record_refs,
            invoice_to=invoice_to,
        )

        return codat_data_contracts_datasets_invoiceable_tracking
