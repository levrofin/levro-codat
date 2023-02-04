from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_integrity_contracts_metadata_match_amount_info import (
        CodatDataIntegrityContractsMetadataMatchAmountInfo,
    )
    from ..models.codat_data_integrity_contracts_metadata_match_connection_ids import (
        CodatDataIntegrityContractsMetadataMatchConnectionIds,
    )
    from ..models.codat_data_integrity_contracts_metadata_match_date_info import (
        CodatDataIntegrityContractsMetadataMatchDateInfo,
    )
    from ..models.codat_data_integrity_contracts_metadata_match_status_info import (
        CodatDataIntegrityContractsMetadataMatchStatusInfo,
    )


T = TypeVar("T", bound="CodatDataIntegrityContractsMetadataMatchMetadata")


@attr.s(auto_attribs=True)
class CodatDataIntegrityContractsMetadataMatchMetadata:
    """
    Attributes:
        type (Union[Unset, None, str]):
        status_info (Union[Unset, CodatDataIntegrityContractsMetadataMatchStatusInfo]):
        connection_ids (Union[Unset, CodatDataIntegrityContractsMetadataMatchConnectionIds]):
        amounts (Union[Unset, CodatDataIntegrityContractsMetadataMatchAmountInfo]):
        dates (Union[Unset, CodatDataIntegrityContractsMetadataMatchDateInfo]):
    """

    type: Union[Unset, None, str] = UNSET
    status_info: Union[Unset, "CodatDataIntegrityContractsMetadataMatchStatusInfo"] = UNSET
    connection_ids: Union[Unset, "CodatDataIntegrityContractsMetadataMatchConnectionIds"] = UNSET
    amounts: Union[Unset, "CodatDataIntegrityContractsMetadataMatchAmountInfo"] = UNSET
    dates: Union[Unset, "CodatDataIntegrityContractsMetadataMatchDateInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        status_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status_info, Unset):
            status_info = self.status_info.to_dict()

        connection_ids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.connection_ids, Unset):
            connection_ids = self.connection_ids.to_dict()

        amounts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amounts, Unset):
            amounts = self.amounts.to_dict()

        dates: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dates, Unset):
            dates = self.dates.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if status_info is not UNSET:
            field_dict["statusInfo"] = status_info
        if connection_ids is not UNSET:
            field_dict["connectionIds"] = connection_ids
        if amounts is not UNSET:
            field_dict["amounts"] = amounts
        if dates is not UNSET:
            field_dict["dates"] = dates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_integrity_contracts_metadata_match_amount_info import (
            CodatDataIntegrityContractsMetadataMatchAmountInfo,
        )
        from ..models.codat_data_integrity_contracts_metadata_match_connection_ids import (
            CodatDataIntegrityContractsMetadataMatchConnectionIds,
        )
        from ..models.codat_data_integrity_contracts_metadata_match_date_info import (
            CodatDataIntegrityContractsMetadataMatchDateInfo,
        )
        from ..models.codat_data_integrity_contracts_metadata_match_status_info import (
            CodatDataIntegrityContractsMetadataMatchStatusInfo,
        )

        d = src_dict.copy()
        type = d.pop("type", UNSET)

        _status_info = d.pop("statusInfo", UNSET)
        status_info: Union[Unset, CodatDataIntegrityContractsMetadataMatchStatusInfo]
        if isinstance(_status_info, Unset):
            status_info = UNSET
        else:
            status_info = CodatDataIntegrityContractsMetadataMatchStatusInfo.from_dict(_status_info)

        _connection_ids = d.pop("connectionIds", UNSET)
        connection_ids: Union[Unset, CodatDataIntegrityContractsMetadataMatchConnectionIds]
        if isinstance(_connection_ids, Unset):
            connection_ids = UNSET
        else:
            connection_ids = CodatDataIntegrityContractsMetadataMatchConnectionIds.from_dict(_connection_ids)

        _amounts = d.pop("amounts", UNSET)
        amounts: Union[Unset, CodatDataIntegrityContractsMetadataMatchAmountInfo]
        if isinstance(_amounts, Unset):
            amounts = UNSET
        else:
            amounts = CodatDataIntegrityContractsMetadataMatchAmountInfo.from_dict(_amounts)

        _dates = d.pop("dates", UNSET)
        dates: Union[Unset, CodatDataIntegrityContractsMetadataMatchDateInfo]
        if isinstance(_dates, Unset):
            dates = UNSET
        else:
            dates = CodatDataIntegrityContractsMetadataMatchDateInfo.from_dict(_dates)

        codat_data_integrity_contracts_metadata_match_metadata = cls(
            type=type,
            status_info=status_info,
            connection_ids=connection_ids,
            amounts=amounts,
            dates=dates,
        )

        return codat_data_integrity_contracts_metadata_match_metadata
