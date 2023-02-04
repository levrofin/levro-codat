import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_item_status import CodatDataContractsDatasetsItemStatus
from ..models.codat_data_contracts_datasets_item_type import CodatDataContractsDatasetsItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_bill_item import CodatDataContractsDatasetsBillItem
    from ..models.codat_data_contracts_datasets_invoice_item import CodatDataContractsDatasetsInvoiceItem
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata


T = TypeVar("T", bound="CodatDataContractsDatasetsItem")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsItem:
    """
    Attributes:
        item_status (CodatDataContractsDatasetsItemStatus):
        type (CodatDataContractsDatasetsItemType):
        is_bill_item (bool):
        is_invoice_item (bool):
        id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        code (Union[Unset, None, str]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        bill_item (Union[Unset, CodatDataContractsDatasetsBillItem]):
        invoice_item (Union[Unset, CodatDataContractsDatasetsInvoiceItem]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
    """

    item_status: CodatDataContractsDatasetsItemStatus
    type: CodatDataContractsDatasetsItemType
    is_bill_item: bool
    is_invoice_item: bool
    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    code: Union[Unset, None, str] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    bill_item: Union[Unset, "CodatDataContractsDatasetsBillItem"] = UNSET
    invoice_item: Union[Unset, "CodatDataContractsDatasetsInvoiceItem"] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_status = self.item_status.value

        type = self.type.value

        is_bill_item = self.is_bill_item
        is_invoice_item = self.is_invoice_item
        id = self.id
        name = self.name
        code = self.code
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        bill_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bill_item, Unset):
            bill_item = self.bill_item.to_dict()

        invoice_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_item, Unset):
            invoice_item = self.invoice_item.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "itemStatus": item_status,
                "type": type,
                "isBillItem": is_bill_item,
                "isInvoiceItem": is_invoice_item,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if bill_item is not UNSET:
            field_dict["billItem"] = bill_item
        if invoice_item is not UNSET:
            field_dict["invoiceItem"] = invoice_item
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_bill_item import CodatDataContractsDatasetsBillItem
        from ..models.codat_data_contracts_datasets_invoice_item import CodatDataContractsDatasetsInvoiceItem
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata

        d = src_dict.copy()
        item_status = CodatDataContractsDatasetsItemStatus(d.pop("itemStatus"))

        type = CodatDataContractsDatasetsItemType(d.pop("type"))

        is_bill_item = d.pop("isBillItem")

        is_invoice_item = d.pop("isInvoiceItem")

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: Union[Unset, None, datetime.datetime]
        if _modified_date is None:
            modified_date = None
        elif isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, None, datetime.datetime]
        if _source_modified_date is None:
            source_modified_date = None
        elif isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        _bill_item = d.pop("billItem", UNSET)
        bill_item: Union[Unset, CodatDataContractsDatasetsBillItem]
        if isinstance(_bill_item, Unset):
            bill_item = UNSET
        else:
            bill_item = CodatDataContractsDatasetsBillItem.from_dict(_bill_item)

        _invoice_item = d.pop("invoiceItem", UNSET)
        invoice_item: Union[Unset, CodatDataContractsDatasetsInvoiceItem]
        if isinstance(_invoice_item, Unset):
            invoice_item = UNSET
        else:
            invoice_item = CodatDataContractsDatasetsInvoiceItem.from_dict(_invoice_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CodatDataContractsDatasetsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CodatDataContractsDatasetsMetadata.from_dict(_metadata)

        codat_data_contracts_datasets_item = cls(
            item_status=item_status,
            type=type,
            is_bill_item=is_bill_item,
            is_invoice_item=is_invoice_item,
            id=id,
            name=name,
            code=code,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            bill_item=bill_item,
            invoice_item=invoice_item,
            metadata=metadata,
        )

        return codat_data_contracts_datasets_item
