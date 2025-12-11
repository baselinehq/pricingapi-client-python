from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_com_baselinehq_golang_shared_types_provider import GithubComBaselinehqGolangSharedTypesProvider
from ..models.github_com_baselinehq_golang_shared_types_service import GithubComBaselinehqGolangSharedTypesService
from ..models.github_com_baselinehq_golang_shared_types_usage_type import GithubComBaselinehqGolangSharedTypesUsageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesDisk")


@_attrs_define
class TypesDisk:
    """
    Attributes:
        availability_zone (str | Unset):
        capacity_gb (float | Unset):
        id (str | Unset):
        iops (float | Unset):
        provider (GithubComBaselinehqGolangSharedTypesProvider | Unset):
        region (str | Unset):
        service (GithubComBaselinehqGolangSharedTypesService | Unset):
        throughput_mbps (float | Unset):
        type_ (str | Unset):
        usage_type (GithubComBaselinehqGolangSharedTypesUsageType | Unset):
    """

    availability_zone: str | Unset = UNSET
    capacity_gb: float | Unset = UNSET
    id: str | Unset = UNSET
    iops: float | Unset = UNSET
    provider: GithubComBaselinehqGolangSharedTypesProvider | Unset = UNSET
    region: str | Unset = UNSET
    service: GithubComBaselinehqGolangSharedTypesService | Unset = UNSET
    throughput_mbps: float | Unset = UNSET
    type_: str | Unset = UNSET
    usage_type: GithubComBaselinehqGolangSharedTypesUsageType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        availability_zone = self.availability_zone

        capacity_gb = self.capacity_gb

        id = self.id

        iops = self.iops

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        region = self.region

        service: str | Unset = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.value

        throughput_mbps = self.throughput_mbps

        type_ = self.type_

        usage_type: str | Unset = UNSET
        if not isinstance(self.usage_type, Unset):
            usage_type = self.usage_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability_zone is not UNSET:
            field_dict["availability_zone"] = availability_zone
        if capacity_gb is not UNSET:
            field_dict["capacity_gb"] = capacity_gb
        if id is not UNSET:
            field_dict["id"] = id
        if iops is not UNSET:
            field_dict["iops"] = iops
        if provider is not UNSET:
            field_dict["provider"] = provider
        if region is not UNSET:
            field_dict["region"] = region
        if service is not UNSET:
            field_dict["service"] = service
        if throughput_mbps is not UNSET:
            field_dict["throughput_mbps"] = throughput_mbps
        if type_ is not UNSET:
            field_dict["type"] = type_
        if usage_type is not UNSET:
            field_dict["usage_type"] = usage_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        availability_zone = d.pop("availability_zone", UNSET)

        capacity_gb = d.pop("capacity_gb", UNSET)

        id = d.pop("id", UNSET)

        iops = d.pop("iops", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: GithubComBaselinehqGolangSharedTypesProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = GithubComBaselinehqGolangSharedTypesProvider(_provider)

        region = d.pop("region", UNSET)

        _service = d.pop("service", UNSET)
        service: GithubComBaselinehqGolangSharedTypesService | Unset
        if isinstance(_service, Unset):
            service = UNSET
        else:
            service = GithubComBaselinehqGolangSharedTypesService(_service)

        throughput_mbps = d.pop("throughput_mbps", UNSET)

        type_ = d.pop("type", UNSET)

        _usage_type = d.pop("usage_type", UNSET)
        usage_type: GithubComBaselinehqGolangSharedTypesUsageType | Unset
        if isinstance(_usage_type, Unset):
            usage_type = UNSET
        else:
            usage_type = GithubComBaselinehqGolangSharedTypesUsageType(_usage_type)

        types_disk = cls(
            availability_zone=availability_zone,
            capacity_gb=capacity_gb,
            id=id,
            iops=iops,
            provider=provider,
            region=region,
            service=service,
            throughput_mbps=throughput_mbps,
            type_=type_,
            usage_type=usage_type,
        )

        types_disk.additional_properties = d
        return types_disk

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
