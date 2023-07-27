from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..models.codat_public_api_models_platform_credentials_data_provided_by import (
    CodatPublicApiModelsPlatformCredentialsDataProvidedBy,
)
from ..models.codat_public_api_models_platform_credentials_integration_supported_environments import (
    CodatPublicApiModelsPlatformCredentialsIntegrationSupportedEnvironments,
)
from ..models.codat_public_api_models_platform_credentials_source_type import (
    CodatPublicApiModelsPlatformCredentialsSourceType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_platform_credentials_datatype_features import (
        CodatPublicApiModelsPlatformCredentialsDatatypeFeatures,
    )


T = TypeVar("T", bound="CodatPublicApiModelsPlatformCredentialsPlatformSourceModel")


@define
class CodatPublicApiModelsPlatformCredentialsPlatformSourceModel:
    """
    Attributes:
        key (Union[Unset, None, str]):
        logo_url (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        enabled (Union[Unset, bool]):
        source_id (Union[Unset, str]):
        integration_id (Union[Unset, str]):
        source_type (Union[Unset, CodatPublicApiModelsPlatformCredentialsSourceType]):
        is_offline_connector (Union[Unset, bool]):
        is_beta (Union[Unset, bool]):
        supported_environments (Union[Unset, CodatPublicApiModelsPlatformCredentialsIntegrationSupportedEnvironments]):
        linked_connections_count (Union[Unset, int]):
        total_connections_count (Union[Unset, int]):
        data_provided_by (Union[Unset, CodatPublicApiModelsPlatformCredentialsDataProvidedBy]):
        datatype_features (Union[Unset, None, List['CodatPublicApiModelsPlatformCredentialsDatatypeFeatures']]):
    """

    key: Union[Unset, None, str] = UNSET
    logo_url: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    source_id: Union[Unset, str] = UNSET
    integration_id: Union[Unset, str] = UNSET
    source_type: Union[Unset, CodatPublicApiModelsPlatformCredentialsSourceType] = UNSET
    is_offline_connector: Union[Unset, bool] = UNSET
    is_beta: Union[Unset, bool] = UNSET
    supported_environments: Union[
        Unset, CodatPublicApiModelsPlatformCredentialsIntegrationSupportedEnvironments
    ] = UNSET
    linked_connections_count: Union[Unset, int] = UNSET
    total_connections_count: Union[Unset, int] = UNSET
    data_provided_by: Union[Unset, CodatPublicApiModelsPlatformCredentialsDataProvidedBy] = UNSET
    datatype_features: Union[Unset, None, List["CodatPublicApiModelsPlatformCredentialsDatatypeFeatures"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        logo_url = self.logo_url
        name = self.name
        enabled = self.enabled
        source_id = self.source_id
        integration_id = self.integration_id
        source_type: Union[Unset, str] = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        is_offline_connector = self.is_offline_connector
        is_beta = self.is_beta
        supported_environments: Union[Unset, str] = UNSET
        if not isinstance(self.supported_environments, Unset):
            supported_environments = self.supported_environments.value

        linked_connections_count = self.linked_connections_count
        total_connections_count = self.total_connections_count
        data_provided_by: Union[Unset, str] = UNSET
        if not isinstance(self.data_provided_by, Unset):
            data_provided_by = self.data_provided_by.value

        datatype_features: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.datatype_features, Unset):
            if self.datatype_features is None:
                datatype_features = None
            else:
                datatype_features = []
                for datatype_features_item_data in self.datatype_features:
                    datatype_features_item = datatype_features_item_data.to_dict()

                    datatype_features.append(datatype_features_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if integration_id is not UNSET:
            field_dict["integrationId"] = integration_id
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if is_offline_connector is not UNSET:
            field_dict["isOfflineConnector"] = is_offline_connector
        if is_beta is not UNSET:
            field_dict["isBeta"] = is_beta
        if supported_environments is not UNSET:
            field_dict["supportedEnvironments"] = supported_environments
        if linked_connections_count is not UNSET:
            field_dict["linkedConnectionsCount"] = linked_connections_count
        if total_connections_count is not UNSET:
            field_dict["totalConnectionsCount"] = total_connections_count
        if data_provided_by is not UNSET:
            field_dict["dataProvidedBy"] = data_provided_by
        if datatype_features is not UNSET:
            field_dict["datatypeFeatures"] = datatype_features

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_platform_credentials_datatype_features import (
            CodatPublicApiModelsPlatformCredentialsDatatypeFeatures,
        )

        d = src_dict.copy()
        key = d.pop("key", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        source_id = d.pop("sourceId", UNSET)

        integration_id = d.pop("integrationId", UNSET)

        _source_type = d.pop("sourceType", UNSET)
        source_type: Union[Unset, CodatPublicApiModelsPlatformCredentialsSourceType]
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = CodatPublicApiModelsPlatformCredentialsSourceType(_source_type)

        is_offline_connector = d.pop("isOfflineConnector", UNSET)

        is_beta = d.pop("isBeta", UNSET)

        _supported_environments = d.pop("supportedEnvironments", UNSET)
        supported_environments: Union[Unset, CodatPublicApiModelsPlatformCredentialsIntegrationSupportedEnvironments]
        if isinstance(_supported_environments, Unset):
            supported_environments = UNSET
        else:
            supported_environments = CodatPublicApiModelsPlatformCredentialsIntegrationSupportedEnvironments(
                _supported_environments
            )

        linked_connections_count = d.pop("linkedConnectionsCount", UNSET)

        total_connections_count = d.pop("totalConnectionsCount", UNSET)

        _data_provided_by = d.pop("dataProvidedBy", UNSET)
        data_provided_by: Union[Unset, CodatPublicApiModelsPlatformCredentialsDataProvidedBy]
        if isinstance(_data_provided_by, Unset):
            data_provided_by = UNSET
        else:
            data_provided_by = CodatPublicApiModelsPlatformCredentialsDataProvidedBy(_data_provided_by)

        datatype_features = []
        _datatype_features = d.pop("datatypeFeatures", UNSET)
        for datatype_features_item_data in _datatype_features or []:
            datatype_features_item = CodatPublicApiModelsPlatformCredentialsDatatypeFeatures.from_dict(
                datatype_features_item_data
            )

            datatype_features.append(datatype_features_item)

        codat_public_api_models_platform_credentials_platform_source_model = cls(
            key=key,
            logo_url=logo_url,
            name=name,
            enabled=enabled,
            source_id=source_id,
            integration_id=integration_id,
            source_type=source_type,
            is_offline_connector=is_offline_connector,
            is_beta=is_beta,
            supported_environments=supported_environments,
            linked_connections_count=linked_connections_count,
            total_connections_count=total_connections_count,
            data_provided_by=data_provided_by,
            datatype_features=datatype_features,
        )

        return codat_public_api_models_platform_credentials_platform_source_model
