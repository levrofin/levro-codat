import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsFileMetadataModel")


@define
class CodatPublicApiModelsFileMetadataModel:
    """
    Attributes:
        file_name (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        source_type (Union[Unset, None, str]):
        uploaded (Union[Unset, datetime.datetime]):
    """

    file_name: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    source_type: Union[Unset, None, str] = UNSET
    uploaded: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        file_name = self.file_name
        display_name = self.display_name
        source_type = self.source_type
        uploaded: Union[Unset, str] = UNSET
        if not isinstance(self.uploaded, Unset):
            uploaded = self.uploaded.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if uploaded is not UNSET:
            field_dict["uploaded"] = uploaded

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_name = d.pop("fileName", UNSET)

        display_name = d.pop("displayName", UNSET)

        source_type = d.pop("sourceType", UNSET)

        _uploaded = d.pop("uploaded", UNSET)
        uploaded: Union[Unset, datetime.datetime]
        if isinstance(_uploaded, Unset):
            uploaded = UNSET
        else:
            uploaded = isoparse(_uploaded)

        codat_public_api_models_file_metadata_model = cls(
            file_name=file_name,
            display_name=display_name,
            source_type=source_type,
            uploaded=uploaded,
        )

        return codat_public_api_models_file_metadata_model
