import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsRulesAlertModel")


@define
class CodatPublicApiModelsRulesAlertModel:
    """
    Attributes:
        company_id (Union[Unset, str]):
        company_name (Union[Unset, None, str]):
        client_id (Union[Unset, str]):
        client_name (Union[Unset, None, str]):
        rule_id (Union[Unset, str]):
        rule_type (Union[Unset, None, str]):
        id (Union[Unset, str]):
        alert_id (Union[Unset, str]):
        data_connection_id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        data (Union[Unset, Any]):
        raised_on_utc (Union[Unset, datetime.datetime]):
    """

    company_id: Union[Unset, str] = UNSET
    company_name: Union[Unset, None, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    client_name: Union[Unset, None, str] = UNSET
    rule_id: Union[Unset, str] = UNSET
    rule_type: Union[Unset, None, str] = UNSET
    id: Union[Unset, str] = UNSET
    alert_id: Union[Unset, str] = UNSET
    data_connection_id: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    data: Union[Unset, Any] = UNSET
    raised_on_utc: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        company_name = self.company_name
        client_id = self.client_id
        client_name = self.client_name
        rule_id = self.rule_id
        rule_type = self.rule_type
        id = self.id
        alert_id = self.alert_id
        data_connection_id = self.data_connection_id
        message = self.message
        data = self.data
        raised_on_utc: Union[Unset, str] = UNSET
        if not isinstance(self.raised_on_utc, Unset):
            raised_on_utc = self.raised_on_utc.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if client_name is not UNSET:
            field_dict["clientName"] = client_name
        if rule_id is not UNSET:
            field_dict["ruleId"] = rule_id
        if rule_type is not UNSET:
            field_dict["ruleType"] = rule_type
        if id is not UNSET:
            field_dict["id"] = id
        if alert_id is not UNSET:
            field_dict["alertId"] = alert_id
        if data_connection_id is not UNSET:
            field_dict["dataConnectionId"] = data_connection_id
        if message is not UNSET:
            field_dict["message"] = message
        if data is not UNSET:
            field_dict["data"] = data
        if raised_on_utc is not UNSET:
            field_dict["raisedOnUtc"] = raised_on_utc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        company_id = d.pop("companyId", UNSET)

        company_name = d.pop("companyName", UNSET)

        client_id = d.pop("clientId", UNSET)

        client_name = d.pop("clientName", UNSET)

        rule_id = d.pop("ruleId", UNSET)

        rule_type = d.pop("ruleType", UNSET)

        id = d.pop("id", UNSET)

        alert_id = d.pop("alertId", UNSET)

        data_connection_id = d.pop("dataConnectionId", UNSET)

        message = d.pop("message", UNSET)

        data = d.pop("data", UNSET)

        _raised_on_utc = d.pop("raisedOnUtc", UNSET)
        raised_on_utc: Union[Unset, datetime.datetime]
        if isinstance(_raised_on_utc, Unset):
            raised_on_utc = UNSET
        else:
            raised_on_utc = isoparse(_raised_on_utc)

        codat_public_api_models_rules_alert_model = cls(
            company_id=company_id,
            company_name=company_name,
            client_id=client_id,
            client_name=client_name,
            rule_id=rule_id,
            rule_type=rule_type,
            id=id,
            alert_id=alert_id,
            data_connection_id=data_connection_id,
            message=message,
            data=data,
            raised_on_utc=raised_on_utc,
        )

        return codat_public_api_models_rules_alert_model
