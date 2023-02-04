from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_account_ref import CodatDataContractsDatasetsAccountRef
    from ..models.codat_data_contracts_datasets_tracking import CodatDataContractsDatasetsTracking


T = TypeVar("T", bound="CodatDataContractsDatasetsJournalLine")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsJournalLine:
    """
    Attributes:
        net_amount (float):
        description (Union[Unset, None, str]):
        currency (Union[Unset, None, str]):
        account_ref (Union[Unset, CodatDataContractsDatasetsAccountRef]):
        tracking (Union[Unset, CodatDataContractsDatasetsTracking]):
    """

    net_amount: float
    description: Union[Unset, None, str] = UNSET
    currency: Union[Unset, None, str] = UNSET
    account_ref: Union[Unset, "CodatDataContractsDatasetsAccountRef"] = UNSET
    tracking: Union[Unset, "CodatDataContractsDatasetsTracking"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        net_amount = self.net_amount
        description = self.description
        currency = self.currency
        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        tracking: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tracking, Unset):
            tracking = self.tracking.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "netAmount": net_amount,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if currency is not UNSET:
            field_dict["currency"] = currency
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if tracking is not UNSET:
            field_dict["tracking"] = tracking

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_account_ref import CodatDataContractsDatasetsAccountRef
        from ..models.codat_data_contracts_datasets_tracking import CodatDataContractsDatasetsTracking

        d = src_dict.copy()
        net_amount = d.pop("netAmount")

        description = d.pop("description", UNSET)

        currency = d.pop("currency", UNSET)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, CodatDataContractsDatasetsAccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = CodatDataContractsDatasetsAccountRef.from_dict(_account_ref)

        _tracking = d.pop("tracking", UNSET)
        tracking: Union[Unset, CodatDataContractsDatasetsTracking]
        if isinstance(_tracking, Unset):
            tracking = UNSET
        else:
            tracking = CodatDataContractsDatasetsTracking.from_dict(_tracking)

        codat_data_contracts_datasets_journal_line = cls(
            net_amount=net_amount,
            description=description,
            currency=currency,
            account_ref=account_ref,
            tracking=tracking,
        )

        return codat_data_contracts_datasets_journal_line
