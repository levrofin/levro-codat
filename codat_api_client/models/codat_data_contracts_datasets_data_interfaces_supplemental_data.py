from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data_content import (
        CodatDataContractsDatasetsDataInterfacesSupplementalDataContent,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsDataInterfacesSupplementalData")


@define
class CodatDataContractsDatasetsDataInterfacesSupplementalData:
    """
    Attributes:
        content (Union[Unset, None, CodatDataContractsDatasetsDataInterfacesSupplementalDataContent]):
    """

    content: Union[Unset, None, "CodatDataContractsDatasetsDataInterfacesSupplementalDataContent"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        content: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict() if self.content else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data_content import (
            CodatDataContractsDatasetsDataInterfacesSupplementalDataContent,
        )

        d = src_dict.copy()
        _content = d.pop("content", UNSET)
        content: Union[Unset, None, CodatDataContractsDatasetsDataInterfacesSupplementalDataContent]
        if _content is None:
            content = None
        elif isinstance(_content, Unset):
            content = UNSET
        else:
            content = CodatDataContractsDatasetsDataInterfacesSupplementalDataContent.from_dict(_content)

        codat_data_contracts_datasets_data_interfaces_supplemental_data = cls(
            content=content,
        )

        return codat_data_contracts_datasets_data_interfaces_supplemental_data
