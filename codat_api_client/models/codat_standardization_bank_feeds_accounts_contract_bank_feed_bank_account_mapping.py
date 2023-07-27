import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodatStandardizationBankFeedsAccountsContractBankFeedBankAccountMapping")


@define
class CodatStandardizationBankFeedsAccountsContractBankFeedBankAccountMapping:
    """
    Attributes:
        source_account_id (Union[Unset, None, str]):
        target_account_id (Union[Unset, None, str]):
        feed_start_date (Union[Unset, datetime.datetime]):
    """

    source_account_id: Union[Unset, None, str] = UNSET
    target_account_id: Union[Unset, None, str] = UNSET
    feed_start_date: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        source_account_id = self.source_account_id
        target_account_id = self.target_account_id
        feed_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.feed_start_date, Unset):
            feed_start_date = self.feed_start_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if source_account_id is not UNSET:
            field_dict["sourceAccountId"] = source_account_id
        if target_account_id is not UNSET:
            field_dict["targetAccountId"] = target_account_id
        if feed_start_date is not UNSET:
            field_dict["feedStartDate"] = feed_start_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_account_id = d.pop("sourceAccountId", UNSET)

        target_account_id = d.pop("targetAccountId", UNSET)

        _feed_start_date = d.pop("feedStartDate", UNSET)
        feed_start_date: Union[Unset, datetime.datetime]
        if isinstance(_feed_start_date, Unset):
            feed_start_date = UNSET
        else:
            feed_start_date = isoparse(_feed_start_date)

        codat_standardization_bank_feeds_accounts_contract_bank_feed_bank_account_mapping = cls(
            source_account_id=source_account_id,
            target_account_id=target_account_id,
            feed_start_date=feed_start_date,
        )

        return codat_standardization_bank_feeds_accounts_contract_bank_feed_bank_account_mapping
