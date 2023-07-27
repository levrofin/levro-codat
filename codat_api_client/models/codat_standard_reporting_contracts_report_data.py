from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_standard_reporting_contracts_i_report_data_measure import (
        CodatStandardReportingContractsIReportDataMeasure,
    )


T = TypeVar("T", bound="CodatStandardReportingContractsReportData")


@define
class CodatStandardReportingContractsReportData:
    """
    Attributes:
        dimension (Union[Unset, int]):
        dimension_display_name (Union[Unset, None, str]):
        item (Union[Unset, int]):
        item_display_name (Union[Unset, None, str]):
        measures (Union[Unset, None, List['CodatStandardReportingContractsIReportDataMeasure']]):
        components (Union[Unset, None, List['CodatStandardReportingContractsReportData']]):
    """

    dimension: Union[Unset, int] = UNSET
    dimension_display_name: Union[Unset, None, str] = UNSET
    item: Union[Unset, int] = UNSET
    item_display_name: Union[Unset, None, str] = UNSET
    measures: Union[Unset, None, List["CodatStandardReportingContractsIReportDataMeasure"]] = UNSET
    components: Union[Unset, None, List["CodatStandardReportingContractsReportData"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        dimension = self.dimension
        dimension_display_name = self.dimension_display_name
        item = self.item
        item_display_name = self.item_display_name
        measures: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.measures, Unset):
            if self.measures is None:
                measures = None
            else:
                measures = []
                for measures_item_data in self.measures:
                    measures_item = measures_item_data.to_dict()

                    measures.append(measures_item)

        components: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.components, Unset):
            if self.components is None:
                components = None
            else:
                components = []
                for components_item_data in self.components:
                    components_item = components_item_data.to_dict()

                    components.append(components_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if dimension_display_name is not UNSET:
            field_dict["dimensionDisplayName"] = dimension_display_name
        if item is not UNSET:
            field_dict["item"] = item
        if item_display_name is not UNSET:
            field_dict["itemDisplayName"] = item_display_name
        if measures is not UNSET:
            field_dict["measures"] = measures
        if components is not UNSET:
            field_dict["components"] = components

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_standard_reporting_contracts_i_report_data_measure import (
            CodatStandardReportingContractsIReportDataMeasure,
        )

        d = src_dict.copy()
        dimension = d.pop("dimension", UNSET)

        dimension_display_name = d.pop("dimensionDisplayName", UNSET)

        item = d.pop("item", UNSET)

        item_display_name = d.pop("itemDisplayName", UNSET)

        measures = []
        _measures = d.pop("measures", UNSET)
        for measures_item_data in _measures or []:
            measures_item = CodatStandardReportingContractsIReportDataMeasure.from_dict(measures_item_data)

            measures.append(measures_item)

        components = []
        _components = d.pop("components", UNSET)
        for components_item_data in _components or []:
            components_item = CodatStandardReportingContractsReportData.from_dict(components_item_data)

            components.append(components_item)

        codat_standard_reporting_contracts_report_data = cls(
            dimension=dimension,
            dimension_display_name=dimension_display_name,
            item=item,
            item_display_name=item_display_name,
            measures=measures,
            components=components,
        )

        return codat_standard_reporting_contracts_report_data
