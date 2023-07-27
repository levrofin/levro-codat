from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_bank_statement_line import CodatDataContractsDatasetsBankStatementLine


T = TypeVar("T", bound="CodatDataContractsDatasetsBankTransactions")


@define
class CodatDataContractsDatasetsBankTransactions:
    """
    Attributes:
        account_id (Union[Unset, None, str]):
        transactions (Union[Unset, None, List['CodatDataContractsDatasetsBankStatementLine']]):
        contract_version (Union[Unset, None, str]):
    """

    account_id: Union[Unset, None, str] = UNSET
    transactions: Union[Unset, None, List["CodatDataContractsDatasetsBankStatementLine"]] = UNSET
    contract_version: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        transactions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transactions, Unset):
            if self.transactions is None:
                transactions = None
            else:
                transactions = []
                for transactions_item_data in self.transactions:
                    transactions_item = transactions_item_data.to_dict()

                    transactions.append(transactions_item)

        contract_version = self.contract_version

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if transactions is not UNSET:
            field_dict["transactions"] = transactions
        if contract_version is not UNSET:
            field_dict["contractVersion"] = contract_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_bank_statement_line import (
            CodatDataContractsDatasetsBankStatementLine,
        )

        d = src_dict.copy()
        account_id = d.pop("accountId", UNSET)

        transactions = []
        _transactions = d.pop("transactions", UNSET)
        for transactions_item_data in _transactions or []:
            transactions_item = CodatDataContractsDatasetsBankStatementLine.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        contract_version = d.pop("contractVersion", UNSET)

        codat_data_contracts_datasets_bank_transactions = cls(
            account_id=account_id,
            transactions=transactions,
            contract_version=contract_version,
        )

        return codat_data_contracts_datasets_bank_transactions
