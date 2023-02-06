import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatAssessDataContractsCommonPagedReportInfo")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsCommonPagedReportInfo:
    """
    Attributes:
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):
        total_results (Union[Unset, int]):
        report_name (Union[Unset, None, str]):
        company_name (Union[Unset, None, str]):
        generated_date (Union[Unset, datetime.datetime]):
    """

    page_number: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    total_results: Union[Unset, int] = UNSET
    report_name: Union[Unset, None, str] = UNSET
    company_name: Union[Unset, None, str] = UNSET
    generated_date: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        page_number = self.page_number
        page_size = self.page_size
        total_results = self.total_results
        report_name = self.report_name
        company_name = self.company_name
        generated_date: Union[Unset, str] = UNSET
        if not isinstance(self.generated_date, Unset):
            generated_date = self.generated_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if total_results is not UNSET:
            field_dict["totalResults"] = total_results
        if report_name is not UNSET:
            field_dict["reportName"] = report_name
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if generated_date is not UNSET:
            field_dict["generatedDate"] = generated_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page_number = d.pop("pageNumber", UNSET)

        page_size = d.pop("pageSize", UNSET)

        total_results = d.pop("totalResults", UNSET)

        report_name = d.pop("reportName", UNSET)

        company_name = d.pop("companyName", UNSET)

        _generated_date = d.pop("generatedDate", UNSET)
        generated_date: Union[Unset, datetime.datetime]
        if isinstance(_generated_date, Unset):
            generated_date = UNSET
        else:
            generated_date = isoparse(_generated_date)

        codat_assess_data_contracts_common_paged_report_info = cls(
            page_number=page_number,
            page_size=page_size,
            total_results=total_results,
            report_name=report_name,
            company_name=company_name,
            generated_date=generated_date,
        )

        return codat_assess_data_contracts_common_paged_report_info
