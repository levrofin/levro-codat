from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsCompanyUpdateCompanyModel")


@define
class CodatPublicApiModelsCompanyUpdateCompanyModel:
    """
    Attributes:
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
    """

    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        codat_public_api_models_company_update_company_model = cls(
            name=name,
            description=description,
        )

        return codat_public_api_models_company_update_company_model
