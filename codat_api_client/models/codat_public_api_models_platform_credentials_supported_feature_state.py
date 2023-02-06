from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsPlatformCredentialsSupportedFeatureState")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsPlatformCredentialsSupportedFeatureState:
    """
    Attributes:
        feature_type (Union[Unset, None, str]):
        feature_state (Union[Unset, None, str]):
    """

    feature_type: Union[Unset, None, str] = UNSET
    feature_state: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        feature_type = self.feature_type
        feature_state = self.feature_state

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if feature_type is not UNSET:
            field_dict["featureType"] = feature_type
        if feature_state is not UNSET:
            field_dict["featureState"] = feature_state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        feature_type = d.pop("featureType", UNSET)

        feature_state = d.pop("featureState", UNSET)

        codat_public_api_models_platform_credentials_supported_feature_state = cls(
            feature_type=feature_type,
            feature_state=feature_state,
        )

        return codat_public_api_models_platform_credentials_supported_feature_state
