from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsCompanyProfileModel")


@define
class CodatPublicApiModelsCompanyProfileModel:
    """
    Attributes:
        name (Union[Unset, None, str]):
        logo_url (Union[Unset, None, str]):
        icon_url (Union[Unset, None, str]):
        redirect_url (Union[Unset, None, str]):
        white_list_urls (Union[Unset, None, List[str]]):
        api_key (Union[Unset, None, str]):
        alert_auth_header (Union[Unset, None, str]):
        confirm_company_name (Union[Unset, bool]):
    """

    name: Union[Unset, None, str] = UNSET
    logo_url: Union[Unset, None, str] = UNSET
    icon_url: Union[Unset, None, str] = UNSET
    redirect_url: Union[Unset, None, str] = UNSET
    white_list_urls: Union[Unset, None, List[str]] = UNSET
    api_key: Union[Unset, None, str] = UNSET
    alert_auth_header: Union[Unset, None, str] = UNSET
    confirm_company_name: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        logo_url = self.logo_url
        icon_url = self.icon_url
        redirect_url = self.redirect_url
        white_list_urls: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.white_list_urls, Unset):
            if self.white_list_urls is None:
                white_list_urls = None
            else:
                white_list_urls = self.white_list_urls

        api_key = self.api_key
        alert_auth_header = self.alert_auth_header
        confirm_company_name = self.confirm_company_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if redirect_url is not UNSET:
            field_dict["redirectUrl"] = redirect_url
        if white_list_urls is not UNSET:
            field_dict["whiteListUrls"] = white_list_urls
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if alert_auth_header is not UNSET:
            field_dict["alertAuthHeader"] = alert_auth_header
        if confirm_company_name is not UNSET:
            field_dict["confirmCompanyName"] = confirm_company_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        redirect_url = d.pop("redirectUrl", UNSET)

        white_list_urls = cast(List[str], d.pop("whiteListUrls", UNSET))

        api_key = d.pop("apiKey", UNSET)

        alert_auth_header = d.pop("alertAuthHeader", UNSET)

        confirm_company_name = d.pop("confirmCompanyName", UNSET)

        codat_public_api_models_company_profile_model = cls(
            name=name,
            logo_url=logo_url,
            icon_url=icon_url,
            redirect_url=redirect_url,
            white_list_urls=white_list_urls,
            api_key=api_key,
            alert_auth_header=alert_auth_header,
            confirm_company_name=confirm_company_name,
        )

        return codat_public_api_models_company_profile_model
