from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="CodatPublicApiModelsPlatformCredentialsPlatformCredentials")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsPlatformCredentialsPlatformCredentials:
    """ """

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        codat_public_api_models_platform_credentials_platform_credentials = cls()

        return codat_public_api_models_platform_credentials_platform_credentials
