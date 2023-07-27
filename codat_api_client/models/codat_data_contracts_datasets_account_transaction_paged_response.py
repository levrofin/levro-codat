from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_account_transaction import CodatDataContractsDatasetsAccountTransaction
    from ..models.codat_data_contracts_datasets_account_transaction_paged_response_links import (
        CodatDataContractsDatasetsAccountTransactionPagedResponseLinks,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsAccountTransactionPagedResponse")


@define
class CodatDataContractsDatasetsAccountTransactionPagedResponse:
    """
    Attributes:
        page_number (int):
        page_size (int):
        total_results (int):
        results (Union[Unset, None, List['CodatDataContractsDatasetsAccountTransaction']]):
        field_links (Union[Unset, None, CodatDataContractsDatasetsAccountTransactionPagedResponseLinks]):
    """

    page_number: int
    page_size: int
    total_results: int
    results: Union[Unset, None, List["CodatDataContractsDatasetsAccountTransaction"]] = UNSET
    field_links: Union[Unset, None, "CodatDataContractsDatasetsAccountTransactionPagedResponseLinks"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        page_number = self.page_number
        page_size = self.page_size
        total_results = self.total_results
        results: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            if self.results is None:
                results = None
            else:
                results = []
                for results_item_data in self.results:
                    results_item = results_item_data.to_dict()

                    results.append(results_item)

        field_links: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict() if self.field_links else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "pageNumber": page_number,
                "pageSize": page_size,
                "totalResults": total_results,
            }
        )
        if results is not UNSET:
            field_dict["results"] = results
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_account_transaction import (
            CodatDataContractsDatasetsAccountTransaction,
        )
        from ..models.codat_data_contracts_datasets_account_transaction_paged_response_links import (
            CodatDataContractsDatasetsAccountTransactionPagedResponseLinks,
        )

        d = src_dict.copy()
        page_number = d.pop("pageNumber")

        page_size = d.pop("pageSize")

        total_results = d.pop("totalResults")

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = CodatDataContractsDatasetsAccountTransaction.from_dict(results_item_data)

            results.append(results_item)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, None, CodatDataContractsDatasetsAccountTransactionPagedResponseLinks]
        if _field_links is None:
            field_links = None
        elif isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CodatDataContractsDatasetsAccountTransactionPagedResponseLinks.from_dict(_field_links)

        codat_data_contracts_datasets_account_transaction_paged_response = cls(
            page_number=page_number,
            page_size=page_size,
            total_results=total_results,
            results=results,
            field_links=field_links,
        )

        return codat_data_contracts_datasets_account_transaction_paged_response
