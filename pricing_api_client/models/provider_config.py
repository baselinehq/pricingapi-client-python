from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_com_baselinehq_golang_shared_types_provider import GithubComBaselinehqGolangSharedTypesProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_predicates import TypesPredicates


T = TypeVar("T", bound="ProviderConfig")


@_attrs_define
class ProviderConfig:
    """
    Attributes:
        predicates (TypesPredicates | Unset):
        provider (GithubComBaselinehqGolangSharedTypesProvider | Unset):
    """

    predicates: TypesPredicates | Unset = UNSET
    provider: GithubComBaselinehqGolangSharedTypesProvider | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        predicates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.predicates, Unset):
            predicates = self.predicates.to_dict()

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if predicates is not UNSET:
            field_dict["predicates"] = predicates
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_predicates import TypesPredicates

        d = dict(src_dict)
        _predicates = d.pop("predicates", UNSET)
        predicates: TypesPredicates | Unset
        if isinstance(_predicates, Unset):
            predicates = UNSET
        else:
            predicates = TypesPredicates.from_dict(_predicates)

        _provider = d.pop("provider", UNSET)
        provider: GithubComBaselinehqGolangSharedTypesProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = GithubComBaselinehqGolangSharedTypesProvider(_provider)

        provider_config = cls(
            predicates=predicates,
            provider=provider,
        )

        provider_config.additional_properties = d
        return provider_config

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
