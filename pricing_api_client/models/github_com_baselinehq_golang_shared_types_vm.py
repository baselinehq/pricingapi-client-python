from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComBaselinehqGolangSharedTypesVM")


@_attrs_define
class GithubComBaselinehqGolangSharedTypesVM:
    """
    Attributes:
        cpu_cores (float | Unset):
        ram_gb (float | Unset):
    """

    cpu_cores: float | Unset = UNSET
    ram_gb: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_cores = self.cpu_cores

        ram_gb = self.ram_gb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu_cores is not UNSET:
            field_dict["cpu_cores"] = cpu_cores
        if ram_gb is not UNSET:
            field_dict["ram_gb"] = ram_gb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpu_cores = d.pop("cpu_cores", UNSET)

        ram_gb = d.pop("ram_gb", UNSET)

        github_com_baselinehq_golang_shared_types_vm = cls(
            cpu_cores=cpu_cores,
            ram_gb=ram_gb,
        )

        github_com_baselinehq_golang_shared_types_vm.additional_properties = d
        return github_com_baselinehq_golang_shared_types_vm

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
