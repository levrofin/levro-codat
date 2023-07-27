from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_cash_flow_transactions_cash_flow_report_banking_account import (
        CodatAssessDataContractsCashFlowTransactionsCashFlowReportBankingAccount,
    )


T = TypeVar("T", bound="CodatAssessDataContractsCashFlowTransactionsAccountsDataSource")


@define
class CodatAssessDataContractsCashFlowTransactionsAccountsDataSource:
    """
    Attributes:
        accounts (Union[Unset, None, List['CodatAssessDataContractsCashFlowTransactionsCashFlowReportBankingAccount']]):
    """

    accounts: Union[
        Unset, None, List["CodatAssessDataContractsCashFlowTransactionsCashFlowReportBankingAccount"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        accounts: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.accounts, Unset):
            if self.accounts is None:
                accounts = None
            else:
                accounts = []
                for accounts_item_data in self.accounts:
                    accounts_item = accounts_item_data.to_dict()

                    accounts.append(accounts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if accounts is not UNSET:
            field_dict["accounts"] = accounts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_cash_flow_transactions_cash_flow_report_banking_account import (
            CodatAssessDataContractsCashFlowTransactionsCashFlowReportBankingAccount,
        )

        d = src_dict.copy()
        accounts = []
        _accounts = d.pop("accounts", UNSET)
        for accounts_item_data in _accounts or []:
            accounts_item = CodatAssessDataContractsCashFlowTransactionsCashFlowReportBankingAccount.from_dict(
                accounts_item_data
            )

            accounts.append(accounts_item)

        codat_assess_data_contracts_cash_flow_transactions_accounts_data_source = cls(
            accounts=accounts,
        )

        return codat_assess_data_contracts_cash_flow_transactions_accounts_data_source
