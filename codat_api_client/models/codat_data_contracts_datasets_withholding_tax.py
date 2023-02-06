from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="CodatDataContractsDatasetsWithholdingTax")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsWithholdingTax:
    """
    Attributes:
        name (str):
        amount (float):
    """

    name: str
    amount: float

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        amount = d.pop("amount")

        codat_data_contracts_datasets_withholding_tax = cls(
            name=name,
            amount=amount,
        )

        return codat_data_contracts_datasets_withholding_tax
