import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_commerce_product_status import (
    CodatDataContractsDatasetsCommerceProductStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_product_category_ref import (
        CodatDataContractsDatasetsCommerceProductCategoryRef,
    )
    from ..models.codat_data_contracts_datasets_commerce_product_variant import (
        CodatDataContractsDatasetsCommerceProductVariant,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceProduct")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCommerceProduct:
    """
    Attributes:
        id (Union[Unset, None, str]):
        categorization (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        product_category_refs (Union[Unset, None, List['CodatDataContractsDatasetsCommerceProductCategoryRef']]):
        is_gift_card (Union[Unset, bool]):
        variants (Union[Unset, None, List['CodatDataContractsDatasetsCommerceProductVariant']]):
        created_date (Union[Unset, datetime.datetime]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        status (Union[Unset, CodatDataContractsDatasetsCommerceProductStatus]):
    """

    id: Union[Unset, None, str] = UNSET
    categorization: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    product_category_refs: Union[Unset, None, List["CodatDataContractsDatasetsCommerceProductCategoryRef"]] = UNSET
    is_gift_card: Union[Unset, bool] = UNSET
    variants: Union[Unset, None, List["CodatDataContractsDatasetsCommerceProductVariant"]] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    status: Union[Unset, CodatDataContractsDatasetsCommerceProductStatus] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        categorization = self.categorization
        name = self.name
        description = self.description
        product_category_refs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.product_category_refs, Unset):
            if self.product_category_refs is None:
                product_category_refs = None
            else:
                product_category_refs = []
                for product_category_refs_item_data in self.product_category_refs:
                    product_category_refs_item = product_category_refs_item_data.to_dict()

                    product_category_refs.append(product_category_refs_item)

        is_gift_card = self.is_gift_card
        variants: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.variants, Unset):
            if self.variants is None:
                variants = None
            else:
                variants = []
                for variants_item_data in self.variants:
                    variants_item = variants_item_data.to_dict()

                    variants.append(variants_item)

        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if categorization is not UNSET:
            field_dict["categorization"] = categorization
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if product_category_refs is not UNSET:
            field_dict["productCategoryRefs"] = product_category_refs
        if is_gift_card is not UNSET:
            field_dict["isGiftCard"] = is_gift_card
        if variants is not UNSET:
            field_dict["variants"] = variants
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_commerce_product_category_ref import (
            CodatDataContractsDatasetsCommerceProductCategoryRef,
        )
        from ..models.codat_data_contracts_datasets_commerce_product_variant import (
            CodatDataContractsDatasetsCommerceProductVariant,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        categorization = d.pop("categorization", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        product_category_refs = []
        _product_category_refs = d.pop("productCategoryRefs", UNSET)
        for product_category_refs_item_data in _product_category_refs or []:
            product_category_refs_item = CodatDataContractsDatasetsCommerceProductCategoryRef.from_dict(
                product_category_refs_item_data
            )

            product_category_refs.append(product_category_refs_item)

        is_gift_card = d.pop("isGiftCard", UNSET)

        variants = []
        _variants = d.pop("variants", UNSET)
        for variants_item_data in _variants or []:
            variants_item = CodatDataContractsDatasetsCommerceProductVariant.from_dict(variants_item_data)

            variants.append(variants_item)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

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

        _status = d.pop("status", UNSET)
        status: Union[Unset, CodatDataContractsDatasetsCommerceProductStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodatDataContractsDatasetsCommerceProductStatus(_status)

        codat_data_contracts_datasets_commerce_product = cls(
            id=id,
            categorization=categorization,
            name=name,
            description=description,
            product_category_refs=product_category_refs,
            is_gift_card=is_gift_card,
            variants=variants,
            created_date=created_date,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            status=status,
        )

        return codat_data_contracts_datasets_commerce_product
