from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsClientsClientCompanyMetricsModel")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsClientsClientCompanyMetricsModel:
    """
    Attributes:
        currently_linked (Union[Unset, int]):
        no_longer_linked (Union[Unset, int]):
        not_yet_linked (Union[Unset, int]):
        all_time_linked (Union[Unset, int]):
    """

    currently_linked: Union[Unset, int] = UNSET
    no_longer_linked: Union[Unset, int] = UNSET
    not_yet_linked: Union[Unset, int] = UNSET
    all_time_linked: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        currently_linked = self.currently_linked
        no_longer_linked = self.no_longer_linked
        not_yet_linked = self.not_yet_linked
        all_time_linked = self.all_time_linked

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if currently_linked is not UNSET:
            field_dict["currentlyLinked"] = currently_linked
        if no_longer_linked is not UNSET:
            field_dict["noLongerLinked"] = no_longer_linked
        if not_yet_linked is not UNSET:
            field_dict["notYetLinked"] = not_yet_linked
        if all_time_linked is not UNSET:
            field_dict["allTimeLinked"] = all_time_linked

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currently_linked = d.pop("currentlyLinked", UNSET)

        no_longer_linked = d.pop("noLongerLinked", UNSET)

        not_yet_linked = d.pop("notYetLinked", UNSET)

        all_time_linked = d.pop("allTimeLinked", UNSET)

        codat_public_api_models_clients_client_company_metrics_model = cls(
            currently_linked=currently_linked,
            no_longer_linked=no_longer_linked,
            not_yet_linked=not_yet_linked,
            all_time_linked=all_time_linked,
        )

        return codat_public_api_models_clients_client_company_metrics_model
