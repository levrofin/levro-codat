from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_push_push_field_validation import CodatDataContractsPushPushFieldValidation


T = TypeVar("T", bound="CodatDataContractsPushPushValidationInfo")


@define
class CodatDataContractsPushPushValidationInfo:
    """
    Attributes:
        warnings (Union[Unset, None, List['CodatDataContractsPushPushFieldValidation']]):
        information (Union[Unset, None, List['CodatDataContractsPushPushFieldValidation']]):
    """

    warnings: Union[Unset, None, List["CodatDataContractsPushPushFieldValidation"]] = UNSET
    information: Union[Unset, None, List["CodatDataContractsPushPushFieldValidation"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        warnings: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            if self.warnings is None:
                warnings = None
            else:
                warnings = []
                for warnings_item_data in self.warnings:
                    warnings_item = warnings_item_data.to_dict()

                    warnings.append(warnings_item)

        information: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.information, Unset):
            if self.information is None:
                information = None
            else:
                information = []
                for information_item_data in self.information:
                    information_item = information_item_data.to_dict()

                    information.append(information_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if information is not UNSET:
            field_dict["information"] = information

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_push_push_field_validation import CodatDataContractsPushPushFieldValidation

        d = src_dict.copy()
        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = CodatDataContractsPushPushFieldValidation.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        information = []
        _information = d.pop("information", UNSET)
        for information_item_data in _information or []:
            information_item = CodatDataContractsPushPushFieldValidation.from_dict(information_item_data)

            information.append(information_item)

        codat_data_contracts_push_push_validation_info = cls(
            warnings=warnings,
            information=information,
        )

        return codat_data_contracts_push_push_validation_info
