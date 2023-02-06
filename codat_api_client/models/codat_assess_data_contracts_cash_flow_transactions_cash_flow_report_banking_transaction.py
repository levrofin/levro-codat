from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_cash_flow_transactions_source_ref import (
        CodatAssessDataContractsCashFlowTransactionsSourceRef,
    )
    from ..models.codat_assess_data_contracts_cash_flow_transactions_transaction_category import (
        CodatAssessDataContractsCashFlowTransactionsTransactionCategory,
    )


T = TypeVar("T", bound="CodatAssessDataContractsCashFlowTransactionsCashFlowReportBankingTransaction")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsCashFlowTransactionsCashFlowReportBankingTransaction:
    """
    Attributes:
        source_ref (Union[Unset, CodatAssessDataContractsCashFlowTransactionsSourceRef]):
        id (Union[Unset, None, str]):
        date (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        amount (Union[Unset, float]):
        currency (Union[Unset, None, str]):
        transaction_category (Union[Unset, CodatAssessDataContractsCashFlowTransactionsTransactionCategory]):
    """

    source_ref: Union[Unset, "CodatAssessDataContractsCashFlowTransactionsSourceRef"] = UNSET
    id: Union[Unset, None, str] = UNSET
    date: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, None, str] = UNSET
    transaction_category: Union[Unset, "CodatAssessDataContractsCashFlowTransactionsTransactionCategory"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        source_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source_ref, Unset):
            source_ref = self.source_ref.to_dict()

        id = self.id
        date = self.date
        description = self.description
        amount = self.amount
        currency = self.currency
        transaction_category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transaction_category, Unset):
            transaction_category = self.transaction_category.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if source_ref is not UNSET:
            field_dict["sourceRef"] = source_ref
        if id is not UNSET:
            field_dict["id"] = id
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if transaction_category is not UNSET:
            field_dict["transactionCategory"] = transaction_category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_cash_flow_transactions_source_ref import (
            CodatAssessDataContractsCashFlowTransactionsSourceRef,
        )
        from ..models.codat_assess_data_contracts_cash_flow_transactions_transaction_category import (
            CodatAssessDataContractsCashFlowTransactionsTransactionCategory,
        )

        d = src_dict.copy()
        _source_ref = d.pop("sourceRef", UNSET)
        source_ref: Union[Unset, CodatAssessDataContractsCashFlowTransactionsSourceRef]
        if isinstance(_source_ref, Unset):
            source_ref = UNSET
        else:
            source_ref = CodatAssessDataContractsCashFlowTransactionsSourceRef.from_dict(_source_ref)

        id = d.pop("id", UNSET)

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        _transaction_category = d.pop("transactionCategory", UNSET)
        transaction_category: Union[Unset, CodatAssessDataContractsCashFlowTransactionsTransactionCategory]
        if isinstance(_transaction_category, Unset):
            transaction_category = UNSET
        else:
            transaction_category = CodatAssessDataContractsCashFlowTransactionsTransactionCategory.from_dict(
                _transaction_category
            )

        codat_assess_data_contracts_cash_flow_transactions_cash_flow_report_banking_transaction = cls(
            source_ref=source_ref,
            id=id,
            date=date,
            description=description,
            amount=amount,
            currency=currency,
            transaction_category=transaction_category,
        )

        return codat_assess_data_contracts_cash_flow_transactions_cash_flow_report_banking_transaction
