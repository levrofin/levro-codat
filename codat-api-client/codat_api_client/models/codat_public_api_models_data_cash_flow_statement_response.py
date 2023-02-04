import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codat_data_contracts_datasets_cash_flow_statement_reporting_basis import (
    CodatDataContractsDatasetsCashFlowStatementReportingBasis,
)
from ..models.codat_data_contracts_datasets_cash_flow_statement_reporting_data import (
    CodatDataContractsDatasetsCashFlowStatementReportingData,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_cash_flow_statement import CodatDataContractsDatasetsCashFlowStatement


T = TypeVar("T", bound="CodatPublicApiModelsDataCashFlowStatementResponse")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsDataCashFlowStatementResponse:
    """
    Attributes:
        reports (List['CodatDataContractsDatasetsCashFlowStatement']):
        report_basis (CodatDataContractsDatasetsCashFlowStatementReportingBasis):
        report_input (CodatDataContractsDatasetsCashFlowStatementReportingData):
        currency (str):
        most_recent_available_month (Union[Unset, None, datetime.datetime]):
        earliest_available_month (Union[Unset, None, datetime.datetime]):
    """

    reports: List["CodatDataContractsDatasetsCashFlowStatement"]
    report_basis: CodatDataContractsDatasetsCashFlowStatementReportingBasis
    report_input: CodatDataContractsDatasetsCashFlowStatementReportingData
    currency: str
    most_recent_available_month: Union[Unset, None, datetime.datetime] = UNSET
    earliest_available_month: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        reports = []
        for reports_item_data in self.reports:
            reports_item = reports_item_data.to_dict()

            reports.append(reports_item)

        report_basis = self.report_basis.value

        report_input = self.report_input.value

        currency = self.currency
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
                "reports": reports,
                "reportBasis": report_basis,
                "reportInput": report_input,
                "currency": currency,
            }
        )
        if most_recent_available_month is not UNSET:
            field_dict["mostRecentAvailableMonth"] = most_recent_available_month
        if earliest_available_month is not UNSET:
            field_dict["earliestAvailableMonth"] = earliest_available_month

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_cash_flow_statement import (
            CodatDataContractsDatasetsCashFlowStatement,
        )

        d = src_dict.copy()
        reports = []
        _reports = d.pop("reports")
        for reports_item_data in _reports:
            reports_item = CodatDataContractsDatasetsCashFlowStatement.from_dict(reports_item_data)

            reports.append(reports_item)

        report_basis = CodatDataContractsDatasetsCashFlowStatementReportingBasis(d.pop("reportBasis"))

        report_input = CodatDataContractsDatasetsCashFlowStatementReportingData(d.pop("reportInput"))

        currency = d.pop("currency")

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

        codat_public_api_models_data_cash_flow_statement_response = cls(
            reports=reports,
            report_basis=report_basis,
            report_input=report_input,
            currency=currency,
            most_recent_available_month=most_recent_available_month,
            earliest_available_month=earliest_available_month,
        )

        return codat_public_api_models_data_cash_flow_statement_response
