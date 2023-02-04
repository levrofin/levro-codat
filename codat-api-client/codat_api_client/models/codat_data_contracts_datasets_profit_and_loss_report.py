import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_report_line import CodatDataContractsDatasetsReportLine


T = TypeVar("T", bound="CodatDataContractsDatasetsProfitAndLossReport")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsProfitAndLossReport:
    """
    Attributes:
        gross_profit (float):
        net_operating_profit (float):
        net_other_income (float):
        net_profit (float):
        from_date (Union[Unset, datetime.datetime]):
        to_date (Union[Unset, datetime.datetime]):
        income (Union[Unset, CodatDataContractsDatasetsReportLine]):
        cost_of_sales (Union[Unset, CodatDataContractsDatasetsReportLine]):
        expenses (Union[Unset, CodatDataContractsDatasetsReportLine]):
        other_expenses (Union[Unset, CodatDataContractsDatasetsReportLine]):
        other_income (Union[Unset, CodatDataContractsDatasetsReportLine]):
    """

    gross_profit: float
    net_operating_profit: float
    net_other_income: float
    net_profit: float
    from_date: Union[Unset, datetime.datetime] = UNSET
    to_date: Union[Unset, datetime.datetime] = UNSET
    income: Union[Unset, "CodatDataContractsDatasetsReportLine"] = UNSET
    cost_of_sales: Union[Unset, "CodatDataContractsDatasetsReportLine"] = UNSET
    expenses: Union[Unset, "CodatDataContractsDatasetsReportLine"] = UNSET
    other_expenses: Union[Unset, "CodatDataContractsDatasetsReportLine"] = UNSET
    other_income: Union[Unset, "CodatDataContractsDatasetsReportLine"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        gross_profit = self.gross_profit
        net_operating_profit = self.net_operating_profit
        net_other_income = self.net_other_income
        net_profit = self.net_profit
        from_date: Union[Unset, str] = UNSET
        if not isinstance(self.from_date, Unset):
            from_date = self.from_date.isoformat()

        to_date: Union[Unset, str] = UNSET
        if not isinstance(self.to_date, Unset):
            to_date = self.to_date.isoformat()

        income: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.income, Unset):
            income = self.income.to_dict()

        cost_of_sales: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cost_of_sales, Unset):
            cost_of_sales = self.cost_of_sales.to_dict()

        expenses: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.expenses, Unset):
            expenses = self.expenses.to_dict()

        other_expenses: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.other_expenses, Unset):
            other_expenses = self.other_expenses.to_dict()

        other_income: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.other_income, Unset):
            other_income = self.other_income.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "grossProfit": gross_profit,
                "netOperatingProfit": net_operating_profit,
                "netOtherIncome": net_other_income,
                "netProfit": net_profit,
            }
        )
        if from_date is not UNSET:
            field_dict["fromDate"] = from_date
        if to_date is not UNSET:
            field_dict["toDate"] = to_date
        if income is not UNSET:
            field_dict["income"] = income
        if cost_of_sales is not UNSET:
            field_dict["costOfSales"] = cost_of_sales
        if expenses is not UNSET:
            field_dict["expenses"] = expenses
        if other_expenses is not UNSET:
            field_dict["otherExpenses"] = other_expenses
        if other_income is not UNSET:
            field_dict["otherIncome"] = other_income

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_report_line import CodatDataContractsDatasetsReportLine

        d = src_dict.copy()
        gross_profit = d.pop("grossProfit")

        net_operating_profit = d.pop("netOperatingProfit")

        net_other_income = d.pop("netOtherIncome")

        net_profit = d.pop("netProfit")

        _from_date = d.pop("fromDate", UNSET)
        from_date: Union[Unset, datetime.datetime]
        if isinstance(_from_date, Unset):
            from_date = UNSET
        else:
            from_date = isoparse(_from_date)

        _to_date = d.pop("toDate", UNSET)
        to_date: Union[Unset, datetime.datetime]
        if isinstance(_to_date, Unset):
            to_date = UNSET
        else:
            to_date = isoparse(_to_date)

        _income = d.pop("income", UNSET)
        income: Union[Unset, CodatDataContractsDatasetsReportLine]
        if isinstance(_income, Unset):
            income = UNSET
        else:
            income = CodatDataContractsDatasetsReportLine.from_dict(_income)

        _cost_of_sales = d.pop("costOfSales", UNSET)
        cost_of_sales: Union[Unset, CodatDataContractsDatasetsReportLine]
        if isinstance(_cost_of_sales, Unset):
            cost_of_sales = UNSET
        else:
            cost_of_sales = CodatDataContractsDatasetsReportLine.from_dict(_cost_of_sales)

        _expenses = d.pop("expenses", UNSET)
        expenses: Union[Unset, CodatDataContractsDatasetsReportLine]
        if isinstance(_expenses, Unset):
            expenses = UNSET
        else:
            expenses = CodatDataContractsDatasetsReportLine.from_dict(_expenses)

        _other_expenses = d.pop("otherExpenses", UNSET)
        other_expenses: Union[Unset, CodatDataContractsDatasetsReportLine]
        if isinstance(_other_expenses, Unset):
            other_expenses = UNSET
        else:
            other_expenses = CodatDataContractsDatasetsReportLine.from_dict(_other_expenses)

        _other_income = d.pop("otherIncome", UNSET)
        other_income: Union[Unset, CodatDataContractsDatasetsReportLine]
        if isinstance(_other_income, Unset):
            other_income = UNSET
        else:
            other_income = CodatDataContractsDatasetsReportLine.from_dict(_other_income)

        codat_data_contracts_datasets_profit_and_loss_report = cls(
            gross_profit=gross_profit,
            net_operating_profit=net_operating_profit,
            net_other_income=net_other_income,
            net_profit=net_profit,
            from_date=from_date,
            to_date=to_date,
            income=income,
            cost_of_sales=cost_of_sales,
            expenses=expenses,
            other_expenses=other_expenses,
            other_income=other_income,
        )

        return codat_data_contracts_datasets_profit_and_loss_report
