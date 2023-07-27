from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_financials_statements_financial_statement_report_info import (
        CodatAssessDataContractsFinancialsStatementsFinancialStatementReportInfo,
    )
    from ..models.codat_assess_data_contracts_financials_statements_financial_statement_report_item import (
        CodatAssessDataContractsFinancialsStatementsFinancialStatementReportItem,
    )


T = TypeVar("T", bound="CodatAssessDataContractsFinancialsStatementsEnhancedFinancialStatement")


@define
class CodatAssessDataContractsFinancialsStatementsEnhancedFinancialStatement:
    """
    Attributes:
        report_info (Union[Unset, CodatAssessDataContractsFinancialsStatementsFinancialStatementReportInfo]):
        report_items (Union[Unset, None,
            List['CodatAssessDataContractsFinancialsStatementsFinancialStatementReportItem']]):
    """

    report_info: Union[Unset, "CodatAssessDataContractsFinancialsStatementsFinancialStatementReportInfo"] = UNSET
    report_items: Union[
        Unset, None, List["CodatAssessDataContractsFinancialsStatementsFinancialStatementReportItem"]
    ] = UNSET

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
        from ..models.codat_assess_data_contracts_financials_statements_financial_statement_report_info import (
            CodatAssessDataContractsFinancialsStatementsFinancialStatementReportInfo,
        )
        from ..models.codat_assess_data_contracts_financials_statements_financial_statement_report_item import (
            CodatAssessDataContractsFinancialsStatementsFinancialStatementReportItem,
        )

        d = src_dict.copy()
        _report_info = d.pop("reportInfo", UNSET)
        report_info: Union[Unset, CodatAssessDataContractsFinancialsStatementsFinancialStatementReportInfo]
        if isinstance(_report_info, Unset):
            report_info = UNSET
        else:
            report_info = CodatAssessDataContractsFinancialsStatementsFinancialStatementReportInfo.from_dict(
                _report_info
            )

        report_items = []
        _report_items = d.pop("reportItems", UNSET)
        for report_items_item_data in _report_items or []:
            report_items_item = CodatAssessDataContractsFinancialsStatementsFinancialStatementReportItem.from_dict(
                report_items_item_data
            )

            report_items.append(report_items_item)

        codat_assess_data_contracts_financials_statements_enhanced_financial_statement = cls(
            report_info=report_info,
            report_items=report_items,
        )

        return codat_assess_data_contracts_financials_statements_enhanced_financial_statement
