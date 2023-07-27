import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_account_status import CodatDataContractsDatasetsAccountStatus
from ..models.codat_data_contracts_datasets_account_type import CodatDataContractsDatasetsAccountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
        CodatDataContractsDatasetsDataInterfacesSupplementalData,
    )
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
    from ..models.codat_data_contracts_datasets_valid_datatype_links import CodatDataContractsDatasetsValidDatatypeLinks


T = TypeVar("T", bound="CodatDataContractsDatasetsAccount")


@define
class CodatDataContractsDatasetsAccount:
    """
    Attributes:
        type (CodatDataContractsDatasetsAccountType):
        status (CodatDataContractsDatasetsAccountStatus):
        is_bank_account (bool):
        id (Union[Unset, None, str]):
        nominal_code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        fully_qualified_category (Union[Unset, None, str]):
        fully_qualified_name (Union[Unset, None, str]):
        currency (Union[Unset, None, str]):
        current_balance (Union[Unset, None, float]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        valid_datatype_links (Union[Unset, None, List['CodatDataContractsDatasetsValidDatatypeLinks']]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
        supplemental_data (Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]):
    """

    type: CodatDataContractsDatasetsAccountType
    status: CodatDataContractsDatasetsAccountStatus
    is_bank_account: bool
    id: Union[Unset, None, str] = UNSET
    nominal_code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    fully_qualified_category: Union[Unset, None, str] = UNSET
    fully_qualified_name: Union[Unset, None, str] = UNSET
    currency: Union[Unset, None, str] = UNSET
    current_balance: Union[Unset, None, float] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    valid_datatype_links: Union[Unset, None, List["CodatDataContractsDatasetsValidDatatypeLinks"]] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET
    supplemental_data: Union[Unset, "CodatDataContractsDatasetsDataInterfacesSupplementalData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        status = self.status.value

        is_bank_account = self.is_bank_account
        id = self.id
        nominal_code = self.nominal_code
        name = self.name
        description = self.description
        fully_qualified_category = self.fully_qualified_category
        fully_qualified_name = self.fully_qualified_name
        currency = self.currency
        current_balance = self.current_balance
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

        supplemental_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplemental_data, Unset):
            supplemental_data = self.supplemental_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "status": status,
                "isBankAccount": is_bank_account,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if nominal_code is not UNSET:
            field_dict["nominalCode"] = nominal_code
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if fully_qualified_category is not UNSET:
            field_dict["fullyQualifiedCategory"] = fully_qualified_category
        if fully_qualified_name is not UNSET:
            field_dict["fullyQualifiedName"] = fully_qualified_name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if current_balance is not UNSET:
            field_dict["currentBalance"] = current_balance
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if valid_datatype_links is not UNSET:
            field_dict["validDatatypeLinks"] = valid_datatype_links
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if supplemental_data is not UNSET:
            field_dict["supplementalData"] = supplemental_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
            CodatDataContractsDatasetsDataInterfacesSupplementalData,
        )
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
        from ..models.codat_data_contracts_datasets_valid_datatype_links import (
            CodatDataContractsDatasetsValidDatatypeLinks,
        )

        d = src_dict.copy()
        type = CodatDataContractsDatasetsAccountType(d.pop("type"))

        status = CodatDataContractsDatasetsAccountStatus(d.pop("status"))

        is_bank_account = d.pop("isBankAccount")

        id = d.pop("id", UNSET)

        nominal_code = d.pop("nominalCode", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        fully_qualified_category = d.pop("fullyQualifiedCategory", UNSET)

        fully_qualified_name = d.pop("fullyQualifiedName", UNSET)

        currency = d.pop("currency", UNSET)

        current_balance = d.pop("currentBalance", UNSET)

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

        _supplemental_data = d.pop("supplementalData", UNSET)
        supplemental_data: Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]
        if isinstance(_supplemental_data, Unset):
            supplemental_data = UNSET
        else:
            supplemental_data = CodatDataContractsDatasetsDataInterfacesSupplementalData.from_dict(_supplemental_data)

        codat_data_contracts_datasets_account = cls(
            type=type,
            status=status,
            is_bank_account=is_bank_account,
            id=id,
            nominal_code=nominal_code,
            name=name,
            description=description,
            fully_qualified_category=fully_qualified_category,
            fully_qualified_name=fully_qualified_name,
            currency=currency,
            current_balance=current_balance,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            valid_datatype_links=valid_datatype_links,
            metadata=metadata,
            supplemental_data=supplemental_data,
        )

        return codat_data_contracts_datasets_account
