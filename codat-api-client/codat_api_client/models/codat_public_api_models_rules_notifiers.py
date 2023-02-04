from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsRulesNotifiers")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsRulesNotifiers:
    """
    Attributes:
        emails (Union[Unset, None, List[str]]):
        webhook (Union[Unset, None, str]):
    """

    emails: Union[Unset, None, List[str]] = UNSET
    webhook: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        emails: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.emails, Unset):
            if self.emails is None:
                emails = None
            else:
                emails = self.emails

        webhook = self.webhook

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if emails is not UNSET:
            field_dict["emails"] = emails
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        emails = cast(List[str], d.pop("emails", UNSET))

        webhook = d.pop("webhook", UNSET)

        codat_public_api_models_rules_notifiers = cls(
            emails=emails,
            webhook=webhook,
        )

        return codat_public_api_models_rules_notifiers
