from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_bank_account_paged_response_href_model import (
        CodatDataContractsDatasetsBankAccountPagedResponseHrefModel,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsBankAccountPagedResponseLinksModel")


@define
class CodatDataContractsDatasetsBankAccountPagedResponseLinksModel:
    """
    Attributes:
        self_ (Union[Unset, CodatDataContractsDatasetsBankAccountPagedResponseHrefModel]):
        current (Union[Unset, CodatDataContractsDatasetsBankAccountPagedResponseHrefModel]):
        next_ (Union[Unset, CodatDataContractsDatasetsBankAccountPagedResponseHrefModel]):
        previous (Union[Unset, CodatDataContractsDatasetsBankAccountPagedResponseHrefModel]):
    """

    self_: Union[Unset, "CodatDataContractsDatasetsBankAccountPagedResponseHrefModel"] = UNSET
    current: Union[Unset, "CodatDataContractsDatasetsBankAccountPagedResponseHrefModel"] = UNSET
    next_: Union[Unset, "CodatDataContractsDatasetsBankAccountPagedResponseHrefModel"] = UNSET
    previous: Union[Unset, "CodatDataContractsDatasetsBankAccountPagedResponseHrefModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        self_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        current: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current, Unset):
            current = self.current.to_dict()

        next_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.next_, Unset):
            next_ = self.next_.to_dict()

        previous: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.previous, Unset):
            previous = self.previous.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if current is not UNSET:
            field_dict["current"] = current
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_bank_account_paged_response_href_model import (
            CodatDataContractsDatasetsBankAccountPagedResponseHrefModel,
        )

        d = src_dict.copy()
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, CodatDataContractsDatasetsBankAccountPagedResponseHrefModel]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = CodatDataContractsDatasetsBankAccountPagedResponseHrefModel.from_dict(_self_)

        _current = d.pop("current", UNSET)
        current: Union[Unset, CodatDataContractsDatasetsBankAccountPagedResponseHrefModel]
        if isinstance(_current, Unset):
            current = UNSET
        else:
            current = CodatDataContractsDatasetsBankAccountPagedResponseHrefModel.from_dict(_current)

        _next_ = d.pop("next", UNSET)
        next_: Union[Unset, CodatDataContractsDatasetsBankAccountPagedResponseHrefModel]
        if isinstance(_next_, Unset):
            next_ = UNSET
        else:
            next_ = CodatDataContractsDatasetsBankAccountPagedResponseHrefModel.from_dict(_next_)

        _previous = d.pop("previous", UNSET)
        previous: Union[Unset, CodatDataContractsDatasetsBankAccountPagedResponseHrefModel]
        if isinstance(_previous, Unset):
            previous = UNSET
        else:
            previous = CodatDataContractsDatasetsBankAccountPagedResponseHrefModel.from_dict(_previous)

        codat_data_contracts_datasets_bank_account_paged_response_links_model = cls(
            self_=self_,
            current=current,
            next_=next_,
            previous=previous,
        )

        return codat_data_contracts_datasets_bank_account_paged_response_links_model
