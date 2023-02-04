from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_validation_validation_item import CodatDataContractsValidationValidationItem


T = TypeVar("T", bound="CodatDataContractsValidationValidationResult")


@attr.s(auto_attribs=True)
class CodatDataContractsValidationValidationResult:
    """
    Attributes:
        errors (Union[Unset, None, List['CodatDataContractsValidationValidationItem']]):
        warnings (Union[Unset, None, List['CodatDataContractsValidationValidationItem']]):
    """

    errors: Union[Unset, None, List["CodatDataContractsValidationValidationItem"]] = UNSET
    warnings: Union[Unset, None, List["CodatDataContractsValidationValidationItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        errors: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            if self.errors is None:
                errors = None
            else:
                errors = []
                for errors_item_data in self.errors:
                    errors_item = errors_item_data.to_dict()

                    errors.append(errors_item)

        warnings: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            if self.warnings is None:
                warnings = None
            else:
                warnings = []
                for warnings_item_data in self.warnings:
                    warnings_item = warnings_item_data.to_dict()

                    warnings.append(warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_validation_validation_item import CodatDataContractsValidationValidationItem

        d = src_dict.copy()
        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = CodatDataContractsValidationValidationItem.from_dict(errors_item_data)

            errors.append(errors_item)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = CodatDataContractsValidationValidationItem.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        codat_data_contracts_validation_validation_result = cls(
            errors=errors,
            warnings=warnings,
        )

        return codat_data_contracts_validation_validation_result
