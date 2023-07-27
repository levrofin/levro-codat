from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef


T = TypeVar("T", bound="CodatDataContractsDatasetsAccountTransactionLine")


@define
class CodatDataContractsDatasetsAccountTransactionLine:
    """
    Attributes:
        description (Union[Unset, None, str]):
        record_ref (Union[Unset, CodatDataContractsDatasetsRecordRef]):
        amount (Union[Unset, float]):
    """

    description: Union[Unset, None, str] = UNSET
    record_ref: Union[Unset, "CodatDataContractsDatasetsRecordRef"] = UNSET
    amount: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        record_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_ref, Unset):
            record_ref = self.record_ref.to_dict()

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if record_ref is not UNSET:
            field_dict["recordRef"] = record_ref
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_record_ref import CodatDataContractsDatasetsRecordRef

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        _record_ref = d.pop("recordRef", UNSET)
        record_ref: Union[Unset, CodatDataContractsDatasetsRecordRef]
        if isinstance(_record_ref, Unset):
            record_ref = UNSET
        else:
            record_ref = CodatDataContractsDatasetsRecordRef.from_dict(_record_ref)

        amount = d.pop("amount", UNSET)

        codat_data_contracts_datasets_account_transaction_line = cls(
            description=description,
            record_ref=record_ref,
            amount=amount,
        )

        return codat_data_contracts_datasets_account_transaction_line
