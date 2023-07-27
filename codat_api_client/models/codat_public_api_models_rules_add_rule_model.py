from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_public_api_models_rules_notifiers import CodatPublicApiModelsRulesNotifiers


T = TypeVar("T", bound="CodatPublicApiModelsRulesAddRuleModel")


@define
class CodatPublicApiModelsRulesAddRuleModel:
    """
    Attributes:
        company_id (str): Leave the companyID blank to create a rule that applies to all companies
        type (str):
        notifiers (Union[Unset, CodatPublicApiModelsRulesNotifiers]):
    """

    company_id: str
    type: str
    notifiers: Union[Unset, "CodatPublicApiModelsRulesNotifiers"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        type = self.type
        notifiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notifiers, Unset):
            notifiers = self.notifiers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "companyId": company_id,
                "type": type,
            }
        )
        if notifiers is not UNSET:
            field_dict["notifiers"] = notifiers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_public_api_models_rules_notifiers import CodatPublicApiModelsRulesNotifiers

        d = src_dict.copy()
        company_id = d.pop("companyId")

        type = d.pop("type")

        _notifiers = d.pop("notifiers", UNSET)
        notifiers: Union[Unset, CodatPublicApiModelsRulesNotifiers]
        if isinstance(_notifiers, Unset):
            notifiers = UNSET
        else:
            notifiers = CodatPublicApiModelsRulesNotifiers.from_dict(_notifiers)

        codat_public_api_models_rules_add_rule_model = cls(
            company_id=company_id,
            type=type,
            notifiers=notifiers,
        )

        return codat_public_api_models_rules_add_rule_model
