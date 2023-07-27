import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_company_company_event_stream_item import (
        CodatPublicApiModelsCompanyCompanyEventStreamItem,
    )


T = TypeVar("T", bound="CodatPublicApiModelsCompanyCompanyEventStream")


@define
class CodatPublicApiModelsCompanyCompanyEventStream:
    """
    Attributes:
        company_id (str):
        data (List['CodatPublicApiModelsCompanyCompanyEventStreamItem']):
        from_ (Union[Unset, None, datetime.datetime]):
        to (Union[Unset, None, datetime.datetime]):
    """

    company_id: str
    data: List["CodatPublicApiModelsCompanyCompanyEventStreamItem"]
    from_: Union[Unset, None, datetime.datetime] = UNSET
    to: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        from_: Union[Unset, None, str] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat() if self.from_ else None

        to: Union[Unset, None, str] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat() if self.to else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "companyId": company_id,
                "data": data,
            }
        )
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_company_company_event_stream_item import (
            CodatPublicApiModelsCompanyCompanyEventStreamItem,
        )

        d = src_dict.copy()
        company_id = d.pop("companyId")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = CodatPublicApiModelsCompanyCompanyEventStreamItem.from_dict(data_item_data)

            data.append(data_item)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, None, datetime.datetime]
        if _from_ is None:
            from_ = None
        elif isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _to = d.pop("to", UNSET)
        to: Union[Unset, None, datetime.datetime]
        if _to is None:
            to = None
        elif isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        codat_public_api_models_company_company_event_stream = cls(
            company_id=company_id,
            data=data,
            from_=from_,
            to=to,
        )

        return codat_public_api_models_company_company_event_stream
