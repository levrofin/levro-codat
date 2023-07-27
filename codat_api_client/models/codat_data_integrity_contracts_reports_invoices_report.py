from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_common_paged_report_info import (
        CodatAssessDataContractsCommonPagedReportInfo,
    )
    from ..models.codat_data_integrity_contracts_reports_invoice import CodatDataIntegrityContractsReportsInvoice


T = TypeVar("T", bound="CodatDataIntegrityContractsReportsInvoicesReport")


@define
class CodatDataIntegrityContractsReportsInvoicesReport:
    """
    Attributes:
        report_info (Union[Unset, CodatAssessDataContractsCommonPagedReportInfo]):
        report_items (Union[Unset, None, List['CodatDataIntegrityContractsReportsInvoice']]):
    """

    report_info: Union[Unset, "CodatAssessDataContractsCommonPagedReportInfo"] = UNSET
    report_items: Union[Unset, None, List["CodatDataIntegrityContractsReportsInvoice"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        report_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.report_info, Unset):
            report_info = self.report_info.to_dict()

        report_items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.report_items, Unset):
            if self.report_items is None:
                report_items = None
            else:
                report_items = []
                for report_items_item_data in self.report_items:
                    report_items_item = report_items_item_data.to_dict()

                    report_items.append(report_items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if report_info is not UNSET:
            field_dict["reportInfo"] = report_info
        if report_items is not UNSET:
            field_dict["reportItems"] = report_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_common_paged_report_info import (
            CodatAssessDataContractsCommonPagedReportInfo,
        )
        from ..models.codat_data_integrity_contracts_reports_invoice import CodatDataIntegrityContractsReportsInvoice

        d = src_dict.copy()
        _report_info = d.pop("reportInfo", UNSET)
        report_info: Union[Unset, CodatAssessDataContractsCommonPagedReportInfo]
        if isinstance(_report_info, Unset):
            report_info = UNSET
        else:
            report_info = CodatAssessDataContractsCommonPagedReportInfo.from_dict(_report_info)

        report_items = []
        _report_items = d.pop("reportItems", UNSET)
        for report_items_item_data in _report_items or []:
            report_items_item = CodatDataIntegrityContractsReportsInvoice.from_dict(report_items_item_data)

            report_items.append(report_items_item)

        codat_data_integrity_contracts_reports_invoices_report = cls(
            report_info=report_info,
            report_items=report_items,
        )

        return codat_data_integrity_contracts_reports_invoices_report
