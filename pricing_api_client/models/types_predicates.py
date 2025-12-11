from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesPredicates")


@_attrs_define
class TypesPredicates:
    """
    Attributes:
        availability_zones (list[str] | Unset):
        disk_types (list[str] | Unset):
        instance_types (list[str] | Unset):
        operating_systems (list[str] | Unset):
        providers (list[str] | Unset):
        regions (list[str] | Unset):
        services (list[str] | Unset):
        usage_types (list[str] | Unset):
    """

    availability_zones: list[str] | Unset = UNSET
    disk_types: list[str] | Unset = UNSET
    instance_types: list[str] | Unset = UNSET
    operating_systems: list[str] | Unset = UNSET
    providers: list[str] | Unset = UNSET
    regions: list[str] | Unset = UNSET
    services: list[str] | Unset = UNSET
    usage_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        availability_zones: list[str] | Unset = UNSET
        if not isinstance(self.availability_zones, Unset):
            availability_zones = self.availability_zones

        disk_types: list[str] | Unset = UNSET
        if not isinstance(self.disk_types, Unset):
            disk_types = self.disk_types

        instance_types: list[str] | Unset = UNSET
        if not isinstance(self.instance_types, Unset):
            instance_types = self.instance_types

        operating_systems: list[str] | Unset = UNSET
        if not isinstance(self.operating_systems, Unset):
            operating_systems = self.operating_systems

        providers: list[str] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = self.providers

        regions: list[str] | Unset = UNSET
        if not isinstance(self.regions, Unset):
            regions = self.regions

        services: list[str] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = self.services

        usage_types: list[str] | Unset = UNSET
        if not isinstance(self.usage_types, Unset):
            usage_types = self.usage_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability_zones is not UNSET:
            field_dict["availability_zones"] = availability_zones
        if disk_types is not UNSET:
            field_dict["disk_types"] = disk_types
        if instance_types is not UNSET:
            field_dict["instance_types"] = instance_types
        if operating_systems is not UNSET:
            field_dict["operating_systems"] = operating_systems
        if providers is not UNSET:
            field_dict["providers"] = providers
        if regions is not UNSET:
            field_dict["regions"] = regions
        if services is not UNSET:
            field_dict["services"] = services
        if usage_types is not UNSET:
            field_dict["usage_types"] = usage_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        availability_zones = cast(list[str], d.pop("availability_zones", UNSET))

        disk_types = cast(list[str], d.pop("disk_types", UNSET))

        instance_types = cast(list[str], d.pop("instance_types", UNSET))

        operating_systems = cast(list[str], d.pop("operating_systems", UNSET))

        providers = cast(list[str], d.pop("providers", UNSET))

        regions = cast(list[str], d.pop("regions", UNSET))

        services = cast(list[str], d.pop("services", UNSET))

        usage_types = cast(list[str], d.pop("usage_types", UNSET))

        types_predicates = cls(
            availability_zones=availability_zones,
            disk_types=disk_types,
            instance_types=instance_types,
            operating_systems=operating_systems,
            providers=providers,
            regions=regions,
            services=services,
            usage_types=usage_types,
        )

        types_predicates.additional_properties = d
        return types_predicates

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
