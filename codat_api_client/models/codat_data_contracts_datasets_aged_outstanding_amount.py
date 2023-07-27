import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_aged_outstanding_amount_detail import (
        CodatDataContractsDatasetsAgedOutstandingAmountDetail,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsAgedOutstandingAmount")


@define
class CodatDataContractsDatasetsAgedOutstandingAmount:
    """
    Attributes:
        from_date (Union[Unset, None, datetime.datetime]):
        to_date (Union[Unset, datetime.datetime]):
        amount (Union[Unset, float]):
        details (Union[Unset, None, List['CodatDataContractsDatasetsAgedOutstandingAmountDetail']]):
    """

    from_date: Union[Unset, None, datetime.datetime] = UNSET
    to_date: Union[Unset, datetime.datetime] = UNSET
    amount: Union[Unset, float] = UNSET
    details: Union[Unset, None, List["CodatDataContractsDatasetsAgedOutstandingAmountDetail"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.from_date, Unset):
            from_date = self.from_date.isoformat() if self.from_date else None

        to_date: Union[Unset, str] = UNSET
        if not isinstance(self.to_date, Unset):
            to_date = self.to_date.isoformat()

        amount = self.amount
        details: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            if self.details is None:
                details = None
            else:
                details = []
                for details_item_data in self.details:
                    details_item = details_item_data.to_dict()

                    details.append(details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if from_date is not UNSET:
            field_dict["fromDate"] = from_date
        if to_date is not UNSET:
            field_dict["toDate"] = to_date
        if amount is not UNSET:
            field_dict["amount"] = amount
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_aged_outstanding_amount_detail import (
            CodatDataContractsDatasetsAgedOutstandingAmountDetail,
        )

        d = src_dict.copy()
        _from_date = d.pop("fromDate", UNSET)
        from_date: Union[Unset, None, datetime.datetime]
        if _from_date is None:
            from_date = None
        elif isinstance(_from_date, Unset):
            from_date = UNSET
        else:
            from_date = isoparse(_from_date)

        _to_date = d.pop("toDate", UNSET)
        to_date: Union[Unset, datetime.datetime]
        if isinstance(_to_date, Unset):
            to_date = UNSET
        else:
            to_date = isoparse(_to_date)

        amount = d.pop("amount", UNSET)

        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = CodatDataContractsDatasetsAgedOutstandingAmountDetail.from_dict(details_item_data)

            details.append(details_item)

        codat_data_contracts_datasets_aged_outstanding_amount = cls(
            from_date=from_date,
            to_date=to_date,
            amount=amount,
            details=details,
        )

        return codat_data_contracts_datasets_aged_outstanding_amount
