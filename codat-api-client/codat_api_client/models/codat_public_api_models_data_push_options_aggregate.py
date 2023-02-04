from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codat_data_contracts_push_push_option import CodatDataContractsPushPushOption


T = TypeVar("T", bound="CodatPublicApiModelsDataPushOptionsAggregate")


@attr.s(auto_attribs=True)
class CodatPublicApiModelsDataPushOptionsAggregate:
    """
    Attributes:
        put (Union[Unset, CodatDataContractsPushPushOption]):
        post (Union[Unset, CodatDataContractsPushPushOption]):
    """

    put: Union[Unset, "CodatDataContractsPushPushOption"] = UNSET
    post: Union[Unset, "CodatDataContractsPushPushOption"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        put: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.put, Unset):
            put = self.put.to_dict()

        post: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.post, Unset):
            post = self.post.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if put is not UNSET:
            field_dict["put"] = put
        if post is not UNSET:
            field_dict["post"] = post

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codat_data_contracts_push_push_option import CodatDataContractsPushPushOption

        d = src_dict.copy()
        _put = d.pop("put", UNSET)
        put: Union[Unset, CodatDataContractsPushPushOption]
        if isinstance(_put, Unset):
            put = UNSET
        else:
            put = CodatDataContractsPushPushOption.from_dict(_put)

        _post = d.pop("post", UNSET)
        post: Union[Unset, CodatDataContractsPushPushOption]
        if isinstance(_post, Unset):
            post = UNSET
        else:
            post = CodatDataContractsPushPushOption.from_dict(_post)

        codat_public_api_models_data_push_options_aggregate = cls(
            put=put,
            post=post,
        )

        return codat_public_api_models_data_push_options_aggregate
