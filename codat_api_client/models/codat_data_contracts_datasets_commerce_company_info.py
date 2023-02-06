import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_commerce_account_balance import (
        CodatDataContractsDatasetsCommerceAccountBalance,
    )
    from ..models.codat_data_contracts_datasets_commerce_address import CodatDataContractsDatasetsCommerceAddress
    from ..models.codat_data_contracts_datasets_commerce_company_info_source_urls import (
        CodatDataContractsDatasetsCommerceCompanyInfoSourceUrls,
    )
    from ..models.codat_data_contracts_datasets_commerce_phone import CodatDataContractsDatasetsCommercePhone
    from ..models.codat_data_contracts_datasets_commerce_web_link import CodatDataContractsDatasetsCommerceWebLink


T = TypeVar("T", bound="CodatDataContractsDatasetsCommerceCompanyInfo")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCommerceCompanyInfo:
    """
    Attributes:
        company_name (Union[Unset, None, str]):
        commerce_platform_ref (Union[Unset, None, str]):
        company_legal_name (Union[Unset, None, str]):
        addresses (Union[Unset, None, List['CodatDataContractsDatasetsCommerceAddress']]):
        phone_numbers (Union[Unset, None, List['CodatDataContractsDatasetsCommercePhone']]):
        web_links (Union[Unset, None, List['CodatDataContractsDatasetsCommerceWebLink']]):
        registration_number (Union[Unset, None, str]):
        base_currency (Union[Unset, None, str]):
        account_balances (Union[Unset, None, List['CodatDataContractsDatasetsCommerceAccountBalance']]):
        source_urls (Union[Unset, None, CodatDataContractsDatasetsCommerceCompanyInfoSourceUrls]):
        created_date (Union[Unset, datetime.datetime]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
    """

    company_name: Union[Unset, None, str] = UNSET
    commerce_platform_ref: Union[Unset, None, str] = UNSET
    company_legal_name: Union[Unset, None, str] = UNSET
    addresses: Union[Unset, None, List["CodatDataContractsDatasetsCommerceAddress"]] = UNSET
    phone_numbers: Union[Unset, None, List["CodatDataContractsDatasetsCommercePhone"]] = UNSET
    web_links: Union[Unset, None, List["CodatDataContractsDatasetsCommerceWebLink"]] = UNSET
    registration_number: Union[Unset, None, str] = UNSET
    base_currency: Union[Unset, None, str] = UNSET
    account_balances: Union[Unset, None, List["CodatDataContractsDatasetsCommerceAccountBalance"]] = UNSET
    source_urls: Union[Unset, None, "CodatDataContractsDatasetsCommerceCompanyInfoSourceUrls"] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_name = self.company_name
        commerce_platform_ref = self.commerce_platform_ref
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

        registration_number = self.registration_number
        base_currency = self.base_currency
        account_balances: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.account_balances, Unset):
            if self.account_balances is None:
                account_balances = None
            else:
                account_balances = []
                for account_balances_item_data in self.account_balances:
                    account_balances_item = account_balances_item_data.to_dict()

                    account_balances.append(account_balances_item)

        source_urls: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.source_urls, Unset):
            source_urls = self.source_urls.to_dict() if self.source_urls else None

        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if commerce_platform_ref is not UNSET:
            field_dict["commercePlatformRef"] = commerce_platform_ref
        if company_legal_name is not UNSET:
            field_dict["companyLegalName"] = company_legal_name
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if phone_numbers is not UNSET:
            field_dict["phoneNumbers"] = phone_numbers
        if web_links is not UNSET:
            field_dict["webLinks"] = web_links
        if registration_number is not UNSET:
            field_dict["registrationNumber"] = registration_number
        if base_currency is not UNSET:
            field_dict["baseCurrency"] = base_currency
        if account_balances is not UNSET:
            field_dict["accountBalances"] = account_balances
        if source_urls is not UNSET:
            field_dict["sourceUrls"] = source_urls
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_commerce_account_balance import (
            CodatDataContractsDatasetsCommerceAccountBalance,
        )
        from ..models.codat_data_contracts_datasets_commerce_address import CodatDataContractsDatasetsCommerceAddress
        from ..models.codat_data_contracts_datasets_commerce_company_info_source_urls import (
            CodatDataContractsDatasetsCommerceCompanyInfoSourceUrls,
        )
        from ..models.codat_data_contracts_datasets_commerce_phone import CodatDataContractsDatasetsCommercePhone
        from ..models.codat_data_contracts_datasets_commerce_web_link import CodatDataContractsDatasetsCommerceWebLink

        d = src_dict.copy()
        company_name = d.pop("companyName", UNSET)

        commerce_platform_ref = d.pop("commercePlatformRef", UNSET)

        company_legal_name = d.pop("companyLegalName", UNSET)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = CodatDataContractsDatasetsCommerceAddress.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        phone_numbers = []
        _phone_numbers = d.pop("phoneNumbers", UNSET)
        for phone_numbers_item_data in _phone_numbers or []:
            phone_numbers_item = CodatDataContractsDatasetsCommercePhone.from_dict(phone_numbers_item_data)

            phone_numbers.append(phone_numbers_item)

        web_links = []
        _web_links = d.pop("webLinks", UNSET)
        for web_links_item_data in _web_links or []:
            web_links_item = CodatDataContractsDatasetsCommerceWebLink.from_dict(web_links_item_data)

            web_links.append(web_links_item)

        registration_number = d.pop("registrationNumber", UNSET)

        base_currency = d.pop("baseCurrency", UNSET)

        account_balances = []
        _account_balances = d.pop("accountBalances", UNSET)
        for account_balances_item_data in _account_balances or []:
            account_balances_item = CodatDataContractsDatasetsCommerceAccountBalance.from_dict(
                account_balances_item_data
            )

            account_balances.append(account_balances_item)

        _source_urls = d.pop("sourceUrls", UNSET)
        source_urls: Union[Unset, None, CodatDataContractsDatasetsCommerceCompanyInfoSourceUrls]
        if _source_urls is None:
            source_urls = None
        elif isinstance(_source_urls, Unset):
            source_urls = UNSET
        else:
            source_urls = CodatDataContractsDatasetsCommerceCompanyInfoSourceUrls.from_dict(_source_urls)

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

        codat_data_contracts_datasets_commerce_company_info = cls(
            company_name=company_name,
            commerce_platform_ref=commerce_platform_ref,
            company_legal_name=company_legal_name,
            addresses=addresses,
            phone_numbers=phone_numbers,
            web_links=web_links,
            registration_number=registration_number,
            base_currency=base_currency,
            account_balances=account_balances,
            source_urls=source_urls,
            created_date=created_date,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
        )

        return codat_data_contracts_datasets_commerce_company_info
