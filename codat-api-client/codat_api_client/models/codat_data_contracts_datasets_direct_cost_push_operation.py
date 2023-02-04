import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_direct_cost import CodatDataContractsDatasetsDirectCost
    from ..models.codat_data_contracts_push_push_operation_change import CodatDataContractsPushPushOperationChange
    from ..models.codat_data_contracts_validation_validation_result import CodatDataContractsValidationValidationResult


T = TypeVar("T", bound="CodatDataContractsDatasetsDirectCostPushOperation")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsDirectCostPushOperation:
    """
    Attributes:
        company_id (str):
        push_operation_key (str):
        data_connection_key (str):
        requested_on_utc (datetime.datetime):
        status (str):
        status_code (int):
        changes (Union[Unset, None, List['CodatDataContractsPushPushOperationChange']]):
        data (Union[Unset, CodatDataContractsDatasetsDirectCost]):
        data_type (Union[Unset, None, str]):
        completed_on_utc (Union[Unset, None, datetime.datetime]):
        timeout_in_minutes (Union[Unset, None, int]):
        timeout_in_seconds (Union[Unset, None, int]):
        error_message (Union[Unset, None, str]):
        validation (Union[Unset, CodatDataContractsValidationValidationResult]):
    """

    company_id: str
    push_operation_key: str
    data_connection_key: str
    requested_on_utc: datetime.datetime
    status: str
    status_code: int
    changes: Union[Unset, None, List["CodatDataContractsPushPushOperationChange"]] = UNSET
    data: Union[Unset, "CodatDataContractsDatasetsDirectCost"] = UNSET
    data_type: Union[Unset, None, str] = UNSET
    completed_on_utc: Union[Unset, None, datetime.datetime] = UNSET
    timeout_in_minutes: Union[Unset, None, int] = UNSET
    timeout_in_seconds: Union[Unset, None, int] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    validation: Union[Unset, "CodatDataContractsValidationValidationResult"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        push_operation_key = self.push_operation_key
        data_connection_key = self.data_connection_key
        requested_on_utc = self.requested_on_utc.isoformat()

        status = self.status
        status_code = self.status_code
        changes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.changes, Unset):
            if self.changes is None:
                changes = None
            else:
                changes = []
                for changes_item_data in self.changes:
                    changes_item = changes_item_data.to_dict()

                    changes.append(changes_item)

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        data_type = self.data_type
        completed_on_utc: Union[Unset, None, str] = UNSET
        if not isinstance(self.completed_on_utc, Unset):
            completed_on_utc = self.completed_on_utc.isoformat() if self.completed_on_utc else None

        timeout_in_minutes = self.timeout_in_minutes
        timeout_in_seconds = self.timeout_in_seconds
        error_message = self.error_message
        validation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.validation, Unset):
            validation = self.validation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "companyId": company_id,
                "pushOperationKey": push_operation_key,
                "dataConnectionKey": data_connection_key,
                "requestedOnUtc": requested_on_utc,
                "status": status,
                "statusCode": status_code,
            }
        )
        if changes is not UNSET:
            field_dict["changes"] = changes
        if data is not UNSET:
            field_dict["data"] = data
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if completed_on_utc is not UNSET:
            field_dict["completedOnUtc"] = completed_on_utc
        if timeout_in_minutes is not UNSET:
            field_dict["timeoutInMinutes"] = timeout_in_minutes
        if timeout_in_seconds is not UNSET:
            field_dict["timeoutInSeconds"] = timeout_in_seconds
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if validation is not UNSET:
            field_dict["validation"] = validation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_direct_cost import CodatDataContractsDatasetsDirectCost
        from ..models.codat_data_contracts_push_push_operation_change import CodatDataContractsPushPushOperationChange
        from ..models.codat_data_contracts_validation_validation_result import (
            CodatDataContractsValidationValidationResult,
        )

        d = src_dict.copy()
        company_id = d.pop("companyId")

        push_operation_key = d.pop("pushOperationKey")

        data_connection_key = d.pop("dataConnectionKey")

        requested_on_utc = isoparse(d.pop("requestedOnUtc"))

        status = d.pop("status")

        status_code = d.pop("statusCode")

        changes = []
        _changes = d.pop("changes", UNSET)
        for changes_item_data in _changes or []:
            changes_item = CodatDataContractsPushPushOperationChange.from_dict(changes_item_data)

            changes.append(changes_item)

        _data = d.pop("data", UNSET)
        data: Union[Unset, CodatDataContractsDatasetsDirectCost]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CodatDataContractsDatasetsDirectCost.from_dict(_data)

        data_type = d.pop("dataType", UNSET)

        _completed_on_utc = d.pop("completedOnUtc", UNSET)
        completed_on_utc: Union[Unset, None, datetime.datetime]
        if _completed_on_utc is None:
            completed_on_utc = None
        elif isinstance(_completed_on_utc, Unset):
            completed_on_utc = UNSET
        else:
            completed_on_utc = isoparse(_completed_on_utc)

        timeout_in_minutes = d.pop("timeoutInMinutes", UNSET)

        timeout_in_seconds = d.pop("timeoutInSeconds", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        _validation = d.pop("validation", UNSET)
        validation: Union[Unset, CodatDataContractsValidationValidationResult]
        if isinstance(_validation, Unset):
            validation = UNSET
        else:
            validation = CodatDataContractsValidationValidationResult.from_dict(_validation)

        codat_data_contracts_datasets_direct_cost_push_operation = cls(
            company_id=company_id,
            push_operation_key=push_operation_key,
            data_connection_key=data_connection_key,
            requested_on_utc=requested_on_utc,
            status=status,
            status_code=status_code,
            changes=changes,
            data=data,
            data_type=data_type,
            completed_on_utc=completed_on_utc,
            timeout_in_minutes=timeout_in_minutes,
            timeout_in_seconds=timeout_in_seconds,
            error_message=error_message,
            validation=validation,
        )

        return codat_data_contracts_datasets_direct_cost_push_operation
