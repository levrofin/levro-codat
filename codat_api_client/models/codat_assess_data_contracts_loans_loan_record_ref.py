from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..models.codat_assess_data_contracts_loans_integration_type import CodatAssessDataContractsLoansIntegrationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatAssessDataContractsLoansLoanRecordRef")


@define
class CodatAssessDataContractsLoansLoanRecordRef:
    """
    Attributes:
        id (Union[Unset, None, str]):
        data_connection_id (Union[Unset, None, str]):
        integration_type (Union[Unset, CodatAssessDataContractsLoansIntegrationType]):
        record_ref_type (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    data_connection_id: Union[Unset, None, str] = UNSET
    integration_type: Union[Unset, CodatAssessDataContractsLoansIntegrationType] = UNSET
    record_ref_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        data_connection_id = self.data_connection_id
        integration_type: Union[Unset, str] = UNSET
        if not isinstance(self.integration_type, Unset):
            integration_type = self.integration_type.value

        record_ref_type = self.record_ref_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if data_connection_id is not UNSET:
            field_dict["dataConnectionId"] = data_connection_id
        if integration_type is not UNSET:
            field_dict["integrationType"] = integration_type
        if record_ref_type is not UNSET:
            field_dict["recordRefType"] = record_ref_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        data_connection_id = d.pop("dataConnectionId", UNSET)

        _integration_type = d.pop("integrationType", UNSET)
        integration_type: Union[Unset, CodatAssessDataContractsLoansIntegrationType]
        if isinstance(_integration_type, Unset):
            integration_type = UNSET
        else:
            integration_type = CodatAssessDataContractsLoansIntegrationType(_integration_type)

        record_ref_type = d.pop("recordRefType", UNSET)

        codat_assess_data_contracts_loans_loan_record_ref = cls(
            id=id,
            data_connection_id=data_connection_id,
            integration_type=integration_type,
            record_ref_type=record_ref_type,
        )

        return codat_assess_data_contracts_loans_loan_record_ref
