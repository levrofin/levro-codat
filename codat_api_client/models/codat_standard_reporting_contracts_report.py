from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_standard_reporting_contracts_i_dimension import CodatStandardReportingContractsIDimension
    from ..models.codat_standard_reporting_contracts_measure import CodatStandardReportingContractsMeasure
    from ..models.codat_standard_reporting_contracts_report_data import CodatStandardReportingContractsReportData
    from ..models.codat_standard_reporting_contracts_report_error import CodatStandardReportingContractsReportError
    from ..models.codat_standard_reporting_contracts_report_report_info import (
        CodatStandardReportingContractsReportReportInfo,
    )


T = TypeVar("T", bound="CodatStandardReportingContractsReport")


@define
class CodatStandardReportingContractsReport:
    """
    Attributes:
        report_info (Union[Unset, None, CodatStandardReportingContractsReportReportInfo]):
        dimensions (Union[Unset, None, List['CodatStandardReportingContractsIDimension']]):
        measures (Union[Unset, None, List['CodatStandardReportingContractsMeasure']]):
        report_data (Union[Unset, None, List['CodatStandardReportingContractsReportData']]):
        errors (Union[Unset, None, List['CodatStandardReportingContractsReportError']]):
    """

    report_info: Union[Unset, None, "CodatStandardReportingContractsReportReportInfo"] = UNSET
    dimensions: Union[Unset, None, List["CodatStandardReportingContractsIDimension"]] = UNSET
    measures: Union[Unset, None, List["CodatStandardReportingContractsMeasure"]] = UNSET
    report_data: Union[Unset, None, List["CodatStandardReportingContractsReportData"]] = UNSET
    errors: Union[Unset, None, List["CodatStandardReportingContractsReportError"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        report_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.report_info, Unset):
            report_info = self.report_info.to_dict() if self.report_info else None

        dimensions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dimensions, Unset):
            if self.dimensions is None:
                dimensions = None
            else:
                dimensions = []
                for dimensions_item_data in self.dimensions:
                    dimensions_item = dimensions_item_data.to_dict()

                    dimensions.append(dimensions_item)

        measures: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.measures, Unset):
            if self.measures is None:
                measures = None
            else:
                measures = []
                for measures_item_data in self.measures:
                    measures_item = measures_item_data.to_dict()

                    measures.append(measures_item)

        report_data: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.report_data, Unset):
            if self.report_data is None:
                report_data = None
            else:
                report_data = []
                for report_data_item_data in self.report_data:
                    report_data_item = report_data_item_data.to_dict()

                    report_data.append(report_data_item)

        errors: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            if self.errors is None:
                errors = None
            else:
                errors = []
                for errors_item_data in self.errors:
                    errors_item = errors_item_data.to_dict()

                    errors.append(errors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if report_info is not UNSET:
            field_dict["reportInfo"] = report_info
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if measures is not UNSET:
            field_dict["measures"] = measures
        if report_data is not UNSET:
            field_dict["reportData"] = report_data
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_standard_reporting_contracts_i_dimension import CodatStandardReportingContractsIDimension
        from ..models.codat_standard_reporting_contracts_measure import CodatStandardReportingContractsMeasure
        from ..models.codat_standard_reporting_contracts_report_data import CodatStandardReportingContractsReportData
        from ..models.codat_standard_reporting_contracts_report_error import CodatStandardReportingContractsReportError
        from ..models.codat_standard_reporting_contracts_report_report_info import (
            CodatStandardReportingContractsReportReportInfo,
        )

        d = src_dict.copy()
        _report_info = d.pop("reportInfo", UNSET)
        report_info: Union[Unset, None, CodatStandardReportingContractsReportReportInfo]
        if _report_info is None:
            report_info = None
        elif isinstance(_report_info, Unset):
            report_info = UNSET
        else:
            report_info = CodatStandardReportingContractsReportReportInfo.from_dict(_report_info)

        dimensions = []
        _dimensions = d.pop("dimensions", UNSET)
        for dimensions_item_data in _dimensions or []:
            dimensions_item = CodatStandardReportingContractsIDimension.from_dict(dimensions_item_data)

            dimensions.append(dimensions_item)

        measures = []
        _measures = d.pop("measures", UNSET)
        for measures_item_data in _measures or []:
            measures_item = CodatStandardReportingContractsMeasure.from_dict(measures_item_data)

            measures.append(measures_item)

        report_data = []
        _report_data = d.pop("reportData", UNSET)
        for report_data_item_data in _report_data or []:
            report_data_item = CodatStandardReportingContractsReportData.from_dict(report_data_item_data)

            report_data.append(report_data_item)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = CodatStandardReportingContractsReportError.from_dict(errors_item_data)

            errors.append(errors_item)

        codat_standard_reporting_contracts_report = cls(
            report_info=report_info,
            dimensions=dimensions,
            measures=measures,
            report_data=report_data,
            errors=errors,
        )

        return codat_standard_reporting_contracts_report
