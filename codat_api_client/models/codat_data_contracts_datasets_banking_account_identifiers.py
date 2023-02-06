from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatDataContractsDatasetsBankingAccountIdentifiers")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsBankingAccountIdentifiers:
    """
    Attributes:
        type (str):
        subtype (Union[Unset, None, str]):
        number (Union[Unset, None, str]):
        bank_code (Union[Unset, None, str]):
        iban (Union[Unset, None, str]):
        bic (Union[Unset, None, str]):
        masked_account_number (Union[Unset, None, str]):
    """

    type: str
    subtype: Union[Unset, None, str] = UNSET
    number: Union[Unset, None, str] = UNSET
    bank_code: Union[Unset, None, str] = UNSET
    iban: Union[Unset, None, str] = UNSET
    bic: Union[Unset, None, str] = UNSET
    masked_account_number: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        subtype = self.subtype
        number = self.number
        bank_code = self.bank_code
        iban = self.iban
        bic = self.bic
        masked_account_number = self.masked_account_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if number is not UNSET:
            field_dict["number"] = number
        if bank_code is not UNSET:
            field_dict["bankCode"] = bank_code
        if iban is not UNSET:
            field_dict["iban"] = iban
        if bic is not UNSET:
            field_dict["bic"] = bic
        if masked_account_number is not UNSET:
            field_dict["maskedAccountNumber"] = masked_account_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        subtype = d.pop("subtype", UNSET)

        number = d.pop("number", UNSET)

        bank_code = d.pop("bankCode", UNSET)

        iban = d.pop("iban", UNSET)

        bic = d.pop("bic", UNSET)

        masked_account_number = d.pop("maskedAccountNumber", UNSET)

        codat_data_contracts_datasets_banking_account_identifiers = cls(
            type=type,
            subtype=subtype,
            number=number,
            bank_code=bank_code,
            iban=iban,
            bic=bic,
            masked_account_number=masked_account_number,
        )

        return codat_data_contracts_datasets_banking_account_identifiers
