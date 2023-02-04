import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_report_line import CodatDataContractsDatasetsReportLine


T = TypeVar("T", bound="CodatDataContractsDatasetsCashFlowStatement")


@attr.s(auto_attribs=True)
class CodatDataContractsDatasetsCashFlowStatement:
    """
    Attributes:
        from_date (Union[Unset, datetime.datetime]):
        to_date (Union[Unset, datetime.datetime]):
        cash_receipts (Union[Unset, CodatDataContractsDatasetsReportLine]):
        cash_payments (Union[Unset, CodatDataContractsDatasetsReportLine]):
    """

    from_date: Union[Unset, datetime.datetime] = UNSET
    to_date: Union[Unset, datetime.datetime] = UNSET
    cash_receipts: Union[Unset, "CodatDataContractsDatasetsReportLine"] = UNSET
    cash_payments: Union[Unset, "CodatDataContractsDatasetsReportLine"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from_date: Union[Unset, str] = UNSET
        if not isinstance(self.from_date, Unset):
            from_date = self.from_date.isoformat()

        to_date: Union[Unset, str] = UNSET
        if not isinstance(self.to_date, Unset):
            to_date = self.to_date.isoformat()

        cash_receipts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cash_receipts, Unset):
            cash_receipts = self.cash_receipts.to_dict()

        cash_payments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cash_payments, Unset):
            cash_payments = self.cash_payments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if from_date is not UNSET:
            field_dict["fromDate"] = from_date
        if to_date is not UNSET:
            field_dict["toDate"] = to_date
        if cash_receipts is not UNSET:
            field_dict["cashReceipts"] = cash_receipts
        if cash_payments is not UNSET:
            field_dict["cashPayments"] = cash_payments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_report_line import CodatDataContractsDatasetsReportLine

        d = src_dict.copy()
        _from_date = d.pop("fromDate", UNSET)
        from_date: Union[Unset, datetime.datetime]
        if isinstance(_from_date, Unset):
            from_date = UNSET
        else:
            from_date = isoparse(_from_date)

        _to_date = d.pop("toDate", UNSET)
        to_date: Union[Unset, datetime.datetime]
        if isinstance(_to_date, Unset):
            to_date = UNSET
        else:
            to_date = isoparse(_to_date)

        _cash_receipts = d.pop("cashReceipts", UNSET)
        cash_receipts: Union[Unset, CodatDataContractsDatasetsReportLine]
        if isinstance(_cash_receipts, Unset):
            cash_receipts = UNSET
        else:
            cash_receipts = CodatDataContractsDatasetsReportLine.from_dict(_cash_receipts)

        _cash_payments = d.pop("cashPayments", UNSET)
        cash_payments: Union[Unset, CodatDataContractsDatasetsReportLine]
        if isinstance(_cash_payments, Unset):
            cash_payments = UNSET
        else:
            cash_payments = CodatDataContractsDatasetsReportLine.from_dict(_cash_payments)

        codat_data_contracts_datasets_cash_flow_statement = cls(
            from_date=from_date,
            to_date=to_date,
            cash_receipts=cash_receipts,
            cash_payments=cash_payments,
        )

        return codat_data_contracts_datasets_cash_flow_statement
