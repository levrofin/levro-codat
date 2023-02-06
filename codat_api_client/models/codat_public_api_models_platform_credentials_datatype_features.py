from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_platform_credentials_supported_feature_state import (
        CodatPublicApiModelsPlatformCredentialsSupportedFeatureState,
    )


T = TypeVar("T", bound="CodatPublicApiModelsPlatformCredentialsDatatypeFeatures")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsPlatformCredentialsDatatypeFeatures:
    """
    Attributes:
        datatype (Union[Unset, None, str]):
        supported_features (Union[Unset, None, List['CodatPublicApiModelsPlatformCredentialsSupportedFeatureState']]):
    """

    datatype: Union[Unset, None, str] = UNSET
    supported_features: Union[Unset, None, List["CodatPublicApiModelsPlatformCredentialsSupportedFeatureState"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        datatype = self.datatype
        supported_features: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.supported_features, Unset):
            if self.supported_features is None:
                supported_features = None
            else:
                supported_features = []
                for supported_features_item_data in self.supported_features:
                    supported_features_item = supported_features_item_data.to_dict()

                    supported_features.append(supported_features_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if datatype is not UNSET:
            field_dict["datatype"] = datatype
        if supported_features is not UNSET:
            field_dict["supportedFeatures"] = supported_features

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_platform_credentials_supported_feature_state import (
            CodatPublicApiModelsPlatformCredentialsSupportedFeatureState,
        )

        d = src_dict.copy()
        datatype = d.pop("datatype", UNSET)

        supported_features = []
        _supported_features = d.pop("supportedFeatures", UNSET)
        for supported_features_item_data in _supported_features or []:
            supported_features_item = CodatPublicApiModelsPlatformCredentialsSupportedFeatureState.from_dict(
                supported_features_item_data
            )

            supported_features.append(supported_features_item)

        codat_public_api_models_platform_credentials_datatype_features = cls(
            datatype=datatype,
            supported_features=supported_features,
        )

        return codat_public_api_models_platform_credentials_datatype_features
