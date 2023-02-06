from enum import Enum


class CodatAssessDataContractsFinancialsMetricsMetricKey(str, Enum):
    UNKNOWN = "Unknown"
    EBITDA = "EBITDA"
    DEBTSERVICECOVERAGERATIO = "DebtServiceCoverageRatio"
    CURRENTRATIO = "CurrentRatio"
    QUICKRATIO = "QuickRatio"
    GROSSPROFITMARGIN = "GrossProfitMargin"
    FIXEDCHARGECOVERAGERATIO = "FixedChargeCoverageRatio"
    WORKINGCAPITAL = "WorkingCapital"
    FREECASHFLOW = "FreeCashFlow"
    NETPROFITMARGIN = "NetProfitMargin"
    RETURNONASSETSRATIO = "ReturnOnAssetsRatio"
    RETURNONEQUITYRATIO = "ReturnOnEquityRatio"
    OPERATINGPROFITMARGIN = "OperatingProfitMargin"
    DEPTTOEQUITY = "DeptToEquity"
    DEBTTOASSETS = "DebtToAssets"
    INTERESTCOVERAGERATIO = "InterestCoverageRatio"
    CASHRATIO = "CashRatio"
    INVENTORYTURNOVERRATIO = "InventoryTurnoverRatio"
    ASSETTURNOVERRATIO = "AssetTurnoverRatio"
    WORKINGCAPITALTURNOVERRATIO = "WorkingCapitalTurnoverRatio"
    DAYSSALESOUTSTANDING = "DaysSalesOutstanding"
    DAYSPAYABLESOUTSTANDING = "DaysPayablesOutstanding"

    def __str__(self) -> str:
        return str(self.value)
