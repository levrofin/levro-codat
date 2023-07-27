from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_cash_flow_transactions_accounts_data_source import (
        CodatAssessDataContractsCashFlowTransactionsAccountsDataSource,
    )
    from ..models.codat_assess_data_contracts_cash_flow_transactions_transactions_data_source import (
        CodatAssessDataContractsCashFlowTransactionsTransactionsDataSource,
    )
    from ..models.codat_assess_data_contracts_common_paged_report_info import (
        CodatAssessDataContractsCommonPagedReportInfo,
    )


T = TypeVar("T", bound="CodatAssessDataContractsCashFlowTransactionsCashFlowTransactionsReport")


@define
class CodatAssessDataContractsCashFlowTransactionsCashFlowTransactionsReport:
    """
    Attributes:
        report_info (Union[Unset, CodatAssessDataContractsCommonPagedReportInfo]):
        data_sources (Union[Unset, None, List['CodatAssessDataContractsCashFlowTransactionsAccountsDataSource']]):
        report_items (Union[Unset, None, List['CodatAssessDataContractsCashFlowTransactionsTransactionsDataSource']]):
    """

    report_info: Union[Unset, "CodatAssessDataContractsCommonPagedReportInfo"] = UNSET
    data_sources: Union[Unset, None, List["CodatAssessDataContractsCashFlowTransactionsAccountsDataSource"]] = UNSET
    report_items: Union[Unset, None, List["CodatAssessDataContractsCashFlowTransactionsTransactionsDataSource"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        report_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.report_info, Unset):
            report_info = self.report_info.to_dict()

        data_sources: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data_sources, Unset):
            if self.data_sources is None:
                data_sources = None
            else:
                data_sources = []
                for data_sources_item_data in self.data_sources:
                    data_sources_item = data_sources_item_data.to_dict()

                    data_sources.append(data_sources_item)

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
        if data_sources is not UNSET:
            field_dict["dataSources"] = data_sources
        if report_items is not UNSET:
            field_dict["reportItems"] = report_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_cash_flow_transactions_accounts_data_source import (
            CodatAssessDataContractsCashFlowTransactionsAccountsDataSource,
        )
        from ..models.codat_assess_data_contracts_cash_flow_transactions_transactions_data_source import (
            CodatAssessDataContractsCashFlowTransactionsTransactionsDataSource,
        )
        from ..models.codat_assess_data_contracts_common_paged_report_info import (
            CodatAssessDataContractsCommonPagedReportInfo,
        )

        d = src_dict.copy()
        _report_info = d.pop("reportInfo", UNSET)
        report_info: Union[Unset, CodatAssessDataContractsCommonPagedReportInfo]
        if isinstance(_report_info, Unset):
            report_info = UNSET
        else:
            report_info = CodatAssessDataContractsCommonPagedReportInfo.from_dict(_report_info)

        data_sources = []
        _data_sources = d.pop("dataSources", UNSET)
        for data_sources_item_data in _data_sources or []:
            data_sources_item = CodatAssessDataContractsCashFlowTransactionsAccountsDataSource.from_dict(
                data_sources_item_data
            )

            data_sources.append(data_sources_item)

        report_items = []
        _report_items = d.pop("reportItems", UNSET)
        for report_items_item_data in _report_items or []:
            report_items_item = CodatAssessDataContractsCashFlowTransactionsTransactionsDataSource.from_dict(
                report_items_item_data
            )

            report_items.append(report_items_item)

        codat_assess_data_contracts_cash_flow_transactions_cash_flow_transactions_report = cls(
            report_info=report_info,
            data_sources=data_sources,
            report_items=report_items,
        )

        return codat_assess_data_contracts_cash_flow_transactions_cash_flow_transactions_report
