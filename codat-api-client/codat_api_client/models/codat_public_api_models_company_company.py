import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_company_data_connection import CodatPublicApiModelsCompanyDataConnection


T = TypeVar("T", bound="CodatPublicApiModelsCompanyCompany")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsCompanyCompany:
    """
    Attributes:
        id (str):
        name (str):
        platform (str):
        redirect (str):
        data_connections (List['CodatPublicApiModelsCompanyDataConnection']):
        description (Union[Unset, None, str]):
        last_sync (Union[Unset, None, datetime.datetime]):
        created (Union[Unset, None, datetime.datetime]):
        created_by_user_name (Union[Unset, None, str]):
    """

    id: str
    name: str
    platform: str
    redirect: str
    data_connections: List["CodatPublicApiModelsCompanyDataConnection"]
    description: Union[Unset, None, str] = UNSET
    last_sync: Union[Unset, None, datetime.datetime] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    created_by_user_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        platform = self.platform
        redirect = self.redirect
        data_connections = []
        for data_connections_item_data in self.data_connections:
            data_connections_item = data_connections_item_data.to_dict()

            data_connections.append(data_connections_item)

        description = self.description
        last_sync: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_sync, Unset):
            last_sync = self.last_sync.isoformat() if self.last_sync else None

        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        created_by_user_name = self.created_by_user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
                "platform": platform,
                "redirect": redirect,
                "dataConnections": data_connections,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if last_sync is not UNSET:
            field_dict["lastSync"] = last_sync
        if created is not UNSET:
            field_dict["created"] = created
        if created_by_user_name is not UNSET:
            field_dict["createdByUserName"] = created_by_user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_company_data_connection import CodatPublicApiModelsCompanyDataConnection

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        platform = d.pop("platform")

        redirect = d.pop("redirect")

        data_connections = []
        _data_connections = d.pop("dataConnections")
        for data_connections_item_data in _data_connections:
            data_connections_item = CodatPublicApiModelsCompanyDataConnection.from_dict(data_connections_item_data)

            data_connections.append(data_connections_item)

        description = d.pop("description", UNSET)

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

        created_by_user_name = d.pop("createdByUserName", UNSET)

        codat_public_api_models_company_company = cls(
            id=id,
            name=name,
            platform=platform,
            redirect=redirect,
            data_connections=data_connections,
            description=description,
            last_sync=last_sync,
            created=created,
            created_by_user_name=created_by_user_name,
        )

        return codat_public_api_models_company_company
