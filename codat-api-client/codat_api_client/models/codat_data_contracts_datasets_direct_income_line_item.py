from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_account_ref import CodatDataContractsDatasetsAccountRef
    from ..models.codat_data_contracts_datasets_item_ref import CodatDataContractsDatasetsItemRef
    from ..models.codat_data_contracts_datasets_tax_rate_ref import CodatDataContractsDatasetsTaxRateRef
    from ..models.codat_data_contracts_datasets_tracking_category_ref import (
        CodatDataContractsDatasetsTrackingCategoryRef,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsDirectIncomeLineItem")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsDirectIncomeLineItem:
    """
    Attributes:
        unit_amount (float):
        quantity (float):
        description (Union[Unset, None, str]):
        discount_amount (Union[Unset, None, float]):
        discount_percentage (Union[Unset, None, float]):
        sub_total (Union[Unset, None, float]):
        tax_amount (Union[Unset, None, float]):
        total_amount (Union[Unset, None, float]):
        account_ref (Union[Unset, CodatDataContractsDatasetsAccountRef]):
        tax_rate_ref (Union[Unset, CodatDataContractsDatasetsTaxRateRef]):
        item_ref (Union[Unset, CodatDataContractsDatasetsItemRef]):
        tracking_category_refs (Union[Unset, None, List['CodatDataContractsDatasetsTrackingCategoryRef']]):
    """

    unit_amount: float
    quantity: float
    description: Union[Unset, None, str] = UNSET
    discount_amount: Union[Unset, None, float] = UNSET
    discount_percentage: Union[Unset, None, float] = UNSET
    sub_total: Union[Unset, None, float] = UNSET
    tax_amount: Union[Unset, None, float] = UNSET
    total_amount: Union[Unset, None, float] = UNSET
    account_ref: Union[Unset, "CodatDataContractsDatasetsAccountRef"] = UNSET
    tax_rate_ref: Union[Unset, "CodatDataContractsDatasetsTaxRateRef"] = UNSET
    item_ref: Union[Unset, "CodatDataContractsDatasetsItemRef"] = UNSET
    tracking_category_refs: Union[Unset, None, List["CodatDataContractsDatasetsTrackingCategoryRef"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        unit_amount = self.unit_amount
        quantity = self.quantity
        description = self.description
        discount_amount = self.discount_amount
        discount_percentage = self.discount_percentage
        sub_total = self.sub_total
        tax_amount = self.tax_amount
        total_amount = self.total_amount
        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        tax_rate_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_rate_ref, Unset):
            tax_rate_ref = self.tax_rate_ref.to_dict()

        item_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_ref, Unset):
            item_ref = self.item_ref.to_dict()

        tracking_category_refs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tracking_category_refs, Unset):
            if self.tracking_category_refs is None:
                tracking_category_refs = None
            else:
                tracking_category_refs = []
                for tracking_category_refs_item_data in self.tracking_category_refs:
                    tracking_category_refs_item = tracking_category_refs_item_data.to_dict()

                    tracking_category_refs.append(tracking_category_refs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "unitAmount": unit_amount,
                "quantity": quantity,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if discount_amount is not UNSET:
            field_dict["discountAmount"] = discount_amount
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if tax_rate_ref is not UNSET:
            field_dict["taxRateRef"] = tax_rate_ref
        if item_ref is not UNSET:
            field_dict["itemRef"] = item_ref
        if tracking_category_refs is not UNSET:
            field_dict["trackingCategoryRefs"] = tracking_category_refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_account_ref import CodatDataContractsDatasetsAccountRef
        from ..models.codat_data_contracts_datasets_item_ref import CodatDataContractsDatasetsItemRef
        from ..models.codat_data_contracts_datasets_tax_rate_ref import CodatDataContractsDatasetsTaxRateRef
        from ..models.codat_data_contracts_datasets_tracking_category_ref import (
            CodatDataContractsDatasetsTrackingCategoryRef,
        )

        d = src_dict.copy()
        unit_amount = d.pop("unitAmount")

        quantity = d.pop("quantity")

        description = d.pop("description", UNSET)

        discount_amount = d.pop("discountAmount", UNSET)

        discount_percentage = d.pop("discountPercentage", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, CodatDataContractsDatasetsAccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = CodatDataContractsDatasetsAccountRef.from_dict(_account_ref)

        _tax_rate_ref = d.pop("taxRateRef", UNSET)
        tax_rate_ref: Union[Unset, CodatDataContractsDatasetsTaxRateRef]
        if isinstance(_tax_rate_ref, Unset):
            tax_rate_ref = UNSET
        else:
            tax_rate_ref = CodatDataContractsDatasetsTaxRateRef.from_dict(_tax_rate_ref)

        _item_ref = d.pop("itemRef", UNSET)
        item_ref: Union[Unset, CodatDataContractsDatasetsItemRef]
        if isinstance(_item_ref, Unset):
            item_ref = UNSET
        else:
            item_ref = CodatDataContractsDatasetsItemRef.from_dict(_item_ref)

        tracking_category_refs = []
        _tracking_category_refs = d.pop("trackingCategoryRefs", UNSET)
        for tracking_category_refs_item_data in _tracking_category_refs or []:
            tracking_category_refs_item = CodatDataContractsDatasetsTrackingCategoryRef.from_dict(
                tracking_category_refs_item_data
            )

            tracking_category_refs.append(tracking_category_refs_item)

        codat_data_contracts_datasets_direct_income_line_item = cls(
            unit_amount=unit_amount,
            quantity=quantity,
            description=description,
            discount_amount=discount_amount,
            discount_percentage=discount_percentage,
            sub_total=sub_total,
            tax_amount=tax_amount,
            total_amount=total_amount,
            account_ref=account_ref,
            tax_rate_ref=tax_rate_ref,
            item_ref=item_ref,
            tracking_category_refs=tracking_category_refs,
        )

        return codat_data_contracts_datasets_direct_income_line_item
