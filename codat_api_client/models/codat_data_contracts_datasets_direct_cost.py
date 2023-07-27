import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_contact_ref import CodatDataContractsDatasetsContactRef
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
        CodatDataContractsDatasetsDataInterfacesSupplementalData,
    )
    from ..models.codat_data_contracts_datasets_detailed_payment_allocation import (
        CodatDataContractsDatasetsDetailedPaymentAllocation,
    )
    from ..models.codat_data_contracts_datasets_direct_cost_line_item import (
        CodatDataContractsDatasetsDirectCostLineItem,
    )
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata


T = TypeVar("T", bound="CodatDataContractsDatasetsDirectCost")


@define
class CodatDataContractsDatasetsDirectCost:
    """
    Attributes:
        issue_date (datetime.datetime):
        currency (str):
        line_items (List['CodatDataContractsDatasetsDirectCostLineItem']):
        payment_allocations (List['CodatDataContractsDatasetsDetailedPaymentAllocation']):
        sub_total (float):
        tax_amount (float):
        total_amount (float):
        id (Union[Unset, None, str]):
        reference (Union[Unset, None, str]):
        note (Union[Unset, None, str]):
        contact_ref (Union[Unset, CodatDataContractsDatasetsContactRef]):
        currency_rate (Union[Unset, None, float]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
        supplemental_data (Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]):
    """

    issue_date: datetime.datetime
    currency: str
    line_items: List["CodatDataContractsDatasetsDirectCostLineItem"]
    payment_allocations: List["CodatDataContractsDatasetsDetailedPaymentAllocation"]
    sub_total: float
    tax_amount: float
    total_amount: float
    id: Union[Unset, None, str] = UNSET
    reference: Union[Unset, None, str] = UNSET
    note: Union[Unset, None, str] = UNSET
    contact_ref: Union[Unset, "CodatDataContractsDatasetsContactRef"] = UNSET
    currency_rate: Union[Unset, None, float] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET
    supplemental_data: Union[Unset, "CodatDataContractsDatasetsDataInterfacesSupplementalData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        issue_date = self.issue_date.isoformat()

        currency = self.currency
        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()

            line_items.append(line_items_item)

        payment_allocations = []
        for payment_allocations_item_data in self.payment_allocations:
            payment_allocations_item = payment_allocations_item_data.to_dict()

            payment_allocations.append(payment_allocations_item)

        sub_total = self.sub_total
        tax_amount = self.tax_amount
        total_amount = self.total_amount
        id = self.id
        reference = self.reference
        note = self.note
        contact_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact_ref, Unset):
            contact_ref = self.contact_ref.to_dict()

        currency_rate = self.currency_rate
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        supplemental_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplemental_data, Unset):
            supplemental_data = self.supplemental_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "issueDate": issue_date,
                "currency": currency,
                "lineItems": line_items,
                "paymentAllocations": payment_allocations,
                "subTotal": sub_total,
                "taxAmount": tax_amount,
                "totalAmount": total_amount,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if note is not UNSET:
            field_dict["note"] = note
        if contact_ref is not UNSET:
            field_dict["contactRef"] = contact_ref
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if supplemental_data is not UNSET:
            field_dict["supplementalData"] = supplemental_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_contact_ref import CodatDataContractsDatasetsContactRef
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
            CodatDataContractsDatasetsDataInterfacesSupplementalData,
        )
        from ..models.codat_data_contracts_datasets_detailed_payment_allocation import (
            CodatDataContractsDatasetsDetailedPaymentAllocation,
        )
        from ..models.codat_data_contracts_datasets_direct_cost_line_item import (
            CodatDataContractsDatasetsDirectCostLineItem,
        )
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata

        d = src_dict.copy()
        issue_date = isoparse(d.pop("issueDate"))

        currency = d.pop("currency")

        line_items = []
        _line_items = d.pop("lineItems")
        for line_items_item_data in _line_items:
            line_items_item = CodatDataContractsDatasetsDirectCostLineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        payment_allocations = []
        _payment_allocations = d.pop("paymentAllocations")
        for payment_allocations_item_data in _payment_allocations:
            payment_allocations_item = CodatDataContractsDatasetsDetailedPaymentAllocation.from_dict(
                payment_allocations_item_data
            )

            payment_allocations.append(payment_allocations_item)

        sub_total = d.pop("subTotal")

        tax_amount = d.pop("taxAmount")

        total_amount = d.pop("totalAmount")

        id = d.pop("id", UNSET)

        reference = d.pop("reference", UNSET)

        note = d.pop("note", UNSET)

        _contact_ref = d.pop("contactRef", UNSET)
        contact_ref: Union[Unset, CodatDataContractsDatasetsContactRef]
        if isinstance(_contact_ref, Unset):
            contact_ref = UNSET
        else:
            contact_ref = CodatDataContractsDatasetsContactRef.from_dict(_contact_ref)

        currency_rate = d.pop("currencyRate", UNSET)

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

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CodatDataContractsDatasetsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CodatDataContractsDatasetsMetadata.from_dict(_metadata)

        _supplemental_data = d.pop("supplementalData", UNSET)
        supplemental_data: Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]
        if isinstance(_supplemental_data, Unset):
            supplemental_data = UNSET
        else:
            supplemental_data = CodatDataContractsDatasetsDataInterfacesSupplementalData.from_dict(_supplemental_data)

        codat_data_contracts_datasets_direct_cost = cls(
            issue_date=issue_date,
            currency=currency,
            line_items=line_items,
            payment_allocations=payment_allocations,
            sub_total=sub_total,
            tax_amount=tax_amount,
            total_amount=total_amount,
            id=id,
            reference=reference,
            note=note,
            contact_ref=contact_ref,
            currency_rate=currency_rate,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            metadata=metadata,
            supplemental_data=supplemental_data,
        )

        return codat_data_contracts_datasets_direct_cost
