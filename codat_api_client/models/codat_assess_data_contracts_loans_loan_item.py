from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_assess_data_contracts_loans_record_ref import CodatAssessDataContractsLoansRecordRef


T = TypeVar("T", bound="CodatAssessDataContractsLoansLoanItem")


@define
class CodatAssessDataContractsLoansLoanItem:
    """
    Attributes:
        loan_ref (Union[Unset, CodatAssessDataContractsLoansRecordRef]):
        item_ref (Union[Unset, CodatAssessDataContractsLoansRecordRef]):
        date (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        transaction_type (Union[Unset, None, str]):
        amount (Union[Unset, float]):
    """

    loan_ref: Union[Unset, "CodatAssessDataContractsLoansRecordRef"] = UNSET
    item_ref: Union[Unset, "CodatAssessDataContractsLoansRecordRef"] = UNSET
    date: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    transaction_type: Union[Unset, None, str] = UNSET
    amount: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        loan_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.loan_ref, Unset):
            loan_ref = self.loan_ref.to_dict()

        item_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_ref, Unset):
            item_ref = self.item_ref.to_dict()

        date = self.date
        description = self.description
        transaction_type = self.transaction_type
        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if loan_ref is not UNSET:
            field_dict["loanRef"] = loan_ref
        if item_ref is not UNSET:
            field_dict["itemRef"] = item_ref
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if transaction_type is not UNSET:
            field_dict["transactionType"] = transaction_type
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_assess_data_contracts_loans_record_ref import CodatAssessDataContractsLoansRecordRef

        d = src_dict.copy()
        _loan_ref = d.pop("loanRef", UNSET)
        loan_ref: Union[Unset, CodatAssessDataContractsLoansRecordRef]
        if isinstance(_loan_ref, Unset):
            loan_ref = UNSET
        else:
            loan_ref = CodatAssessDataContractsLoansRecordRef.from_dict(_loan_ref)

        _item_ref = d.pop("itemRef", UNSET)
        item_ref: Union[Unset, CodatAssessDataContractsLoansRecordRef]
        if isinstance(_item_ref, Unset):
            item_ref = UNSET
        else:
            item_ref = CodatAssessDataContractsLoansRecordRef.from_dict(_item_ref)

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        transaction_type = d.pop("transactionType", UNSET)

        amount = d.pop("amount", UNSET)

        codat_assess_data_contracts_loans_loan_item = cls(
            loan_ref=loan_ref,
            item_ref=item_ref,
            date=date,
            description=description,
            transaction_type=transaction_type,
            amount=amount,
        )

        return codat_assess_data_contracts_loans_loan_item
