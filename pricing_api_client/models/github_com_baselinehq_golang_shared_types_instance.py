from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_com_baselinehq_golang_shared_types_provider import GithubComBaselinehqGolangSharedTypesProvider
from ..models.github_com_baselinehq_golang_shared_types_service import GithubComBaselinehqGolangSharedTypesService
from ..models.github_com_baselinehq_golang_shared_types_usage_type import GithubComBaselinehqGolangSharedTypesUsageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_baselinehq_golang_shared_types_vm import GithubComBaselinehqGolangSharedTypesVM


T = TypeVar("T", bound="GithubComBaselinehqGolangSharedTypesInstance")


@_attrs_define
class GithubComBaselinehqGolangSharedTypesInstance:
    """
    Attributes:
        availability_zone (str | Unset):
        id (str | Unset):
        instance_type (str | Unset):
        operating_system (str | Unset):
        provider (GithubComBaselinehqGolangSharedTypesProvider | Unset):
        region (str | Unset):
        service (GithubComBaselinehqGolangSharedTypesService | Unset):
        usage_type (GithubComBaselinehqGolangSharedTypesUsageType | Unset):
        vm (GithubComBaselinehqGolangSharedTypesVM | Unset):
    """

    availability_zone: str | Unset = UNSET
    id: str | Unset = UNSET
    instance_type: str | Unset = UNSET
    operating_system: str | Unset = UNSET
    provider: GithubComBaselinehqGolangSharedTypesProvider | Unset = UNSET
    region: str | Unset = UNSET
    service: GithubComBaselinehqGolangSharedTypesService | Unset = UNSET
    usage_type: GithubComBaselinehqGolangSharedTypesUsageType | Unset = UNSET
    vm: GithubComBaselinehqGolangSharedTypesVM | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        availability_zone = self.availability_zone

        id = self.id

        instance_type = self.instance_type

        operating_system = self.operating_system

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        region = self.region

        service: str | Unset = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.value

        usage_type: str | Unset = UNSET
        if not isinstance(self.usage_type, Unset):
            usage_type = self.usage_type.value

        vm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vm, Unset):
            vm = self.vm.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability_zone is not UNSET:
            field_dict["availability_zone"] = availability_zone
        if id is not UNSET:
            field_dict["id"] = id
        if instance_type is not UNSET:
            field_dict["instance_type"] = instance_type
        if operating_system is not UNSET:
            field_dict["operating_system"] = operating_system
        if provider is not UNSET:
            field_dict["provider"] = provider
        if region is not UNSET:
            field_dict["region"] = region
        if service is not UNSET:
            field_dict["service"] = service
        if usage_type is not UNSET:
            field_dict["usage_type"] = usage_type
        if vm is not UNSET:
            field_dict["vm"] = vm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_baselinehq_golang_shared_types_vm import GithubComBaselinehqGolangSharedTypesVM

        d = dict(src_dict)
        availability_zone = d.pop("availability_zone", UNSET)

        id = d.pop("id", UNSET)

        instance_type = d.pop("instance_type", UNSET)

        operating_system = d.pop("operating_system", UNSET)

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

        _usage_type = d.pop("usage_type", UNSET)
        usage_type: GithubComBaselinehqGolangSharedTypesUsageType | Unset
        if isinstance(_usage_type, Unset):
            usage_type = UNSET
        else:
            usage_type = GithubComBaselinehqGolangSharedTypesUsageType(_usage_type)

        _vm = d.pop("vm", UNSET)
        vm: GithubComBaselinehqGolangSharedTypesVM | Unset
        if isinstance(_vm, Unset):
            vm = UNSET
        else:
            vm = GithubComBaselinehqGolangSharedTypesVM.from_dict(_vm)

        github_com_baselinehq_golang_shared_types_instance = cls(
            availability_zone=availability_zone,
            id=id,
            instance_type=instance_type,
            operating_system=operating_system,
            provider=provider,
            region=region,
            service=service,
            usage_type=usage_type,
            vm=vm,
        )

        github_com_baselinehq_golang_shared_types_instance.additional_properties = d
        return github_com_baselinehq_golang_shared_types_instance

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
