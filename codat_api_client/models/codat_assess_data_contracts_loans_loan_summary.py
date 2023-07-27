from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_loans_loan_record_ref import CodatAssessDataContractsLoansLoanRecordRef


T = TypeVar("T", bound="CodatAssessDataContractsLoansLoanSummary")


@define
class CodatAssessDataContractsLoansLoanSummary:
    """
    Attributes:
        record_ref (Union[Unset, CodatAssessDataContractsLoansLoanRecordRef]):
        description (Union[Unset, None, str]):
        start_date (Union[Unset, None, str]):
        total_drawdowns (Union[Unset, float]):
        total_repayments (Union[Unset, float]):
        balance (Union[Unset, None, float]):
    """

    record_ref: Union[Unset, "CodatAssessDataContractsLoansLoanRecordRef"] = UNSET
    description: Union[Unset, None, str] = UNSET
    start_date: Union[Unset, None, str] = UNSET
    total_drawdowns: Union[Unset, float] = UNSET
    total_repayments: Union[Unset, float] = UNSET
    balance: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        record_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_ref, Unset):
            record_ref = self.record_ref.to_dict()

        description = self.description
        start_date = self.start_date
        total_drawdowns = self.total_drawdowns
        total_repayments = self.total_repayments
        balance = self.balance

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if record_ref is not UNSET:
            field_dict["recordRef"] = record_ref
        if description is not UNSET:
            field_dict["description"] = description
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if total_drawdowns is not UNSET:
            field_dict["totalDrawdowns"] = total_drawdowns
        if total_repayments is not UNSET:
            field_dict["totalRepayments"] = total_repayments
        if balance is not UNSET:
            field_dict["balance"] = balance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_loans_loan_record_ref import (
            CodatAssessDataContractsLoansLoanRecordRef,
        )

        d = src_dict.copy()
        _record_ref = d.pop("recordRef", UNSET)
        record_ref: Union[Unset, CodatAssessDataContractsLoansLoanRecordRef]
        if isinstance(_record_ref, Unset):
            record_ref = UNSET
        else:
            record_ref = CodatAssessDataContractsLoansLoanRecordRef.from_dict(_record_ref)

        description = d.pop("description", UNSET)

        start_date = d.pop("startDate", UNSET)

        total_drawdowns = d.pop("totalDrawdowns", UNSET)

        total_repayments = d.pop("totalRepayments", UNSET)

        balance = d.pop("balance", UNSET)

        codat_assess_data_contracts_loans_loan_summary = cls(
            record_ref=record_ref,
            description=description,
            start_date=start_date,
            total_drawdowns=total_drawdowns,
            total_repayments=total_repayments,
            balance=balance,
        )

        return codat_assess_data_contracts_loans_loan_summary
