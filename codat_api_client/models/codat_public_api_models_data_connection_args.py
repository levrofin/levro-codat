from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_data_connection_args_connection_info import (
        CodatPublicApiModelsDataConnectionArgsConnectionInfo,
    )


T = TypeVar("T", bound="CodatPublicApiModelsDataConnectionArgs")


@define
class CodatPublicApiModelsDataConnectionArgs:
    """
    Attributes:
        platform_key (Union[Unset, None, str]):
        connection_info (Union[Unset, None, CodatPublicApiModelsDataConnectionArgsConnectionInfo]):
    """

    platform_key: Union[Unset, None, str] = UNSET
    connection_info: Union[Unset, None, "CodatPublicApiModelsDataConnectionArgsConnectionInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        platform_key = self.platform_key
        connection_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.connection_info, Unset):
            connection_info = self.connection_info.to_dict() if self.connection_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if platform_key is not UNSET:
            field_dict["platformKey"] = platform_key
        if connection_info is not UNSET:
            field_dict["connectionInfo"] = connection_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_data_connection_args_connection_info import (
            CodatPublicApiModelsDataConnectionArgsConnectionInfo,
        )

        d = src_dict.copy()
        platform_key = d.pop("platformKey", UNSET)

        _connection_info = d.pop("connectionInfo", UNSET)
        connection_info: Union[Unset, None, CodatPublicApiModelsDataConnectionArgsConnectionInfo]
        if _connection_info is None:
            connection_info = None
        elif isinstance(_connection_info, Unset):
            connection_info = UNSET
        else:
            connection_info = CodatPublicApiModelsDataConnectionArgsConnectionInfo.from_dict(_connection_info)

        codat_public_api_models_data_connection_args = cls(
            platform_key=platform_key,
            connection_info=connection_info,
        )

        return codat_public_api_models_data_connection_args
