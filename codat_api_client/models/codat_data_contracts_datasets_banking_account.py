import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_banking_account_type import CodatDataContractsDatasetsBankingAccountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_banking_account_balance_amounts import (
        CodatDataContractsDatasetsBankingAccountBalanceAmounts,
    )
    from ..models.codat_data_contracts_datasets_banking_account_identifiers import (
        CodatDataContractsDatasetsBankingAccountIdentifiers,
    )
    from ..models.codat_data_contracts_datasets_banking_account_institution import (
        CodatDataContractsDatasetsBankingAccountInstitution,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsBankingAccount")


@define
class CodatDataContractsDatasetsBankingAccount:
    """
    Attributes:
        id (str):
        name (str):
        type (CodatDataContractsDatasetsBankingAccountType):
        balance (CodatDataContractsDatasetsBankingAccountBalanceAmounts):
        identifiers (CodatDataContractsDatasetsBankingAccountIdentifiers):
        currency (str):
        institution (CodatDataContractsDatasetsBankingAccountInstitution):
        informal_name (Union[Unset, None, str]):
        holder (Union[Unset, None, str]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    id: str
    name: str
    type: CodatDataContractsDatasetsBankingAccountType
    balance: "CodatDataContractsDatasetsBankingAccountBalanceAmounts"
    identifiers: "CodatDataContractsDatasetsBankingAccountIdentifiers"
    currency: str
    institution: "CodatDataContractsDatasetsBankingAccountInstitution"
    informal_name: Union[Unset, None, str] = UNSET
    holder: Union[Unset, None, str] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type = self.type.value

        balance = self.balance.to_dict()

        identifiers = self.identifiers.to_dict()

        currency = self.currency
        institution = self.institution.to_dict()

        informal_name = self.informal_name
        holder = self.holder
        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type,
                "balance": balance,
                "identifiers": identifiers,
                "currency": currency,
                "institution": institution,
            }
        )
        if informal_name is not UNSET:
            field_dict["informalName"] = informal_name
        if holder is not UNSET:
            field_dict["holder"] = holder
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_banking_account_balance_amounts import (
            CodatDataContractsDatasetsBankingAccountBalanceAmounts,
        )
        from ..models.codat_data_contracts_datasets_banking_account_identifiers import (
            CodatDataContractsDatasetsBankingAccountIdentifiers,
        )
        from ..models.codat_data_contracts_datasets_banking_account_institution import (
            CodatDataContractsDatasetsBankingAccountInstitution,
        )

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        type = CodatDataContractsDatasetsBankingAccountType(d.pop("type"))

        balance = CodatDataContractsDatasetsBankingAccountBalanceAmounts.from_dict(d.pop("balance"))

        identifiers = CodatDataContractsDatasetsBankingAccountIdentifiers.from_dict(d.pop("identifiers"))

        currency = d.pop("currency")

        institution = CodatDataContractsDatasetsBankingAccountInstitution.from_dict(d.pop("institution"))

        informal_name = d.pop("informalName", UNSET)

        holder = d.pop("holder", UNSET)

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

        codat_data_contracts_datasets_banking_account = cls(
            id=id,
            name=name,
            type=type,
            balance=balance,
            identifiers=identifiers,
            currency=currency,
            institution=institution,
            informal_name=informal_name,
            holder=holder,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_banking_account
