from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_pull_messages_contracts_fetch_message import CodatPullMessagesContractsFetchMessage
    from ..models.codat_pull_messages_contracts_map_message import CodatPullMessagesContractsMapMessage
    from ..models.codat_pull_messages_contracts_validation_message import CodatPullMessagesContractsValidationMessage


T = TypeVar("T", bound="CodatPullMessagesContractsDatasetMessages")


@define
class CodatPullMessagesContractsDatasetMessages:
    """
    Attributes:
        fetch (Union[Unset, None, List['CodatPullMessagesContractsFetchMessage']]):
        map_ (Union[Unset, None, List['CodatPullMessagesContractsMapMessage']]):
        validation (Union[Unset, None, List['CodatPullMessagesContractsValidationMessage']]):
    """

    fetch: Union[Unset, None, List["CodatPullMessagesContractsFetchMessage"]] = UNSET
    map_: Union[Unset, None, List["CodatPullMessagesContractsMapMessage"]] = UNSET
    validation: Union[Unset, None, List["CodatPullMessagesContractsValidationMessage"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        fetch: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fetch, Unset):
            if self.fetch is None:
                fetch = None
            else:
                fetch = []
                for fetch_item_data in self.fetch:
                    fetch_item = fetch_item_data.to_dict()

                    fetch.append(fetch_item)

        map_: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.map_, Unset):
            if self.map_ is None:
                map_ = None
            else:
                map_ = []
                for map_item_data in self.map_:
                    map_item = map_item_data.to_dict()

                    map_.append(map_item)

        validation: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.validation, Unset):
            if self.validation is None:
                validation = None
            else:
                validation = []
                for validation_item_data in self.validation:
                    validation_item = validation_item_data.to_dict()

                    validation.append(validation_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if fetch is not UNSET:
            field_dict["fetch"] = fetch
        if map_ is not UNSET:
            field_dict["map"] = map_
        if validation is not UNSET:
            field_dict["validation"] = validation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_pull_messages_contracts_fetch_message import CodatPullMessagesContractsFetchMessage
        from ..models.codat_pull_messages_contracts_map_message import CodatPullMessagesContractsMapMessage
        from ..models.codat_pull_messages_contracts_validation_message import (
            CodatPullMessagesContractsValidationMessage,
        )

        d = src_dict.copy()
        fetch = []
        _fetch = d.pop("fetch", UNSET)
        for fetch_item_data in _fetch or []:
            fetch_item = CodatPullMessagesContractsFetchMessage.from_dict(fetch_item_data)

            fetch.append(fetch_item)

        map_ = []
        _map_ = d.pop("map", UNSET)
        for map_item_data in _map_ or []:
            map_item = CodatPullMessagesContractsMapMessage.from_dict(map_item_data)

            map_.append(map_item)

        validation = []
        _validation = d.pop("validation", UNSET)
        for validation_item_data in _validation or []:
            validation_item = CodatPullMessagesContractsValidationMessage.from_dict(validation_item_data)

            validation.append(validation_item)

        codat_pull_messages_contracts_dataset_messages = cls(
            fetch=fetch,
            map_=map_,
            validation=validation,
        )

        return codat_pull_messages_contracts_dataset_messages
