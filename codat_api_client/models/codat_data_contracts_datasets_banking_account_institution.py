from typing import Any, Dict, Type, TypeVar

from attrs import define

T = TypeVar("T", bound="CodatDataContractsDatasetsBankingAccountInstitution")


@define
class CodatDataContractsDatasetsBankingAccountInstitution:
    """
    Attributes:
        id (str):
        name (str):
    """

    id: str
    name: str

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        codat_data_contracts_datasets_banking_account_institution = cls(
            id=id,
            name=name,
        )

        return codat_data_contracts_datasets_banking_account_institution
