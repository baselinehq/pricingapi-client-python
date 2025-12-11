from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_baselinehq_golang_shared_types_instance import GithubComBaselinehqGolangSharedTypesInstance
    from ..models.github_com_baselinehq_golang_shared_types_vm import GithubComBaselinehqGolangSharedTypesVM
    from ..models.types_predicates import TypesPredicates


T = TypeVar("T", bound="TypesComputeRequest")


@_attrs_define
class TypesComputeRequest:
    """
    Attributes:
        include_metadata (bool | Unset):
        instance (GithubComBaselinehqGolangSharedTypesInstance | Unset):
        predicates (TypesPredicates | Unset):
        usage (GithubComBaselinehqGolangSharedTypesVM | Unset):
    """

    include_metadata: bool | Unset = UNSET
    instance: GithubComBaselinehqGolangSharedTypesInstance | Unset = UNSET
    predicates: TypesPredicates | Unset = UNSET
    usage: GithubComBaselinehqGolangSharedTypesVM | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_metadata = self.include_metadata

        instance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instance, Unset):
            instance = self.instance.to_dict()

        predicates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.predicates, Unset):
            predicates = self.predicates.to_dict()

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_metadata is not UNSET:
            field_dict["include_metadata"] = include_metadata
        if instance is not UNSET:
            field_dict["instance"] = instance
        if predicates is not UNSET:
            field_dict["predicates"] = predicates
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_baselinehq_golang_shared_types_instance import (
            GithubComBaselinehqGolangSharedTypesInstance,
        )
        from ..models.github_com_baselinehq_golang_shared_types_vm import GithubComBaselinehqGolangSharedTypesVM
        from ..models.types_predicates import TypesPredicates

        d = dict(src_dict)
        include_metadata = d.pop("include_metadata", UNSET)

        _instance = d.pop("instance", UNSET)
        instance: GithubComBaselinehqGolangSharedTypesInstance | Unset
        if isinstance(_instance, Unset):
            instance = UNSET
        else:
            instance = GithubComBaselinehqGolangSharedTypesInstance.from_dict(_instance)

        _predicates = d.pop("predicates", UNSET)
        predicates: TypesPredicates | Unset
        if isinstance(_predicates, Unset):
            predicates = UNSET
        else:
            predicates = TypesPredicates.from_dict(_predicates)

        _usage = d.pop("usage", UNSET)
        usage: GithubComBaselinehqGolangSharedTypesVM | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = GithubComBaselinehqGolangSharedTypesVM.from_dict(_usage)

        types_compute_request = cls(
            include_metadata=include_metadata,
            instance=instance,
            predicates=predicates,
            usage=usage,
        )

        types_compute_request.additional_properties = d
        return types_compute_request

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
