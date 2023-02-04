import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_company_data_connection_connection_info import (
        CodatPublicApiModelsCompanyDataConnectionConnectionInfo,
    )
    from ..models.codat_public_api_models_company_data_connection_error import (
        CodatPublicApiModelsCompanyDataConnectionError,
    )


T = TypeVar("T", bound="CodatPublicApiModelsCompanyDataConnection")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsCompanyDataConnection:
    """
    Attributes:
        id (str):
        integration_id (str):
        source_id (str):
        platform_name (str):
        link_url (str):
        integration_key (Union[Unset, None, str]):
        status (Union[Unset, None, str]):
        last_sync (Union[Unset, None, datetime.datetime]):
        created (Union[Unset, None, datetime.datetime]):
        source_type (Union[Unset, None, str]):
        data_connection_errors (Union[Unset, None, List['CodatPublicApiModelsCompanyDataConnectionError']]):
        connection_info (Union[Unset, None, CodatPublicApiModelsCompanyDataConnectionConnectionInfo]):
    """

    id: str
    integration_id: str
    source_id: str
    platform_name: str
    link_url: str
    integration_key: Union[Unset, None, str] = UNSET
    status: Union[Unset, None, str] = UNSET
    last_sync: Union[Unset, None, datetime.datetime] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    source_type: Union[Unset, None, str] = UNSET
    data_connection_errors: Union[Unset, None, List["CodatPublicApiModelsCompanyDataConnectionError"]] = UNSET
    connection_info: Union[Unset, None, "CodatPublicApiModelsCompanyDataConnectionConnectionInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        integration_id = self.integration_id
        source_id = self.source_id
        platform_name = self.platform_name
        link_url = self.link_url
        integration_key = self.integration_key
        status = self.status
        last_sync: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_sync, Unset):
            last_sync = self.last_sync.isoformat() if self.last_sync else None

        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        source_type = self.source_type
        data_connection_errors: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data_connection_errors, Unset):
            if self.data_connection_errors is None:
                data_connection_errors = None
            else:
                data_connection_errors = []
                for data_connection_errors_item_data in self.data_connection_errors:
                    data_connection_errors_item = data_connection_errors_item_data.to_dict()

                    data_connection_errors.append(data_connection_errors_item)

        connection_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.connection_info, Unset):
            connection_info = self.connection_info.to_dict() if self.connection_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "integrationId": integration_id,
                "sourceId": source_id,
                "platformName": platform_name,
                "linkUrl": link_url,
            }
        )
        if integration_key is not UNSET:
            field_dict["integrationKey"] = integration_key
        if status is not UNSET:
            field_dict["status"] = status
        if last_sync is not UNSET:
            field_dict["lastSync"] = last_sync
        if created is not UNSET:
            field_dict["created"] = created
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if data_connection_errors is not UNSET:
            field_dict["dataConnectionErrors"] = data_connection_errors
        if connection_info is not UNSET:
            field_dict["connectionInfo"] = connection_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_company_data_connection_connection_info import (
            CodatPublicApiModelsCompanyDataConnectionConnectionInfo,
        )
        from ..models.codat_public_api_models_company_data_connection_error import (
            CodatPublicApiModelsCompanyDataConnectionError,
        )

        d = src_dict.copy()
        id = d.pop("id")

        integration_id = d.pop("integrationId")

        source_id = d.pop("sourceId")

        platform_name = d.pop("platformName")

        link_url = d.pop("linkUrl")

        integration_key = d.pop("integrationKey", UNSET)

        status = d.pop("status", UNSET)

        _last_sync = d.pop("lastSync", UNSET)
        last_sync: Union[Unset, None, datetime.datetime]
        if _last_sync is None:
            last_sync = None
        elif isinstance(_last_sync, Unset):
            last_sync = UNSET
        else:
            last_sync = isoparse(_last_sync)

        _created = d.pop("created", UNSET)
        created: Union[Unset, None, datetime.datetime]
        if _created is None:
            created = None
        elif isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        source_type = d.pop("sourceType", UNSET)

        data_connection_errors = []
        _data_connection_errors = d.pop("dataConnectionErrors", UNSET)
        for data_connection_errors_item_data in _data_connection_errors or []:
            data_connection_errors_item = CodatPublicApiModelsCompanyDataConnectionError.from_dict(
                data_connection_errors_item_data
            )

            data_connection_errors.append(data_connection_errors_item)

        _connection_info = d.pop("connectionInfo", UNSET)
        connection_info: Union[Unset, None, CodatPublicApiModelsCompanyDataConnectionConnectionInfo]
        if _connection_info is None:
            connection_info = None
        elif isinstance(_connection_info, Unset):
            connection_info = UNSET
        else:
            connection_info = CodatPublicApiModelsCompanyDataConnectionConnectionInfo.from_dict(_connection_info)

        codat_public_api_models_company_data_connection = cls(
            id=id,
            integration_id=integration_id,
            source_id=source_id,
            platform_name=platform_name,
            link_url=link_url,
            integration_key=integration_key,
            status=status,
            last_sync=last_sync,
            created=created,
            source_type=source_type,
            data_connection_errors=data_connection_errors,
            connection_info=connection_info,
        )

        return codat_public_api_models_company_data_connection
