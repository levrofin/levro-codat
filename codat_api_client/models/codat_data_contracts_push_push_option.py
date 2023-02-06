from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.codat_data_contracts_push_option_type import CodatDataContractsPushOptionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_push_push_option_choice import CodatDataContractsPushPushOptionChoice
    from ..models.codat_data_contracts_push_push_option_properties import CodatDataContractsPushPushOptionProperties
    from ..models.codat_data_contracts_push_push_validation_info import CodatDataContractsPushPushValidationInfo


T = TypeVar("T", bound="CodatDataContractsPushPushOption")


@attr.s(auto_attribs=True)
class CodatDataContractsPushPushOption:
    """
    Attributes:
        type (CodatDataContractsPushOptionType):
        display_name (str):
        description (str):
        required (bool):
        properties (Union[Unset, None, CodatDataContractsPushPushOptionProperties]):
        options (Union[Unset, None, List['CodatDataContractsPushPushOptionChoice']]):
        validation (Union[Unset, CodatDataContractsPushPushValidationInfo]):
        rel (Union[Unset, None, str]):
    """

    type: CodatDataContractsPushOptionType
    display_name: str
    description: str
    required: bool
    properties: Union[Unset, None, "CodatDataContractsPushPushOptionProperties"] = UNSET
    options: Union[Unset, None, List["CodatDataContractsPushPushOptionChoice"]] = UNSET
    validation: Union[Unset, "CodatDataContractsPushPushValidationInfo"] = UNSET
    rel: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        display_name = self.display_name
        description = self.description
        required = self.required
        properties: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict() if self.properties else None

        options: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            if self.options is None:
                options = None
            else:
                options = []
                for options_item_data in self.options:
                    options_item = options_item_data.to_dict()

                    options.append(options_item)

        validation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.validation, Unset):
            validation = self.validation.to_dict()

        rel = self.rel

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "displayName": display_name,
                "description": description,
                "required": required,
            }
        )
        if properties is not UNSET:
            field_dict["properties"] = properties
        if options is not UNSET:
            field_dict["options"] = options
        if validation is not UNSET:
            field_dict["validation"] = validation
        if rel is not UNSET:
            field_dict["rel"] = rel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_push_push_option_choice import CodatDataContractsPushPushOptionChoice
        from ..models.codat_data_contracts_push_push_option_properties import CodatDataContractsPushPushOptionProperties
        from ..models.codat_data_contracts_push_push_validation_info import CodatDataContractsPushPushValidationInfo

        d = src_dict.copy()
        type = CodatDataContractsPushOptionType(d.pop("type"))

        display_name = d.pop("displayName")

        description = d.pop("description")

        required = d.pop("required")

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, None, CodatDataContractsPushPushOptionProperties]
        if _properties is None:
            properties = None
        elif isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = CodatDataContractsPushPushOptionProperties.from_dict(_properties)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = CodatDataContractsPushPushOptionChoice.from_dict(options_item_data)

            options.append(options_item)

        _validation = d.pop("validation", UNSET)
        validation: Union[Unset, CodatDataContractsPushPushValidationInfo]
        if isinstance(_validation, Unset):
            validation = UNSET
        else:
            validation = CodatDataContractsPushPushValidationInfo.from_dict(_validation)

        rel = d.pop("rel", UNSET)

        codat_data_contracts_push_push_option = cls(
            type=type,
            display_name=display_name,
            description=description,
            required=required,
            properties=properties,
            options=options,
            validation=validation,
            rel=rel,
        )

        return codat_data_contracts_push_push_option
