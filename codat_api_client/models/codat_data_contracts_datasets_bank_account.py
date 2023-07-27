import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_bank_account_type import CodatDataContractsDatasetsBankAccountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
        CodatDataContractsDatasetsDataInterfacesSupplementalData,
    )
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata


T = TypeVar("T", bound="CodatDataContractsDatasetsBankAccount")


@define
class CodatDataContractsDatasetsBankAccount:
    """
    Attributes:
        id (Union[Unset, None, str]):
        account_name (Union[Unset, None, str]):
        account_type (Union[Unset, CodatDataContractsDatasetsBankAccountType]):
        nominal_code (Union[Unset, None, str]):
        sort_code (Union[Unset, None, str]):
        account_number (Union[Unset, None, str]):
        i_ban (Union[Unset, None, str]):
        currency (Union[Unset, None, str]):
        balance (Union[Unset, None, float]):
        institution (Union[Unset, None, str]):
        supplemental_data (Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]):
        available_balance (Union[Unset, None, float]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        overdraft_limit (Union[Unset, None, float]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
    """

    id: Union[Unset, None, str] = UNSET
    account_name: Union[Unset, None, str] = UNSET
    account_type: Union[Unset, CodatDataContractsDatasetsBankAccountType] = UNSET
    nominal_code: Union[Unset, None, str] = UNSET
    sort_code: Union[Unset, None, str] = UNSET
    account_number: Union[Unset, None, str] = UNSET
    i_ban: Union[Unset, None, str] = UNSET
    currency: Union[Unset, None, str] = UNSET
    balance: Union[Unset, None, float] = UNSET
    institution: Union[Unset, None, str] = UNSET
    supplemental_data: Union[Unset, "CodatDataContractsDatasetsDataInterfacesSupplementalData"] = UNSET
    available_balance: Union[Unset, None, float] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    overdraft_limit: Union[Unset, None, float] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        account_name = self.account_name
        account_type: Union[Unset, str] = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        nominal_code = self.nominal_code
        sort_code = self.sort_code
        account_number = self.account_number
        i_ban = self.i_ban
        currency = self.currency
        balance = self.balance
        institution = self.institution
        supplemental_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplemental_data, Unset):
            supplemental_data = self.supplemental_data.to_dict()

        available_balance = self.available_balance
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        overdraft_limit = self.overdraft_limit
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if nominal_code is not UNSET:
            field_dict["nominalCode"] = nominal_code
        if sort_code is not UNSET:
            field_dict["sortCode"] = sort_code
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if i_ban is not UNSET:
            field_dict["iBan"] = i_ban
        if currency is not UNSET:
            field_dict["currency"] = currency
        if balance is not UNSET:
            field_dict["balance"] = balance
        if institution is not UNSET:
            field_dict["institution"] = institution
        if supplemental_data is not UNSET:
            field_dict["supplementalData"] = supplemental_data
        if available_balance is not UNSET:
            field_dict["availableBalance"] = available_balance
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if overdraft_limit is not UNSET:
            field_dict["overdraftLimit"] = overdraft_limit
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
            CodatDataContractsDatasetsDataInterfacesSupplementalData,
        )
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        account_name = d.pop("accountName", UNSET)

        _account_type = d.pop("accountType", UNSET)
        account_type: Union[Unset, CodatDataContractsDatasetsBankAccountType]
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = CodatDataContractsDatasetsBankAccountType(_account_type)

        nominal_code = d.pop("nominalCode", UNSET)

        sort_code = d.pop("sortCode", UNSET)

        account_number = d.pop("accountNumber", UNSET)

        i_ban = d.pop("iBan", UNSET)

        currency = d.pop("currency", UNSET)

        balance = d.pop("balance", UNSET)

        institution = d.pop("institution", UNSET)

        _supplemental_data = d.pop("supplementalData", UNSET)
        supplemental_data: Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]
        if isinstance(_supplemental_data, Unset):
            supplemental_data = UNSET
        else:
            supplemental_data = CodatDataContractsDatasetsDataInterfacesSupplementalData.from_dict(_supplemental_data)

        available_balance = d.pop("availableBalance", UNSET)

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

        overdraft_limit = d.pop("overdraftLimit", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CodatDataContractsDatasetsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CodatDataContractsDatasetsMetadata.from_dict(_metadata)

        codat_data_contracts_datasets_bank_account = cls(
            id=id,
            account_name=account_name,
            account_type=account_type,
            nominal_code=nominal_code,
            sort_code=sort_code,
            account_number=account_number,
            i_ban=i_ban,
            currency=currency,
            balance=balance,
            institution=institution,
            supplemental_data=supplemental_data,
            available_balance=available_balance,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            overdraft_limit=overdraft_limit,
            metadata=metadata,
        )

        return codat_data_contracts_datasets_bank_account
