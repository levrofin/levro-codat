from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define, field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostCompaniesCompanyIdConnectionsJsonBody")


@define
class PostCompaniesCompanyIdConnectionsJsonBody:
    """
    Attributes:
        platform_key (Union[Unset, str]):
    """

    platform_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        platform_key = self.platform_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform_key is not UNSET:
            field_dict["platformKey"] = platform_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        platform_key = d.pop("platformKey", UNSET)

        post_companies_company_id_connections_json_body = cls(
            platform_key=platform_key,
        )

        post_companies_company_id_connections_json_body.additional_properties = d
        return post_companies_company_id_connections_json_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
