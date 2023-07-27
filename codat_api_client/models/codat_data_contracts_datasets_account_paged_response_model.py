from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_account import CodatDataContractsDatasetsAccount
    from ..models.codat_data_contracts_datasets_account_paged_response_links_model import (
        CodatDataContractsDatasetsAccountPagedResponseLinksModel,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsAccountPagedResponseModel")


@define
class CodatDataContractsDatasetsAccountPagedResponseModel:
    """Used to represent what can be returned by an endpoint that supports paging.
    Usable with the [ProducesResponseType] attribute on a controller action.

        Attributes:
            results (Union[Unset, None, List['CodatDataContractsDatasetsAccount']]):
            page_number (Union[Unset, int]):
            page_size (Union[Unset, int]):
            total_results (Union[Unset, int]):
            field_links (Union[Unset, CodatDataContractsDatasetsAccountPagedResponseLinksModel]):
    """

    results: Union[Unset, None, List["CodatDataContractsDatasetsAccount"]] = UNSET
    page_number: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    total_results: Union[Unset, int] = UNSET
    field_links: Union[Unset, "CodatDataContractsDatasetsAccountPagedResponseLinksModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        results: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            if self.results is None:
                results = None
            else:
                results = []
                for results_item_data in self.results:
                    results_item = results_item_data.to_dict()

                    results.append(results_item)

        page_number = self.page_number
        page_size = self.page_size
        total_results = self.total_results
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if total_results is not UNSET:
            field_dict["totalResults"] = total_results
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_account import CodatDataContractsDatasetsAccount
        from ..models.codat_data_contracts_datasets_account_paged_response_links_model import (
            CodatDataContractsDatasetsAccountPagedResponseLinksModel,
        )

        d = src_dict.copy()
        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = CodatDataContractsDatasetsAccount.from_dict(results_item_data)

            results.append(results_item)

        page_number = d.pop("pageNumber", UNSET)

        page_size = d.pop("pageSize", UNSET)

        total_results = d.pop("totalResults", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CodatDataContractsDatasetsAccountPagedResponseLinksModel]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CodatDataContractsDatasetsAccountPagedResponseLinksModel.from_dict(_field_links)

        codat_data_contracts_datasets_account_paged_response_model = cls(
            results=results,
            page_number=page_number,
            page_size=page_size,
            total_results=total_results,
            field_links=field_links,
        )

        return codat_data_contracts_datasets_account_paged_response_model
