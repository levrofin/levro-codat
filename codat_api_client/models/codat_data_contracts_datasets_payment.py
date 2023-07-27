import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_account_ref import CodatDataContractsDatasetsAccountRef
    from ..models.codat_data_contracts_datasets_customer_ref import CodatDataContractsDatasetsCustomerRef
    from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
        CodatDataContractsDatasetsDataInterfacesSupplementalData,
    )
    from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
    from ..models.codat_data_contracts_datasets_payment_line import CodatDataContractsDatasetsPaymentLine
    from ..models.codat_data_contracts_datasets_payment_method_ref import CodatDataContractsDatasetsPaymentMethodRef


T = TypeVar("T", bound="CodatDataContractsDatasetsPayment")


@define
class CodatDataContractsDatasetsPayment:
    """
    Attributes:
        date (datetime.datetime):
        id (Union[Unset, None, str]):
        customer_ref (Union[Unset, CodatDataContractsDatasetsCustomerRef]):
        account_ref (Union[Unset, CodatDataContractsDatasetsAccountRef]):
        payment_method_ref (Union[Unset, CodatDataContractsDatasetsPaymentMethodRef]):
        total_amount (Union[Unset, float]):
        currency (Union[Unset, None, str]):
        currency_rate (Union[Unset, None, float]):
        note (Union[Unset, None, str]):
        lines (Union[Unset, None, List['CodatDataContractsDatasetsPaymentLine']]):
        modified_date (Union[Unset, None, datetime.datetime]):
        source_modified_date (Union[Unset, None, datetime.datetime]):
        reference (Union[Unset, None, str]):
        metadata (Union[Unset, CodatDataContractsDatasetsMetadata]):
        supplemental_data (Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]):
    """

    date: datetime.datetime
    id: Union[Unset, None, str] = UNSET
    customer_ref: Union[Unset, "CodatDataContractsDatasetsCustomerRef"] = UNSET
    account_ref: Union[Unset, "CodatDataContractsDatasetsAccountRef"] = UNSET
    payment_method_ref: Union[Unset, "CodatDataContractsDatasetsPaymentMethodRef"] = UNSET
    total_amount: Union[Unset, float] = UNSET
    currency: Union[Unset, None, str] = UNSET
    currency_rate: Union[Unset, None, float] = UNSET
    note: Union[Unset, None, str] = UNSET
    lines: Union[Unset, None, List["CodatDataContractsDatasetsPaymentLine"]] = UNSET
    modified_date: Union[Unset, None, datetime.datetime] = UNSET
    source_modified_date: Union[Unset, None, datetime.datetime] = UNSET
    reference: Union[Unset, None, str] = UNSET
    metadata: Union[Unset, "CodatDataContractsDatasetsMetadata"] = UNSET
    supplemental_data: Union[Unset, "CodatDataContractsDatasetsDataInterfacesSupplementalData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        date = self.date.isoformat()

        id = self.id
        customer_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_ref, Unset):
            customer_ref = self.customer_ref.to_dict()

        account_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_ref, Unset):
            account_ref = self.account_ref.to_dict()

        payment_method_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_ref, Unset):
            payment_method_ref = self.payment_method_ref.to_dict()

        total_amount = self.total_amount
        currency = self.currency
        currency_rate = self.currency_rate
        note = self.note
        lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            if self.lines is None:
                lines = None
            else:
                lines = []
                for lines_item_data in self.lines:
                    lines_item = lines_item_data.to_dict()

                    lines.append(lines_item)

        modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat() if self.modified_date else None

        source_modified_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.source_modified_date, Unset):
            source_modified_date = self.source_modified_date.isoformat() if self.source_modified_date else None

        reference = self.reference
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        supplemental_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplemental_data, Unset):
            supplemental_data = self.supplemental_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "date": date,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if customer_ref is not UNSET:
            field_dict["customerRef"] = customer_ref
        if account_ref is not UNSET:
            field_dict["accountRef"] = account_ref
        if payment_method_ref is not UNSET:
            field_dict["paymentMethodRef"] = payment_method_ref
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_rate is not UNSET:
            field_dict["currencyRate"] = currency_rate
        if note is not UNSET:
            field_dict["note"] = note
        if lines is not UNSET:
            field_dict["lines"] = lines
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if source_modified_date is not UNSET:
            field_dict["sourceModifiedDate"] = source_modified_date
        if reference is not UNSET:
            field_dict["reference"] = reference
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if supplemental_data is not UNSET:
            field_dict["supplementalData"] = supplemental_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_account_ref import CodatDataContractsDatasetsAccountRef
        from ..models.codat_data_contracts_datasets_customer_ref import CodatDataContractsDatasetsCustomerRef
        from ..models.codat_data_contracts_datasets_data_interfaces_supplemental_data import (
            CodatDataContractsDatasetsDataInterfacesSupplementalData,
        )
        from ..models.codat_data_contracts_datasets_metadata import CodatDataContractsDatasetsMetadata
        from ..models.codat_data_contracts_datasets_payment_line import CodatDataContractsDatasetsPaymentLine
        from ..models.codat_data_contracts_datasets_payment_method_ref import CodatDataContractsDatasetsPaymentMethodRef

        d = src_dict.copy()
        date = isoparse(d.pop("date"))

        id = d.pop("id", UNSET)

        _customer_ref = d.pop("customerRef", UNSET)
        customer_ref: Union[Unset, CodatDataContractsDatasetsCustomerRef]
        if isinstance(_customer_ref, Unset):
            customer_ref = UNSET
        else:
            customer_ref = CodatDataContractsDatasetsCustomerRef.from_dict(_customer_ref)

        _account_ref = d.pop("accountRef", UNSET)
        account_ref: Union[Unset, CodatDataContractsDatasetsAccountRef]
        if isinstance(_account_ref, Unset):
            account_ref = UNSET
        else:
            account_ref = CodatDataContractsDatasetsAccountRef.from_dict(_account_ref)

        _payment_method_ref = d.pop("paymentMethodRef", UNSET)
        payment_method_ref: Union[Unset, CodatDataContractsDatasetsPaymentMethodRef]
        if isinstance(_payment_method_ref, Unset):
            payment_method_ref = UNSET
        else:
            payment_method_ref = CodatDataContractsDatasetsPaymentMethodRef.from_dict(_payment_method_ref)

        total_amount = d.pop("totalAmount", UNSET)

        currency = d.pop("currency", UNSET)

        currency_rate = d.pop("currencyRate", UNSET)

        note = d.pop("note", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = CodatDataContractsDatasetsPaymentLine.from_dict(lines_item_data)

            lines.append(lines_item)

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: Union[Unset, None, datetime.datetime]
        if _modified_date is None:
            modified_date = None
        elif isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        _source_modified_date = d.pop("sourceModifiedDate", UNSET)
        source_modified_date: Union[Unset, None, datetime.datetime]
        if _source_modified_date is None:
            source_modified_date = None
        elif isinstance(_source_modified_date, Unset):
            source_modified_date = UNSET
        else:
            source_modified_date = isoparse(_source_modified_date)

        reference = d.pop("reference", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CodatDataContractsDatasetsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CodatDataContractsDatasetsMetadata.from_dict(_metadata)

        _supplemental_data = d.pop("supplementalData", UNSET)
        supplemental_data: Union[Unset, CodatDataContractsDatasetsDataInterfacesSupplementalData]
        if isinstance(_supplemental_data, Unset):
            supplemental_data = UNSET
        else:
            supplemental_data = CodatDataContractsDatasetsDataInterfacesSupplementalData.from_dict(_supplemental_data)

        codat_data_contracts_datasets_payment = cls(
            date=date,
            id=id,
            customer_ref=customer_ref,
            account_ref=account_ref,
            payment_method_ref=payment_method_ref,
            total_amount=total_amount,
            currency=currency,
            currency_rate=currency_rate,
            note=note,
            lines=lines,
            modified_date=modified_date,
            source_modified_date=source_modified_date,
            reference=reference,
            metadata=metadata,
            supplemental_data=supplemental_data,
        )

        return codat_data_contracts_datasets_payment
