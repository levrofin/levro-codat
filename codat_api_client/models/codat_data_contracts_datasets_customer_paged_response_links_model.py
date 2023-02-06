from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_customer_paged_response_href_model import (
        CodatDataContractsDatasetsCustomerPagedResponseHrefModel,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsCustomerPagedResponseLinksModel")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCustomerPagedResponseLinksModel:
    """
    Attributes:
        self_ (Union[Unset, CodatDataContractsDatasetsCustomerPagedResponseHrefModel]):
        current (Union[Unset, CodatDataContractsDatasetsCustomerPagedResponseHrefModel]):
        next_ (Union[Unset, CodatDataContractsDatasetsCustomerPagedResponseHrefModel]):
        previous (Union[Unset, CodatDataContractsDatasetsCustomerPagedResponseHrefModel]):
    """

    self_: Union[Unset, "CodatDataContractsDatasetsCustomerPagedResponseHrefModel"] = UNSET
    current: Union[Unset, "CodatDataContractsDatasetsCustomerPagedResponseHrefModel"] = UNSET
    next_: Union[Unset, "CodatDataContractsDatasetsCustomerPagedResponseHrefModel"] = UNSET
    previous: Union[Unset, "CodatDataContractsDatasetsCustomerPagedResponseHrefModel"] = UNSET

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
        from ..models.codat_data_contracts_datasets_customer_paged_response_href_model import (
            CodatDataContractsDatasetsCustomerPagedResponseHrefModel,
        )

        d = src_dict.copy()
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, CodatDataContractsDatasetsCustomerPagedResponseHrefModel]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = CodatDataContractsDatasetsCustomerPagedResponseHrefModel.from_dict(_self_)

        _current = d.pop("current", UNSET)
        current: Union[Unset, CodatDataContractsDatasetsCustomerPagedResponseHrefModel]
        if isinstance(_current, Unset):
            current = UNSET
        else:
            current = CodatDataContractsDatasetsCustomerPagedResponseHrefModel.from_dict(_current)

        _next_ = d.pop("next", UNSET)
        next_: Union[Unset, CodatDataContractsDatasetsCustomerPagedResponseHrefModel]
        if isinstance(_next_, Unset):
            next_ = UNSET
        else:
            next_ = CodatDataContractsDatasetsCustomerPagedResponseHrefModel.from_dict(_next_)

        _previous = d.pop("previous", UNSET)
        previous: Union[Unset, CodatDataContractsDatasetsCustomerPagedResponseHrefModel]
        if isinstance(_previous, Unset):
            previous = UNSET
        else:
            previous = CodatDataContractsDatasetsCustomerPagedResponseHrefModel.from_dict(_previous)

        codat_data_contracts_datasets_customer_paged_response_links_model = cls(
            self_=self_,
            current=current,
            next_=next_,
            previous=previous,
        )

        return codat_data_contracts_datasets_customer_paged_response_links_model
