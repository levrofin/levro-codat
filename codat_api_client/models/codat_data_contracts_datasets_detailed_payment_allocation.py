from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define

if TYPE_CHECKING:
    from ..models.codat_data_contracts_datasets_allocation import CodatDataContractsDatasetsAllocation
    from ..models.codat_data_contracts_datasets_payment_allocation_payment import (
        CodatDataContractsDatasetsPaymentAllocationPayment,
    )


T = TypeVar("T", bound="CodatDataContractsDatasetsDetailedPaymentAllocation")


@define
class CodatDataContractsDatasetsDetailedPaymentAllocation:
    """
    Attributes:
        payment (CodatDataContractsDatasetsPaymentAllocationPayment):
        allocation (CodatDataContractsDatasetsAllocation):
    """

    payment: "CodatDataContractsDatasetsPaymentAllocationPayment"
    allocation: "CodatDataContractsDatasetsAllocation"

    def to_dict(self) -> Dict[str, Any]:
        payment = self.payment.to_dict()

        allocation = self.allocation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "payment": payment,
                "allocation": allocation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_datasets_allocation import CodatDataContractsDatasetsAllocation
        from ..models.codat_data_contracts_datasets_payment_allocation_payment import (
            CodatDataContractsDatasetsPaymentAllocationPayment,
        )

        d = src_dict.copy()
        payment = CodatDataContractsDatasetsPaymentAllocationPayment.from_dict(d.pop("payment"))

        allocation = CodatDataContractsDatasetsAllocation.from_dict(d.pop("allocation"))

        codat_data_contracts_datasets_detailed_payment_allocation = cls(
            payment=payment,
            allocation=allocation,
        )

        return codat_data_contracts_datasets_detailed_payment_allocation
