from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaDiskPricingsRow")


@_attrs_define
class SchemaDiskPricingsRow:
    """
    Attributes:
        availability_zone (str | Unset):
        cost_per_gb_hour (float | Unset):
        cost_per_iops_hour (float | Unset):
        cost_per_throughput_mbps_hour (float | Unset):
        created_at (str | Unset):
        id (str | Unset):
        max_capacity_gb (float | Unset):
        max_iops (float | Unset):
        max_throughput_mbps (float | Unset):
        min_capacity_gb (float | Unset):
        min_iops (float | Unset):
        min_throughput_mbps (float | Unset):
        period_billing_hours (float | Unset):
        provider (str | Unset):
        raw_pricing_data (list[int] | Unset):
        region (str | Unset):
        service (str | Unset):
        tags (list[int] | Unset):
        type_ (str | Unset):
        updated_at (str | Unset):
        usage_type (str | Unset):
    """

    availability_zone: str | Unset = UNSET
    cost_per_gb_hour: float | Unset = UNSET
    cost_per_iops_hour: float | Unset = UNSET
    cost_per_throughput_mbps_hour: float | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    max_capacity_gb: float | Unset = UNSET
    max_iops: float | Unset = UNSET
    max_throughput_mbps: float | Unset = UNSET
    min_capacity_gb: float | Unset = UNSET
    min_iops: float | Unset = UNSET
    min_throughput_mbps: float | Unset = UNSET
    period_billing_hours: float | Unset = UNSET
    provider: str | Unset = UNSET
    raw_pricing_data: list[int] | Unset = UNSET
    region: str | Unset = UNSET
    service: str | Unset = UNSET
    tags: list[int] | Unset = UNSET
    type_: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    usage_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        availability_zone = self.availability_zone

        cost_per_gb_hour = self.cost_per_gb_hour

        cost_per_iops_hour = self.cost_per_iops_hour

        cost_per_throughput_mbps_hour = self.cost_per_throughput_mbps_hour

        created_at = self.created_at

        id = self.id

        max_capacity_gb = self.max_capacity_gb

        max_iops = self.max_iops

        max_throughput_mbps = self.max_throughput_mbps

        min_capacity_gb = self.min_capacity_gb

        min_iops = self.min_iops

        min_throughput_mbps = self.min_throughput_mbps

        period_billing_hours = self.period_billing_hours

        provider = self.provider

        raw_pricing_data: list[int] | Unset = UNSET
        if not isinstance(self.raw_pricing_data, Unset):
            raw_pricing_data = self.raw_pricing_data

        region = self.region

        service = self.service

        tags: list[int] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        type_ = self.type_

        updated_at = self.updated_at

        usage_type = self.usage_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability_zone is not UNSET:
            field_dict["availability_zone"] = availability_zone
        if cost_per_gb_hour is not UNSET:
            field_dict["cost_per_gb_hour"] = cost_per_gb_hour
        if cost_per_iops_hour is not UNSET:
            field_dict["cost_per_iops_hour"] = cost_per_iops_hour
        if cost_per_throughput_mbps_hour is not UNSET:
            field_dict["cost_per_throughput_mbps_hour"] = cost_per_throughput_mbps_hour
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if max_capacity_gb is not UNSET:
            field_dict["max_capacity_gb"] = max_capacity_gb
        if max_iops is not UNSET:
            field_dict["max_iops"] = max_iops
        if max_throughput_mbps is not UNSET:
            field_dict["max_throughput_mbps"] = max_throughput_mbps
        if min_capacity_gb is not UNSET:
            field_dict["min_capacity_gb"] = min_capacity_gb
        if min_iops is not UNSET:
            field_dict["min_iops"] = min_iops
        if min_throughput_mbps is not UNSET:
            field_dict["min_throughput_mbps"] = min_throughput_mbps
        if period_billing_hours is not UNSET:
            field_dict["period_billing_hours"] = period_billing_hours
        if provider is not UNSET:
            field_dict["provider"] = provider
        if raw_pricing_data is not UNSET:
            field_dict["raw_pricing_data"] = raw_pricing_data
        if region is not UNSET:
            field_dict["region"] = region
        if service is not UNSET:
            field_dict["service"] = service
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if usage_type is not UNSET:
            field_dict["usage_type"] = usage_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        availability_zone = d.pop("availability_zone", UNSET)

        cost_per_gb_hour = d.pop("cost_per_gb_hour", UNSET)

        cost_per_iops_hour = d.pop("cost_per_iops_hour", UNSET)

        cost_per_throughput_mbps_hour = d.pop("cost_per_throughput_mbps_hour", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        max_capacity_gb = d.pop("max_capacity_gb", UNSET)

        max_iops = d.pop("max_iops", UNSET)

        max_throughput_mbps = d.pop("max_throughput_mbps", UNSET)

        min_capacity_gb = d.pop("min_capacity_gb", UNSET)

        min_iops = d.pop("min_iops", UNSET)

        min_throughput_mbps = d.pop("min_throughput_mbps", UNSET)

        period_billing_hours = d.pop("period_billing_hours", UNSET)

        provider = d.pop("provider", UNSET)

        raw_pricing_data = cast(list[int], d.pop("raw_pricing_data", UNSET))

        region = d.pop("region", UNSET)

        service = d.pop("service", UNSET)

        tags = cast(list[int], d.pop("tags", UNSET))

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        usage_type = d.pop("usage_type", UNSET)

        schema_disk_pricings_row = cls(
            availability_zone=availability_zone,
            cost_per_gb_hour=cost_per_gb_hour,
            cost_per_iops_hour=cost_per_iops_hour,
            cost_per_throughput_mbps_hour=cost_per_throughput_mbps_hour,
            created_at=created_at,
            id=id,
            max_capacity_gb=max_capacity_gb,
            max_iops=max_iops,
            max_throughput_mbps=max_throughput_mbps,
            min_capacity_gb=min_capacity_gb,
            min_iops=min_iops,
            min_throughput_mbps=min_throughput_mbps,
            period_billing_hours=period_billing_hours,
            provider=provider,
            raw_pricing_data=raw_pricing_data,
            region=region,
            service=service,
            tags=tags,
            type_=type_,
            updated_at=updated_at,
            usage_type=usage_type,
        )

        schema_disk_pricings_row.additional_properties = d
        return schema_disk_pricings_row

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
