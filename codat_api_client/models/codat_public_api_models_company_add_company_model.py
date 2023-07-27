from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatPublicApiModelsCompanyAddCompanyModel")


@define
class CodatPublicApiModelsCompanyAddCompanyModel:
    """
    Attributes:
        name (str):
        description (Union[Unset, None, str]):
        platform_type (Union[Unset, None, str]):
    """

    name: str
    description: Union[Unset, None, str] = UNSET
    platform_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        platform_type = self.platform_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if platform_type is not UNSET:
            field_dict["platformType"] = platform_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        platform_type = d.pop("platformType", UNSET)

        codat_public_api_models_company_add_company_model = cls(
            name=name,
            description=description,
            platform_type=platform_type,
        )

        return codat_public_api_models_company_add_company_model
