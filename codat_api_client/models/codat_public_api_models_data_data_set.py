import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_public_api_models_data_dataset_status import CodatPublicApiModelsDataDatasetStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsDataDataSet")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsDataDataSet:
    """
    Attributes:
        id (str):
        company_id (str):
        connection_id (str):
        status (CodatPublicApiModelsDataDatasetStatus):
        requested (datetime.datetime):
        progress (int):
        is_completed (bool):
        is_errored (bool):
        dataset_logs_url (Union[Unset, None, str]):
        data_type (Union[Unset, None, str]):
        error_message (Union[Unset, None, str]):
        completed (Union[Unset, None, datetime.datetime]):
        validationinformation_url (Union[Unset, None, str]):
    """

    id: str
    company_id: str
    connection_id: str
    status: CodatPublicApiModelsDataDatasetStatus
    requested: datetime.datetime
    progress: int
    is_completed: bool
    is_errored: bool
    dataset_logs_url: Union[Unset, None, str] = UNSET
    data_type: Union[Unset, None, str] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    completed: Union[Unset, None, datetime.datetime] = UNSET
    validationinformation_url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        company_id = self.company_id
        connection_id = self.connection_id
        status = self.status.value

        requested = self.requested.isoformat()

        progress = self.progress
        is_completed = self.is_completed
        is_errored = self.is_errored
        dataset_logs_url = self.dataset_logs_url
        data_type = self.data_type
        error_message = self.error_message
        completed: Union[Unset, None, str] = UNSET
        if not isinstance(self.completed, Unset):
            completed = self.completed.isoformat() if self.completed else None

        validationinformation_url = self.validationinformation_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "companyId": company_id,
                "connectionId": connection_id,
                "status": status,
                "requested": requested,
                "progress": progress,
                "isCompleted": is_completed,
                "isErrored": is_errored,
            }
        )
        if dataset_logs_url is not UNSET:
            field_dict["datasetLogsUrl"] = dataset_logs_url
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if completed is not UNSET:
            field_dict["completed"] = completed
        if validationinformation_url is not UNSET:
            field_dict["validationinformationUrl"] = validationinformation_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        company_id = d.pop("companyId")

        connection_id = d.pop("connectionId")

        status = CodatPublicApiModelsDataDatasetStatus(d.pop("status"))

        requested = isoparse(d.pop("requested"))

        progress = d.pop("progress")

        is_completed = d.pop("isCompleted")

        is_errored = d.pop("isErrored")

        dataset_logs_url = d.pop("datasetLogsUrl", UNSET)

        data_type = d.pop("dataType", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        _completed = d.pop("completed", UNSET)
        completed: Union[Unset, None, datetime.datetime]
        if _completed is None:
            completed = None
        elif isinstance(_completed, Unset):
            completed = UNSET
        else:
            completed = isoparse(_completed)

        validationinformation_url = d.pop("validationinformationUrl", UNSET)

        codat_public_api_models_data_data_set = cls(
            id=id,
            company_id=company_id,
            connection_id=connection_id,
            status=status,
            requested=requested,
            progress=progress,
            is_completed=is_completed,
            is_errored=is_errored,
            dataset_logs_url=dataset_logs_url,
            data_type=data_type,
            error_message=error_message,
            completed=completed,
            validationinformation_url=validationinformation_url,
        )

        return codat_public_api_models_data_data_set
