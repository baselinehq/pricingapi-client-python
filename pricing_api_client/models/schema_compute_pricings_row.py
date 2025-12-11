from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaComputePricingsRow")


@_attrs_define
class SchemaComputePricingsRow:
    """
    Attributes:
        availability_zone (str | Unset):
        cost_per_hour (float | Unset):
        cpu_cores (float | Unset):
        cpu_cores_cost_per_hour (float | Unset):
        created_at (str | Unset):
        id (str | Unset):
        instance_type (str | Unset):
        operating_system (str | Unset):
        period_billing_hours (float | Unset):
        provider (str | Unset):
        ram_gb (float | Unset):
        ram_gb_cost_per_hour (float | Unset):
        raw_pricing_data (list[int] | Unset):
        region (str | Unset):
        service (str | Unset):
        tags (list[int] | Unset):
        updated_at (str | Unset):
        usage_type (str | Unset):
    """

    availability_zone: str | Unset = UNSET
    cost_per_hour: float | Unset = UNSET
    cpu_cores: float | Unset = UNSET
    cpu_cores_cost_per_hour: float | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    instance_type: str | Unset = UNSET
    operating_system: str | Unset = UNSET
    period_billing_hours: float | Unset = UNSET
    provider: str | Unset = UNSET
    ram_gb: float | Unset = UNSET
    ram_gb_cost_per_hour: float | Unset = UNSET
    raw_pricing_data: list[int] | Unset = UNSET
    region: str | Unset = UNSET
    service: str | Unset = UNSET
    tags: list[int] | Unset = UNSET
    updated_at: str | Unset = UNSET
    usage_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        availability_zone = self.availability_zone

        cost_per_hour = self.cost_per_hour

        cpu_cores = self.cpu_cores

        cpu_cores_cost_per_hour = self.cpu_cores_cost_per_hour

        created_at = self.created_at

        id = self.id

        instance_type = self.instance_type

        operating_system = self.operating_system

        period_billing_hours = self.period_billing_hours

        provider = self.provider

        ram_gb = self.ram_gb

        ram_gb_cost_per_hour = self.ram_gb_cost_per_hour

        raw_pricing_data: list[int] | Unset = UNSET
        if not isinstance(self.raw_pricing_data, Unset):
            raw_pricing_data = self.raw_pricing_data

        region = self.region

        service = self.service

        tags: list[int] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        updated_at = self.updated_at

        usage_type = self.usage_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability_zone is not UNSET:
            field_dict["availability_zone"] = availability_zone
        if cost_per_hour is not UNSET:
            field_dict["cost_per_hour"] = cost_per_hour
        if cpu_cores is not UNSET:
            field_dict["cpu_cores"] = cpu_cores
        if cpu_cores_cost_per_hour is not UNSET:
            field_dict["cpu_cores_cost_per_hour"] = cpu_cores_cost_per_hour
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if instance_type is not UNSET:
            field_dict["instance_type"] = instance_type
        if operating_system is not UNSET:
            field_dict["operating_system"] = operating_system
        if period_billing_hours is not UNSET:
            field_dict["period_billing_hours"] = period_billing_hours
        if provider is not UNSET:
            field_dict["provider"] = provider
        if ram_gb is not UNSET:
            field_dict["ram_gb"] = ram_gb
        if ram_gb_cost_per_hour is not UNSET:
            field_dict["ram_gb_cost_per_hour"] = ram_gb_cost_per_hour
        if raw_pricing_data is not UNSET:
            field_dict["raw_pricing_data"] = raw_pricing_data
        if region is not UNSET:
            field_dict["region"] = region
        if service is not UNSET:
            field_dict["service"] = service
        if tags is not UNSET:
            field_dict["tags"] = tags
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if usage_type is not UNSET:
            field_dict["usage_type"] = usage_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        availability_zone = d.pop("availability_zone", UNSET)

        cost_per_hour = d.pop("cost_per_hour", UNSET)

        cpu_cores = d.pop("cpu_cores", UNSET)

        cpu_cores_cost_per_hour = d.pop("cpu_cores_cost_per_hour", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        instance_type = d.pop("instance_type", UNSET)

        operating_system = d.pop("operating_system", UNSET)

        period_billing_hours = d.pop("period_billing_hours", UNSET)

        provider = d.pop("provider", UNSET)

        ram_gb = d.pop("ram_gb", UNSET)

        ram_gb_cost_per_hour = d.pop("ram_gb_cost_per_hour", UNSET)

        raw_pricing_data = cast(list[int], d.pop("raw_pricing_data", UNSET))

        region = d.pop("region", UNSET)

        service = d.pop("service", UNSET)

        tags = cast(list[int], d.pop("tags", UNSET))

        updated_at = d.pop("updated_at", UNSET)

        usage_type = d.pop("usage_type", UNSET)

        schema_compute_pricings_row = cls(
            availability_zone=availability_zone,
            cost_per_hour=cost_per_hour,
            cpu_cores=cpu_cores,
            cpu_cores_cost_per_hour=cpu_cores_cost_per_hour,
            created_at=created_at,
            id=id,
            instance_type=instance_type,
            operating_system=operating_system,
            period_billing_hours=period_billing_hours,
            provider=provider,
            ram_gb=ram_gb,
            ram_gb_cost_per_hour=ram_gb_cost_per_hour,
            raw_pricing_data=raw_pricing_data,
            region=region,
            service=service,
            tags=tags,
            updated_at=updated_at,
            usage_type=usage_type,
        )

        schema_compute_pricings_row.additional_properties = d
        return schema_compute_pricings_row

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
