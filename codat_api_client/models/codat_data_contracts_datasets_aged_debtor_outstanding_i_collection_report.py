import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_aged_debtor_outstanding import (
        CodatDataContractsDatasetsAgedDebtorOutstanding,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsAgedDebtorOutstandingICollectionReport")


@define
class CodatDataContractsDatasetsAgedDebtorOutstandingICollectionReport:
    """
    Attributes:
        generated (datetime.datetime):
        report_date (datetime.datetime):
        data (List['CodatDataContractsDatasetsAgedDebtorOutstanding']):
    """

    generated: datetime.datetime
    report_date: datetime.datetime
    data: List["CodatDataContractsDatasetsAgedDebtorOutstanding"]

    def to_dict(self) -> Dict[str, Any]:
        generated = self.generated.isoformat()

        report_date = self.report_date.isoformat()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "generated": generated,
                "reportDate": report_date,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_aged_debtor_outstanding import (
            CodatDataContractsDatasetsAgedDebtorOutstanding,
        )

        d = src_dict.copy()
        generated = isoparse(d.pop("generated"))

        report_date = isoparse(d.pop("reportDate"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = CodatDataContractsDatasetsAgedDebtorOutstanding.from_dict(data_item_data)

            data.append(data_item)

        codat_data_contracts_datasets_aged_debtor_outstanding_i_collection_report = cls(
            generated=generated,
            report_date=report_date,
            data=data,
        )

        return codat_data_contracts_datasets_aged_debtor_outstanding_i_collection_report
