import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_public_api_models_data_account_status_response import CodatPublicApiModelsDataAccountStatusResponse
from ..models.codat_public_api_models_data_account_type_response import CodatPublicApiModelsDataAccountTypeResponse
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_data_valid_datatype_links_response import (
        CodatPublicApiModelsDataValidDatatypeLinksResponse,
    )


T = TypeVar("T", bound="CodatPublicApiModelsDataAccountResponse")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsDataAccountResponse:
    """
    Attributes:
        id (Union[Unset, None, str]):
        nominal_code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        fully_qualified_category (Union[Unset, None, str]):
        fully_qualified_name (Union[Unset, None, str]):
        currency (Union[Unset, None, str]):
        current_balance (Union[Unset, None, float]):
        type (Union[Unset, CodatPublicApiModelsDataAccountTypeResponse]):
        status (Union[Unset, CodatPublicApiModelsDataAccountStatusResponse]):
        is_bank_account (Union[Unset, bool]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        valid_datatype_links (Union[Unset, None, List['CodatPublicApiModelsDataValidDatatypeLinksResponse']]):
    """

    id: Union[Unset, None, str] = UNSET
    nominal_code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    fully_qualified_category: Union[Unset, None, str] = UNSET
    fully_qualified_name: Union[Unset, None, str] = UNSET
    currency: Union[Unset, None, str] = UNSET
    current_balance: Union[Unset, None, float] = UNSET
    type: Union[Unset, CodatPublicApiModelsDataAccountTypeResponse] = UNSET
    status: Union[Unset, CodatPublicApiModelsDataAccountStatusResponse] = UNSET
    is_bank_account: Union[Unset, bool] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    valid_datatype_links: Union[Unset, None, List["CodatPublicApiModelsDataValidDatatypeLinksResponse"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        nominal_code = self.nominal_code
        name = self.name
        description = self.description
        fully_qualified_category = self.fully_qualified_category
        fully_qualified_name = self.fully_qualified_name
        currency = self.currency
        current_balance = self.current_balance
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        is_bank_account = self.is_bank_account
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

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
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
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if is_bank_account is not UNSET:
            field_dict["isBankAccount"] = is_bank_account
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if valid_datatype_links is not UNSET:
            field_dict["validDatatypeLinks"] = valid_datatype_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_data_valid_datatype_links_response import (
            CodatPublicApiModelsDataValidDatatypeLinksResponse,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        nominal_code = d.pop("nominalCode", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        fully_qualified_category = d.pop("fullyQualifiedCategory", UNSET)

        fully_qualified_name = d.pop("fullyQualifiedName", UNSET)

        currency = d.pop("currency", UNSET)

        current_balance = d.pop("currentBalance", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CodatPublicApiModelsDataAccountTypeResponse]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodatPublicApiModelsDataAccountTypeResponse(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CodatPublicApiModelsDataAccountStatusResponse]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodatPublicApiModelsDataAccountStatusResponse(_status)

        is_bank_account = d.pop("isBankAccount", UNSET)

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
            valid_datatype_links_item = CodatPublicApiModelsDataValidDatatypeLinksResponse.from_dict(
                valid_datatype_links_item_data
            )

            valid_datatype_links.append(valid_datatype_links_item)

        codat_public_api_models_data_account_response = cls(
            id=id,
            nominal_code=nominal_code,
            name=name,
            description=description,
            fully_qualified_category=fully_qualified_category,
            fully_qualified_name=fully_qualified_name,
            currency=currency,
            current_balance=current_balance,
            type=type,
            status=status,
            is_bank_account=is_bank_account,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            valid_datatype_links=valid_datatype_links,
        )

        return codat_public_api_models_data_account_response
