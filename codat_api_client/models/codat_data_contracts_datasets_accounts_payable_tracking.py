from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..models.codat_data_contracts_datasets_accounts_payable_is_billed_to_type import (
    CodatDataContractsDatasetsAccountsPayableIsBilledToType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_customer_ref import CodatDataContractsDatasetsCustomerRef
    from ..models.codat_data_contracts_datasets_project_ref import CodatDataContractsDatasetsProjectRef
    from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef
    from ..models.codat_data_contracts_datasets_tracking_category_ref import (
        CodatDataContractsDatasetsTrackingCategoryRef,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsAccountsPayableTracking")


@define
class CodatDataContractsDatasetsAccountsPayableTracking:
    """
    Attributes:
        category_refs (List['CodatDataContractsDatasetsTrackingCategoryRef']):
        record_refs (List['CodatDataContractsDatasetsRecordRef']):
        is_billed_to (CodatDataContractsDatasetsAccountsPayableIsBilledToType):
        is_rebilled_to (CodatDataContractsDatasetsAccountsPayableIsBilledToType):
        customer_ref (Union[Unset, CodatDataContractsDatasetsCustomerRef]):
        invoice_to (Union[Unset, CodatDataContractsDatasetsRecordRef]):
        project_ref (Union[Unset, CodatDataContractsDatasetsProjectRef]):
    """

    category_refs: List["CodatDataContractsDatasetsTrackingCategoryRef"]
    record_refs: List["CodatDataContractsDatasetsRecordRef"]
    is_billed_to: CodatDataContractsDatasetsAccountsPayableIsBilledToType
    is_rebilled_to: CodatDataContractsDatasetsAccountsPayableIsBilledToType
    customer_ref: Union[Unset, "CodatDataContractsDatasetsCustomerRef"] = UNSET
    invoice_to: Union[Unset, "CodatDataContractsDatasetsRecordRef"] = UNSET
    project_ref: Union[Unset, "CodatDataContractsDatasetsProjectRef"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        category_refs = []
        for category_refs_item_data in self.category_refs:
            category_refs_item = category_refs_item_data.to_dict()

            category_refs.append(category_refs_item)

        record_refs = []
        for record_refs_item_data in self.record_refs:
            record_refs_item = record_refs_item_data.to_dict()

            record_refs.append(record_refs_item)

        is_billed_to = self.is_billed_to.value

        is_rebilled_to = self.is_rebilled_to.value

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        invoice_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_to, Unset):
            invoice_to = self.invoice_to.to_dict()

        project_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_ref, Unset):
            project_ref = self.project_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "categoryRefs": category_refs,
                "recordRefs": record_refs,
                "isBilledTo": is_billed_to,
                "isRebilledTo": is_rebilled_to,
            }
        )
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if invoice_to is not UNSET:
            field_dict["invoiceTo"] = invoice_to
        if project_ref is not UNSET:
            field_dict["projectRef"] = project_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_customer_ref import CodatDataContractsDatasetsCustomerRef
        from ..models.codat_data_contracts_datasets_project_ref import CodatDataContractsDatasetsProjectRef
        from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef
        from ..models.codat_data_contracts_datasets_tracking_category_ref import (
            CodatDataContractsDatasetsTrackingCategoryRef,
        )

        d = src_dict.copy()
        category_refs = []
        _category_refs = d.pop("categoryRefs")
        for category_refs_item_data in _category_refs:
            category_refs_item = CodatDataContractsDatasetsTrackingCategoryRef.from_dict(category_refs_item_data)

            category_refs.append(category_refs_item)

        record_refs = []
        _record_refs = d.pop("recordRefs")
        for record_refs_item_data in _record_refs:
            record_refs_item = CodatDataContractsDatasetsRecordRef.from_dict(record_refs_item_data)

            record_refs.append(record_refs_item)

        is_billed_to = CodatDataContractsDatasetsAccountsPayableIsBilledToType(d.pop("isBilledTo"))

        is_rebilled_to = CodatDataContractsDatasetsAccountsPayableIsBilledToType(d.pop("isRebilledTo"))

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CodatDataContractsDatasetsCustomerRef]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CodatDataContractsDatasetsCustomerRef.from_dict(_customer_ref)

        _invoice_to = d.pop("invoiceTo", UNSET)
        invoice_to: Union[Unset, CodatDataContractsDatasetsRecordRef]
        if isinstance(_invoice_to, Unset):
            invoice_to = UNSET
        else:
            invoice_to = CodatDataContractsDatasetsRecordRef.from_dict(_invoice_to)

        _project_ref = d.pop("projectRef", UNSET)
        project_ref: Union[Unset, CodatDataContractsDatasetsProjectRef]
        if isinstance(_project_ref, Unset):
            project_ref = UNSET
        else:
            project_ref = CodatDataContractsDatasetsProjectRef.from_dict(_project_ref)

        codat_data_contracts_datasets_accounts_payable_tracking = cls(
            category_refs=category_refs,
            record_refs=record_refs,
            is_billed_to=is_billed_to,
            is_rebilled_to=is_rebilled_to,
            customer_ref=customer_ref,
            invoice_to=invoice_to,
            project_ref=project_ref,
        )

        return codat_data_contracts_datasets_accounts_payable_tracking
