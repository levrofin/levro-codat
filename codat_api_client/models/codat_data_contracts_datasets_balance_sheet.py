import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_report_line import CodatDataContractsDatasetsReportLine


T = TypeVar("T", bound="CodatDataContractsDatasetsBalanceSheet")


@define
class CodatDataContractsDatasetsBalanceSheet:
    """
    Attributes:
        net_assets (float):
        date (Union[Unset, datetime.datetime]):
        assets (Union[Unset, CodatDataContractsDatasetsReportLine]):
        liabilities (Union[Unset, CodatDataContractsDatasetsReportLine]):
        equity (Union[Unset, CodatDataContractsDatasetsReportLine]):
    """

    net_assets: float
    date: Union[Unset, datetime.datetime] = UNSET
    assets: Union[Unset, "CodatDataContractsDatasetsReportLine"] = UNSET
    liabilities: Union[Unset, "CodatDataContractsDatasetsReportLine"] = UNSET
    equity: Union[Unset, "CodatDataContractsDatasetsReportLine"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        net_assets = self.net_assets
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        assets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assets, Unset):
            assets = self.assets.to_dict()

        liabilities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.liabilities, Unset):
            liabilities = self.liabilities.to_dict()

        equity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.equity, Unset):
            equity = self.equity.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "netAssets": net_assets,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if assets is not UNSET:
            field_dict["assets"] = assets
        if liabilities is not UNSET:
            field_dict["liabilities"] = liabilities
        if equity is not UNSET:
            field_dict["equity"] = equity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_report_line import CodatDataContractsDatasetsReportLine

        d = src_dict.copy()
        net_assets = d.pop("netAssets")

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _assets = d.pop("assets", UNSET)
        assets: Union[Unset, CodatDataContractsDatasetsReportLine]
        if isinstance(_assets, Unset):
            assets = UNSET
        else:
            assets = CodatDataContractsDatasetsReportLine.from_dict(_assets)

        _liabilities = d.pop("liabilities", UNSET)
        liabilities: Union[Unset, CodatDataContractsDatasetsReportLine]
        if isinstance(_liabilities, Unset):
            liabilities = UNSET
        else:
            liabilities = CodatDataContractsDatasetsReportLine.from_dict(_liabilities)

        _equity = d.pop("equity", UNSET)
        equity: Union[Unset, CodatDataContractsDatasetsReportLine]
        if isinstance(_equity, Unset):
            equity = UNSET
        else:
            equity = CodatDataContractsDatasetsReportLine.from_dict(_equity)

        codat_data_contracts_datasets_balance_sheet = cls(
            net_assets=net_assets,
            date=date,
            assets=assets,
            liabilities=liabilities,
            equity=equity,
        )

        return codat_data_contracts_datasets_balance_sheet
