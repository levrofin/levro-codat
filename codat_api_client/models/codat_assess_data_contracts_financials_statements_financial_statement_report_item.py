from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_financials_statements_account_category import (
        CodatAssessDataContractsFinancialsStatementsAccountCategory,
    )


T = TypeVar("T", bound="CodatAssessDataContractsFinancialsStatementsFinancialStatementReportItem")


@define
class CodatAssessDataContractsFinancialsStatementsFinancialStatementReportItem:
    """
    Attributes:
        date (Union[Unset, None, str]):
        balance (Union[Unset, float]):
        account_id (Union[Unset, None, str]):
        account_name (Union[Unset, None, str]):
        account_category (Union[Unset, CodatAssessDataContractsFinancialsStatementsAccountCategory]):
    """

    date: Union[Unset, None, str] = UNSET
    balance: Union[Unset, float] = UNSET
    account_id: Union[Unset, None, str] = UNSET
    account_name: Union[Unset, None, str] = UNSET
    account_category: Union[Unset, "CodatAssessDataContractsFinancialsStatementsAccountCategory"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        date = self.date
        balance = self.balance
        account_id = self.account_id
        account_name = self.account_name
        account_category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_category, Unset):
            account_category = self.account_category.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if balance is not UNSET:
            field_dict["balance"] = balance
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if account_category is not UNSET:
            field_dict["accountCategory"] = account_category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_financials_statements_account_category import (
            CodatAssessDataContractsFinancialsStatementsAccountCategory,
        )

        d = src_dict.copy()
        date = d.pop("date", UNSET)

        balance = d.pop("balance", UNSET)

        account_id = d.pop("accountId", UNSET)

        account_name = d.pop("accountName", UNSET)

        _account_category = d.pop("accountCategory", UNSET)
        account_category: Union[Unset, CodatAssessDataContractsFinancialsStatementsAccountCategory]
        if isinstance(_account_category, Unset):
            account_category = UNSET
        else:
            account_category = CodatAssessDataContractsFinancialsStatementsAccountCategory.from_dict(_account_category)

        codat_assess_data_contracts_financials_statements_financial_statement_report_item = cls(
            date=date,
            balance=balance,
            account_id=account_id,
            account_name=account_name,
            account_category=account_category,
        )

        return codat_assess_data_contracts_financials_statements_financial_statement_report_item
