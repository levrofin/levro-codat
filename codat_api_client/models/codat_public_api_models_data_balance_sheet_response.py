import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_balance_sheet import CodatDataContractsDatasetsBalanceSheet


T = TypeVar("T", bound="CodatPublicApiModelsDataBalanceSheetResponse")


@define
class CodatPublicApiModelsDataBalanceSheetResponse:
    """
    Attributes:
        currency (str):
        reports (List['CodatDataContractsDatasetsBalanceSheet']):
        most_recent_available_month (Union[Unset, None, datetime.datetime]):
        earliest_available_month (Union[Unset, None, datetime.datetime]):
    """

    currency: str
    reports: List["CodatDataContractsDatasetsBalanceSheet"]
    most_recent_available_month: Union[Unset, None, datetime.datetime] = UNSET
    earliest_available_month: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency
        reports = []
        for reports_item_data in self.reports:
            reports_item = reports_item_data.to_dict()

            reports.append(reports_item)

        most_recent_available_month: Union[Unset, None, str] = UNSET
        if not isinstance(self.most_recent_available_month, Unset):
            most_recent_available_month = (
                self.most_recent_available_month.isoformat() if self.most_recent_available_month else None
            )

        earliest_available_month: Union[Unset, None, str] = UNSET
        if not isinstance(self.earliest_available_month, Unset):
            earliest_available_month = (
                self.earliest_available_month.isoformat() if self.earliest_available_month else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "currency": currency,
                "reports": reports,
            }
        )
        if most_recent_available_month is not UNSET:
            field_dict["mostRecentAvailableMonth"] = most_recent_available_month
        if earliest_available_month is not UNSET:
            field_dict["earliestAvailableMonth"] = earliest_available_month

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_balance_sheet import CodatDataContractsDatasetsBalanceSheet

        d = src_dict.copy()
        currency = d.pop("currency")

        reports = []
        _reports = d.pop("reports")
        for reports_item_data in _reports:
            reports_item = CodatDataContractsDatasetsBalanceSheet.from_dict(reports_item_data)

            reports.append(reports_item)

        _most_recent_available_month = d.pop("mostRecentAvailableMonth", UNSET)
        most_recent_available_month: Union[Unset, None, datetime.datetime]
        if _most_recent_available_month is None:
            most_recent_available_month = None
        elif isinstance(_most_recent_available_month, Unset):
            most_recent_available_month = UNSET
        else:
            most_recent_available_month = isoparse(_most_recent_available_month)

        _earliest_available_month = d.pop("earliestAvailableMonth", UNSET)
        earliest_available_month: Union[Unset, None, datetime.datetime]
        if _earliest_available_month is None:
            earliest_available_month = None
        elif isinstance(_earliest_available_month, Unset):
            earliest_available_month = UNSET
        else:
            earliest_available_month = isoparse(_earliest_available_month)

        codat_public_api_models_data_balance_sheet_response = cls(
            currency=currency,
            reports=reports,
            most_recent_available_month=most_recent_available_month,
            earliest_available_month=earliest_available_month,
        )

        return codat_public_api_models_data_balance_sheet_response
