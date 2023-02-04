from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_cash_flow_transactions_source_ref import (
        CodatAssessDataContractsCashFlowTransactionsSourceRef,
    )


T = TypeVar("T", bound="CodatAssessDataContractsCashFlowTransactionsCashFlowReportBankingAccount")


@attr.s(auto_attribs=True)
class CodatAssessDataContractsCashFlowTransactionsCashFlowReportBankingAccount:
    """
    Attributes:
        source_ref (Union[Unset, CodatAssessDataContractsCashFlowTransactionsSourceRef]):
        platform_name (Union[Unset, None, str]):
        account_provider (Union[Unset, None, str]):
        account_name (Union[Unset, None, str]):
        account_type (Union[Unset, None, str]):
        currency (Union[Unset, None, str]):
        current_balance (Union[Unset, float]):
    """

    source_ref: Union[Unset, "CodatAssessDataContractsCashFlowTransactionsSourceRef"] = UNSET
    platform_name: Union[Unset, None, str] = UNSET
    account_provider: Union[Unset, None, str] = UNSET
    account_name: Union[Unset, None, str] = UNSET
    account_type: Union[Unset, None, str] = UNSET
    currency: Union[Unset, None, str] = UNSET
    current_balance: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        source_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source_ref, Unset):
            source_ref = self.source_ref.to_dict()

        platform_name = self.platform_name
        account_provider = self.account_provider
        account_name = self.account_name
        account_type = self.account_type
        currency = self.currency
        current_balance = self.current_balance

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if source_ref is not UNSET:
            field_dict["sourceRef"] = source_ref
        if platform_name is not UNSET:
            field_dict["platformName"] = platform_name
        if account_provider is not UNSET:
            field_dict["accountProvider"] = account_provider
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if currency is not UNSET:
            field_dict["currency"] = currency
        if current_balance is not UNSET:
            field_dict["currentBalance"] = current_balance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_cash_flow_transactions_source_ref import (
            CodatAssessDataContractsCashFlowTransactionsSourceRef,
        )

        d = src_dict.copy()
        _source_ref = d.pop("sourceRef", UNSET)
        source_ref: Union[Unset, CodatAssessDataContractsCashFlowTransactionsSourceRef]
        if isinstance(_source_ref, Unset):
            source_ref = UNSET
        else:
            source_ref = CodatAssessDataContractsCashFlowTransactionsSourceRef.from_dict(_source_ref)

        platform_name = d.pop("platformName", UNSET)

        account_provider = d.pop("accountProvider", UNSET)

        account_name = d.pop("accountName", UNSET)

        account_type = d.pop("accountType", UNSET)

        currency = d.pop("currency", UNSET)

        current_balance = d.pop("currentBalance", UNSET)

        codat_assess_data_contracts_cash_flow_transactions_cash_flow_report_banking_account = cls(
            source_ref=source_ref,
            platform_name=platform_name,
            account_provider=account_provider,
            account_name=account_name,
            account_type=account_type,
            currency=currency,
            current_balance=current_balance,
        )

        return codat_assess_data_contracts_cash_flow_transactions_cash_flow_report_banking_account
