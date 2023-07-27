from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_company_patch_data_connection_model_connection_info import (
        CodatPublicApiModelsCompanyPatchDataConnectionModelConnectionInfo,
    )


T = TypeVar("T", bound="CodatPublicApiModelsCompanyPatchDataConnectionModel")


@define
class CodatPublicApiModelsCompanyPatchDataConnectionModel:
    """
    Attributes:
        status (Union[Unset, None, str]):
        connection_info (Union[Unset, None, CodatPublicApiModelsCompanyPatchDataConnectionModelConnectionInfo]):
    """

    status: Union[Unset, None, str] = UNSET
    connection_info: Union[Unset, None, "CodatPublicApiModelsCompanyPatchDataConnectionModelConnectionInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        connection_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.connection_info, Unset):
            connection_info = self.connection_info.to_dict() if self.connection_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if connection_info is not UNSET:
            field_dict["connectionInfo"] = connection_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_company_patch_data_connection_model_connection_info import (
            CodatPublicApiModelsCompanyPatchDataConnectionModelConnectionInfo,
        )

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        _connection_info = d.pop("connectionInfo", UNSET)
        connection_info: Union[Unset, None, CodatPublicApiModelsCompanyPatchDataConnectionModelConnectionInfo]
        if _connection_info is None:
            connection_info = None
        elif isinstance(_connection_info, Unset):
            connection_info = UNSET
        else:
            connection_info = CodatPublicApiModelsCompanyPatchDataConnectionModelConnectionInfo.from_dict(
                _connection_info
            )

        codat_public_api_models_company_patch_data_connection_model = cls(
            status=status,
            connection_info=connection_info,
        )

        return codat_public_api_models_company_patch_data_connection_model
