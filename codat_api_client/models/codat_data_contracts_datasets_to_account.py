from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef


T = TypeVar("T", bound="CodatDataContractsDatasetsToAccount")


@define
class CodatDataContractsDatasetsToAccount:
    """
    Attributes:
        account_ref (Union[Unset, CodatDataContractsDatasetsRecordRef]):
        currency (Union[Unset, None, str]):
        amount (Union[Unset, float]):
    """

    account_ref: Union[Unset, "CodatDataContractsDatasetsRecordRef"] = UNSET
    currency: Union[Unset, None, str] = UNSET
    amount: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        currency = self.currency
        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef

        d = src_dict.copy()
        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, CodatDataContractsDatasetsRecordRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = CodatDataContractsDatasetsRecordRef.from_dict(_account_ref)

        currency = d.pop("currency", UNSET)

        amount = d.pop("amount", UNSET)

        codat_data_contracts_datasets_to_account = cls(
            account_ref=account_ref,
            currency=currency,
            amount=amount,
        )

        return codat_data_contracts_datasets_to_account
