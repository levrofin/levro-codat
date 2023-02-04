from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsPlatformCredentialsEnabledArgs")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsPlatformCredentialsEnabledArgs:
    """
    Attributes:
        enabled (Union[Unset, bool]):
    """

    enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        codat_public_api_models_platform_credentials_enabled_args = cls(
            enabled=enabled,
        )

        return codat_public_api_models_platform_credentials_enabled_args
