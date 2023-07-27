from typing import Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemIOStream")


@define
class SystemIOStream:
    """
    Attributes:
        can_read (Union[Unset, bool]):
        can_write (Union[Unset, bool]):
        can_seek (Union[Unset, bool]):
        can_timeout (Union[Unset, bool]):
        length (Union[Unset, int]):
        position (Union[Unset, int]):
        read_timeout (Union[Unset, int]):
        write_timeout (Union[Unset, int]):
    """

    can_read: Union[Unset, bool] = UNSET
    can_write: Union[Unset, bool] = UNSET
    can_seek: Union[Unset, bool] = UNSET
    can_timeout: Union[Unset, bool] = UNSET
    length: Union[Unset, int] = UNSET
    position: Union[Unset, int] = UNSET
    read_timeout: Union[Unset, int] = UNSET
    write_timeout: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        can_read = self.can_read
        can_write = self.can_write
        can_seek = self.can_seek
        can_timeout = self.can_timeout
        length = self.length
        position = self.position
        read_timeout = self.read_timeout
        write_timeout = self.write_timeout

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if can_read is not UNSET:
            field_dict["canRead"] = can_read
        if can_write is not UNSET:
            field_dict["canWrite"] = can_write
        if can_seek is not UNSET:
            field_dict["canSeek"] = can_seek
        if can_timeout is not UNSET:
            field_dict["canTimeout"] = can_timeout
        if length is not UNSET:
            field_dict["length"] = length
        if position is not UNSET:
            field_dict["position"] = position
        if read_timeout is not UNSET:
            field_dict["readTimeout"] = read_timeout
        if write_timeout is not UNSET:
            field_dict["writeTimeout"] = write_timeout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        can_read = d.pop("canRead", UNSET)

        can_write = d.pop("canWrite", UNSET)

        can_seek = d.pop("canSeek", UNSET)

        can_timeout = d.pop("canTimeout", UNSET)

        length = d.pop("length", UNSET)

        position = d.pop("position", UNSET)

        read_timeout = d.pop("readTimeout", UNSET)

        write_timeout = d.pop("writeTimeout", UNSET)

        system_io_stream = cls(
            can_read=can_read,
            can_write=can_write,
            can_seek=can_seek,
            can_timeout=can_timeout,
            length=length,
            position=position,
            read_timeout=read_timeout,
            write_timeout=write_timeout,
        )

        return system_io_stream
