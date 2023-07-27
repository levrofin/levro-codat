from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_rules_notifiers import CodatPublicApiModelsRulesNotifiers


T = TypeVar("T", bound="CodatPublicApiModelsRulesRule")


@define
class CodatPublicApiModelsRulesRule:
    """
    Attributes:
        id (str):
        type (str):
        company_id (Union[Unset, None, str]):
        notifiers (Union[Unset, CodatPublicApiModelsRulesNotifiers]):
    """

    id: str
    type: str
    company_id: Union[Unset, None, str] = UNSET
    notifiers: Union[Unset, "CodatPublicApiModelsRulesNotifiers"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        company_id = self.company_id
        notifiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notifiers, Unset):
            notifiers = self.notifiers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if notifiers is not UNSET:
            field_dict["notifiers"] = notifiers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_rules_notifiers import CodatPublicApiModelsRulesNotifiers

        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        company_id = d.pop("companyId", UNSET)

        _notifiers = d.pop("notifiers", UNSET)
        notifiers: Union[Unset, CodatPublicApiModelsRulesNotifiers]
        if isinstance(_notifiers, Unset):
            notifiers = UNSET
        else:
            notifiers = CodatPublicApiModelsRulesNotifiers.from_dict(_notifiers)

        codat_public_api_models_rules_rule = cls(
            id=id,
            type=type,
            company_id=company_id,
            notifiers=notifiers,
        )

        return codat_public_api_models_rules_rule
