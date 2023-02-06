import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_tax_rate_status import CodatDataContractsDatasetsTaxRateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
    from ..models.codat_data_contracts_datasets_tax_rate_component import CodatDataContractsDatasetsTaxRateComponent
    from ..models.codat_data_contracts_datasets_valid_datatype_links import CodatDataContractsDatasetsValidDatatypeLinks


T = TypeVar("T", bound="CodatDataContractsDatasetsTaxRate")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsTaxRate:
    """
    Attributes:
        id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        code (Union[Unset, None, str]):
        status (Union[Unset, CodatDataContractsDatasetsTaxRateStatus]):
        effective_tax_rate (Union[Unset, None, float]):
        total_tax_rate (Union[Unset, None, float]):
        components (Union[Unset, None, List['CodatDataContractsDatasetsTaxRateComponent']]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        valid_datatype_links (Union[Unset, None, List['CodatDataContractsDatasetsValidDatatypeLinks']]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
    """

    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    code: Union[Unset, None, str] = UNSET
    status: Union[Unset, CodatDataContractsDatasetsTaxRateStatus] = UNSET
    effective_tax_rate: Union[Unset, None, float] = UNSET
    total_tax_rate: Union[Unset, None, float] = UNSET
    components: Union[Unset, None, List["CodatDataContractsDatasetsTaxRateComponent"]] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    valid_datatype_links: Union[Unset, None, List["CodatDataContractsDatasetsValidDatatypeLinks"]] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        code = self.code
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        effective_tax_rate = self.effective_tax_rate
        total_tax_rate = self.total_tax_rate
        components: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.components, Unset):
            if self.components is None:
                components = None
            else:
                components = []
                for components_item_data in self.components:
                    components_item = components_item_data.to_dict()

                    components.append(components_item)

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        valid_datatype_links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.valid_datatype_links, Unset):
            if self.valid_datatype_links is None:
                valid_datatype_links = None
            else:
                valid_datatype_links = []
                for valid_datatype_links_item_data in self.valid_datatype_links:
                    valid_datatype_links_item = valid_datatype_links_item_data.to_dict()

                    valid_datatype_links.append(valid_datatype_links_item)

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if status is not UNSET:
            field_dict["status"] = status
        if effective_tax_rate is not UNSET:
            field_dict["effectiveTaxRate"] = effective_tax_rate
        if total_tax_rate is not UNSET:
            field_dict["totalTaxRate"] = total_tax_rate
        if components is not UNSET:
            field_dict["components"] = components
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if valid_datatype_links is not UNSET:
            field_dict["validDatatypeLinks"] = valid_datatype_links
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
        from ..models.codat_data_contracts_datasets_tax_rate_component import CodatDataContractsDatasetsTaxRateComponent
        from ..models.codat_data_contracts_datasets_valid_datatype_links import (
            CodatDataContractsDatasetsValidDatatypeLinks,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CodatDataContractsDatasetsTaxRateStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodatDataContractsDatasetsTaxRateStatus(_status)

        effective_tax_rate = d.pop("effectiveTaxRate", UNSET)

        total_tax_rate = d.pop("totalTaxRate", UNSET)

        components = []
        _components = d.pop("components", UNSET)
        for components_item_data in _components or []:
            components_item = CodatDataContractsDatasetsTaxRateComponent.from_dict(components_item_data)

            components.append(components_item)

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

        valid_datatype_links = []
        _valid_datatype_links = d.pop("validDatatypeLinks", UNSET)
        for valid_datatype_links_item_data in _valid_datatype_links or []:
            valid_datatype_links_item = CodatDataContractsDatasetsValidDatatypeLinks.from_dict(
                valid_datatype_links_item_data
            )

            valid_datatype_links.append(valid_datatype_links_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CodatDataContractsDatasetsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CodatDataContractsDatasetsMetadata.from_dict(_metadata)

        codat_data_contracts_datasets_tax_rate = cls(
            id=id,
            name=name,
            code=code,
            status=status,
            effective_tax_rate=effective_tax_rate,
            total_tax_rate=total_tax_rate,
            components=components,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            valid_datatype_links=valid_datatype_links,
            metadata=metadata,
        )

        return codat_data_contracts_datasets_tax_rate
