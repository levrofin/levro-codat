from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_cash_flow_transactions_cash_flow_report_banking_transaction import (
        CodatAssessDataContractsCashFlowTransactionsCashFlowReportBankingTransaction,
    )


T = TypeVar("T", bound="CodatAssessDataContractsCashFlowTransactionsTransactionsDataSource")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsCashFlowTransactionsTransactionsDataSource:
    """
    Attributes:
        transactions (Union[Unset, None,
            List['CodatAssessDataContractsCashFlowTransactionsCashFlowReportBankingTransaction']]):
    """

    transactions: Union[
        Unset, None, List["CodatAssessDataContractsCashFlowTransactionsCashFlowReportBankingTransaction"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        transactions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transactions, Unset):
            if self.transactions is None:
                transactions = None
            else:
                transactions = []
                for transactions_item_data in self.transactions:
                    transactions_item = transactions_item_data.to_dict()

                    transactions.append(transactions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if transactions is not UNSET:
            field_dict["transactions"] = transactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_cash_flow_transactions_cash_flow_report_banking_transaction import (
            CodatAssessDataContractsCashFlowTransactionsCashFlowReportBankingTransaction,
        )

        d = src_dict.copy()
        transactions = []
        _transactions = d.pop("transactions", UNSET)
        for transactions_item_data in _transactions or []:
            transactions_item = CodatAssessDataContractsCashFlowTransactionsCashFlowReportBankingTransaction.from_dict(
                transactions_item_data
            )

            transactions.append(transactions_item)

        codat_assess_data_contracts_cash_flow_transactions_transactions_data_source = cls(
            transactions=transactions,
        )

        return codat_assess_data_contracts_cash_flow_transactions_transactions_data_source
