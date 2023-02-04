import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsCompanyDataConnectionError")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsCompanyDataConnectionError:
    """
    Attributes:
        status_code (Union[Unset, None, str]):
        status_text (Union[Unset, None, str]):
        error_message (Union[Unset, None, str]):
        errored_on_utc (Union[Unset, datetime.datetime]):
    """

    status_code: Union[Unset, None, str] = UNSET
    status_text: Union[Unset, None, str] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    errored_on_utc: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status_code = self.status_code
        status_text = self.status_text
        error_message = self.error_message
        errored_on_utc: Union[Unset, str] = UNSET
        if not isinstance(self.errored_on_utc, Unset):
            errored_on_utc = self.errored_on_utc.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if status_text is not UNSET:
            field_dict["statusText"] = status_text
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if errored_on_utc is not UNSET:
            field_dict["erroredOnUtc"] = errored_on_utc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status_code = d.pop("statusCode", UNSET)

        status_text = d.pop("statusText", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        _errored_on_utc = d.pop("erroredOnUtc", UNSET)
        errored_on_utc: Union[Unset, datetime.datetime]
        if isinstance(_errored_on_utc, Unset):
            errored_on_utc = UNSET
        else:
            errored_on_utc = isoparse(_errored_on_utc)

        codat_public_api_models_company_data_connection_error = cls(
            status_code=status_code,
            status_text=status_text,
            error_message=error_message,
            errored_on_utc=errored_on_utc,
        )

        return codat_public_api_models_company_data_connection_error
