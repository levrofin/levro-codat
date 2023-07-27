import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_address import CodatDataContractsDatasetsAddress
    from ..models.codat_data_contracts_datasets_company_dataset_source_urls import (
        CodatDataContractsDatasetsCompanyDatasetSourceUrls,
    )
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
        CodatDataContractsDatasetsDataInterfacesSupplementalData,
    )
    from ..models.codat_data_contracts_datasets_phone import CodatDataContractsDatasetsPhone
    from ..models.codat_data_contracts_datasets_web_link import CodatDataContractsDatasetsWebLink


T = TypeVar("T", bound="CodatDataContractsDatasetsCompanyDataset")


@define
class CodatDataContractsDatasetsCompanyDataset:
    """
    Attributes:
        company_name (Union[Unset, None, str]):
        accounting_platform_ref (Union[Unset, None, str]):
        company_legal_name (Union[Unset, None, str]):
        addresses (Union[Unset, None, List['CodatDataContractsDatasetsAddress']]):
        phone_numbers (Union[Unset, None, List['CodatDataContractsDatasetsPhone']]):
        web_links (Union[Unset, None, List['CodatDataContractsDatasetsWebLink']]):
        ledger_lock_date (Union[Unset, None, datetime.datetime]):
        registration_number (Union[Unset, None, str]):
        tax_number (Union[Unset, None, str]):
        financial_year_start_date (Union[Unset, None, datetime.datetime]):
        base_currency (Union[Unset, None, str]):
        source_urls (Union[Unset, None, CodatDataContractsDatasetsCompanyDatasetSourceUrls]):
        created_date (Union[Unset, None, datetime.datetime]):
        contract_version (Union[Unset, None, str]):
        supplemental_data (Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]):
    """

    company_name: Union[Unset, None, str] = UNSET
    accounting_platform_ref: Union[Unset, None, str] = UNSET
    company_legal_name: Union[Unset, None, str] = UNSET
    addresses: Union[Unset, None, List["CodatDataContractsDatasetsAddress"]] = UNSET
    phone_numbers: Union[Unset, None, List["CodatDataContractsDatasetsPhone"]] = UNSET
    web_links: Union[Unset, None, List["CodatDataContractsDatasetsWebLink"]] = UNSET
    ledger_lock_date: Union[Unset, None, datetime.datetime] = UNSET
    registration_number: Union[Unset, None, str] = UNSET
    tax_number: Union[Unset, None, str] = UNSET
    financial_year_start_date: Union[Unset, None, datetime.datetime] = UNSET
    base_currency: Union[Unset, None, str] = UNSET
    source_urls: Union[Unset, None, "CodatDataContractsDatasetsCompanyDatasetSourceUrls"] = UNSET
    created_date: Union[Unset, None, datetime.datetime] = UNSET
    contract_version: Union[Unset, None, str] = UNSET
    supplemental_data: Union[Unset, "CodatDataContractsDatasetsDataInterfacesSupplementalData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_name = self.company_name
        accounting_platform_ref = self.accounting_platform_ref
        company_legal_name = self.company_legal_name
        addresses: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            if self.addresses is None:
                addresses = None
            else:
                addresses = []
                for addresses_item_data in self.addresses:
                    addresses_item = addresses_item_data.to_dict()

                    addresses.append(addresses_item)

        phone_numbers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.phone_numbers, Unset):
            if self.phone_numbers is None:
                phone_numbers = None
            else:
                phone_numbers = []
                for phone_numbers_item_data in self.phone_numbers:
                    phone_numbers_item = phone_numbers_item_data.to_dict()

                    phone_numbers.append(phone_numbers_item)

        web_links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.web_links, Unset):
            if self.web_links is None:
                web_links = None
            else:
                web_links = []
                for web_links_item_data in self.web_links:
                    web_links_item = web_links_item_data.to_dict()

                    web_links.append(web_links_item)

        ledger_lock_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.ledger_lock_date, Unset):
            ledger_lock_date = self.ledger_lock_date.isoformat() if self.ledger_lock_date else None

        registration_number = self.registration_number
        tax_number = self.tax_number
        financial_year_start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.financial_year_start_date, Unset):
            financial_year_start_date = (
                self.financial_year_start_date.isoformat() if self.financial_year_start_date else None
            )

        base_currency = self.base_currency
        source_urls: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.source_urls, Unset):
            source_urls = self.source_urls.to_dict() if self.source_urls else None

        created_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat() if self.created_date else None

        contract_version = self.contract_version
        supplemental_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplemental_data, Unset):
            supplemental_data = self.supplemental_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if accounting_platform_ref is not UNSET:
            field_dict["accountingPlatformRef"] = accounting_platform_ref
        if company_legal_name is not UNSET:
            field_dict["companyLegalName"] = company_legal_name
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if phone_numbers is not UNSET:
            field_dict["phoneNumbers"] = phone_numbers
        if web_links is not UNSET:
            field_dict["webLinks"] = web_links
        if ledger_lock_date is not UNSET:
            field_dict["ledgerLockDate"] = ledger_lock_date
        if registration_number is not UNSET:
            field_dict["registrationNumber"] = registration_number
        if tax_number is not UNSET:
            field_dict["taxNumber"] = tax_number
        if financial_year_start_date is not UNSET:
            field_dict["financialYearStartDate"] = financial_year_start_date
        if base_currency is not UNSET:
            field_dict["baseCurrency"] = base_currency
        if source_urls is not UNSET:
            field_dict["sourceUrls"] = source_urls
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if contract_version is not UNSET:
            field_dict["contractVersion"] = contract_version
        if supplemental_data is not UNSET:
            field_dict["supplementalData"] = supplemental_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_address import CodatDataContractsDatasetsAddress
        from ..models.codat_data_contracts_datasets_company_dataset_source_urls import (
            CodatDataContractsDatasetsCompanyDatasetSourceUrls,
        )
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
            CodatDataContractsDatasetsDataInterfacesSupplementalData,
        )
        from ..models.codat_data_contracts_datasets_phone import CodatDataContractsDatasetsPhone
        from ..models.codat_data_contracts_datasets_web_link import CodatDataContractsDatasetsWebLink

        d = src_dict.copy()
        company_name = d.pop("companyName", UNSET)

        accounting_platform_ref = d.pop("accountingPlatformRef", UNSET)

        company_legal_name = d.pop("companyLegalName", UNSET)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = CodatDataContractsDatasetsAddress.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        phone_numbers = []
        _phone_numbers = d.pop("phoneNumbers", UNSET)
        for phone_numbers_item_data in _phone_numbers or []:
            phone_numbers_item = CodatDataContractsDatasetsPhone.from_dict(phone_numbers_item_data)

            phone_numbers.append(phone_numbers_item)

        web_links = []
        _web_links = d.pop("webLinks", UNSET)
        for web_links_item_data in _web_links or []:
            web_links_item = CodatDataContractsDatasetsWebLink.from_dict(web_links_item_data)

            web_links.append(web_links_item)

        _ledger_lock_date = d.pop("ledgerLockDate", UNSET)
        ledger_lock_date: Union[Unset, None, datetime.datetime]
        if _ledger_lock_date is None:
            ledger_lock_date = None
        elif isinstance(_ledger_lock_date, Unset):
            ledger_lock_date = UNSET
        else:
            ledger_lock_date = isoparse(_ledger_lock_date)

        registration_number = d.pop("registrationNumber", UNSET)

        tax_number = d.pop("taxNumber", UNSET)

        _financial_year_start_date = d.pop("financialYearStartDate", UNSET)
        financial_year_start_date: Union[Unset, None, datetime.datetime]
        if _financial_year_start_date is None:
            financial_year_start_date = None
        elif isinstance(_financial_year_start_date, Unset):
            financial_year_start_date = UNSET
        else:
            financial_year_start_date = isoparse(_financial_year_start_date)

        base_currency = d.pop("baseCurrency", UNSET)

        _source_urls = d.pop("sourceUrls", UNSET)
        source_urls: Union[Unset, None, CodatDataContractsDatasetsCompanyDatasetSourceUrls]
        if _source_urls is None:
            source_urls = None
        elif isinstance(_source_urls, Unset):
            source_urls = UNSET
        else:
            source_urls = CodatDataContractsDatasetsCompanyDatasetSourceUrls.from_dict(_source_urls)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, None, datetime.datetime]
        if _created_date is None:
            created_date = None
        elif isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        contract_version = d.pop("contractVersion", UNSET)

        _supplemental_data = d.pop("supplementalData", UNSET)
        supplemental_data: Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]
        if isinstance(_supplemental_data, Unset):
            supplemental_data = UNSET
        else:
            supplemental_data = CodatDataContractsDatasetsDataInterfacesSupplementalData.from_dict(_supplemental_data)

        codat_data_contracts_datasets_company_dataset = cls(
            company_name=company_name,
            accounting_platform_ref=accounting_platform_ref,
            company_legal_name=company_legal_name,
            addresses=addresses,
            phone_numbers=phone_numbers,
            web_links=web_links,
            ledger_lock_date=ledger_lock_date,
            registration_number=registration_number,
            tax_number=tax_number,
            financial_year_start_date=financial_year_start_date,
            base_currency=base_currency,
            source_urls=source_urls,
            created_date=created_date,
            contract_version=contract_version,
            supplemental_data=supplemental_data,
        )

        return codat_data_contracts_datasets_company_dataset
