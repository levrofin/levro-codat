from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..models.codat_data_contracts_datasets_accounts_receivable_is_billed_to_type import (
    CodatDataContractsDatasetsAccountsReceivableIsBilledToType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_customer_ref import CodatDataContractsDatasetsCustomerRef
    from ..models.codat_data_contracts_datasets_project_ref import CodatDataContractsDatasetsProjectRef
    from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef
    from ..models.codat_data_contracts_datasets_tracking_category_ref import (
        CodatDataContractsDatasetsTrackingCategoryRef,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsAccountsReceivableTracking")


@define
class CodatDataContractsDatasetsAccountsReceivableTracking:
    """
    Attributes:
        category_refs (List['CodatDataContractsDatasetsTrackingCategoryRef']):
        is_billed_to (CodatDataContractsDatasetsAccountsReceivableIsBilledToType):
        is_rebilled_to (CodatDataContractsDatasetsAccountsReceivableIsBilledToType):
        record_refs (Union[Unset, None, List['CodatDataContractsDatasetsRecordRef']]):
        project_ref (Union[Unset, CodatDataContractsDatasetsProjectRef]):
        customer_ref (Union[Unset, CodatDataContractsDatasetsCustomerRef]):
    """

    category_refs: List["CodatDataContractsDatasetsTrackingCategoryRef"]
    is_billed_to: CodatDataContractsDatasetsAccountsReceivableIsBilledToType
    is_rebilled_to: CodatDataContractsDatasetsAccountsReceivableIsBilledToType
    record_refs: Union[Unset, None, List["CodatDataContractsDatasetsRecordRef"]] = UNSET
    project_ref: Union[Unset, "CodatDataContractsDatasetsProjectRef"] = UNSET
    customer_ref: Union[Unset, "CodatDataContractsDatasetsCustomerRef"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        category_refs = []
        for category_refs_item_data in self.category_refs:
            category_refs_item = category_refs_item_data.to_dict()

            category_refs.append(category_refs_item)

        is_billed_to = self.is_billed_to.value

        is_rebilled_to = self.is_rebilled_to.value

        record_refs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.record_refs, Unset):
            if self.record_refs is None:
                record_refs = None
            else:
                record_refs = []
                for record_refs_item_data in self.record_refs:
                    record_refs_item = record_refs_item_data.to_dict()

                    record_refs.append(record_refs_item)

        project_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_ref, Unset):
            project_ref = self.project_ref.to_dict()

        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "categoryRefs": category_refs,
                "isBilledTo": is_billed_to,
                "isRebilledTo": is_rebilled_to,
            }
        )
        if record_refs is not UNSET:
            field_dict["recordRefs"] = record_refs
        if project_ref is not UNSET:
            field_dict["projectRef"] = project_ref
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref

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

        is_billed_to = CodatDataContractsDatasetsAccountsReceivableIsBilledToType(d.pop("isBilledTo"))

        is_rebilled_to = CodatDataContractsDatasetsAccountsReceivableIsBilledToType(d.pop("isRebilledTo"))

        record_refs = []
        _record_refs = d.pop("recordRefs", UNSET)
        for record_refs_item_data in _record_refs or []:
            record_refs_item = CodatDataContractsDatasetsRecordRef.from_dict(record_refs_item_data)

            record_refs.append(record_refs_item)

        _project_ref = d.pop("projectRef", UNSET)
        project_ref: Union[Unset, CodatDataContractsDatasetsProjectRef]
        if isinstance(_project_ref, Unset):
            project_ref = UNSET
        else:
            project_ref = CodatDataContractsDatasetsProjectRef.from_dict(_project_ref)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CodatDataContractsDatasetsCustomerRef]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CodatDataContractsDatasetsCustomerRef.from_dict(_customer_ref)

        codat_data_contracts_datasets_accounts_receivable_tracking = cls(
            category_refs=category_refs,
            is_billed_to=is_billed_to,
            is_rebilled_to=is_rebilled_to,
            record_refs=record_refs,
            project_ref=project_ref,
            customer_ref=customer_ref,
        )

        return codat_data_contracts_datasets_accounts_receivable_tracking
