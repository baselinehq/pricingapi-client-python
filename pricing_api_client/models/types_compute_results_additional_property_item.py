from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_baselinehq_golang_shared_types_vm import GithubComBaselinehqGolangSharedTypesVM
    from ..models.schema_compute_pricings_row import SchemaComputePricingsRow
    from ..models.types_savings import TypesSavings


T = TypeVar("T", bound="TypesComputeResultsAdditionalPropertyItem")


@_attrs_define
class TypesComputeResultsAdditionalPropertyItem:
    """
    Attributes:
        instance_pricing (SchemaComputePricingsRow | Unset):
        savings (TypesSavings | Unset):
        vm (GithubComBaselinehqGolangSharedTypesVM | Unset):
    """

    instance_pricing: SchemaComputePricingsRow | Unset = UNSET
    savings: TypesSavings | Unset = UNSET
    vm: GithubComBaselinehqGolangSharedTypesVM | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_pricing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instance_pricing, Unset):
            instance_pricing = self.instance_pricing.to_dict()

        savings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.savings, Unset):
            savings = self.savings.to_dict()

        vm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vm, Unset):
            vm = self.vm.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_pricing is not UNSET:
            field_dict["instance_pricing"] = instance_pricing
        if savings is not UNSET:
            field_dict["savings"] = savings
        if vm is not UNSET:
            field_dict["vm"] = vm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_baselinehq_golang_shared_types_vm import GithubComBaselinehqGolangSharedTypesVM
        from ..models.schema_compute_pricings_row import SchemaComputePricingsRow
        from ..models.types_savings import TypesSavings

        d = dict(src_dict)
        _instance_pricing = d.pop("instance_pricing", UNSET)
        instance_pricing: SchemaComputePricingsRow | Unset
        if isinstance(_instance_pricing, Unset):
            instance_pricing = UNSET
        else:
            instance_pricing = SchemaComputePricingsRow.from_dict(_instance_pricing)

        _savings = d.pop("savings", UNSET)
        savings: TypesSavings | Unset
        if isinstance(_savings, Unset):
            savings = UNSET
        else:
            savings = TypesSavings.from_dict(_savings)

        _vm = d.pop("vm", UNSET)
        vm: GithubComBaselinehqGolangSharedTypesVM | Unset
        if isinstance(_vm, Unset):
            vm = UNSET
        else:
            vm = GithubComBaselinehqGolangSharedTypesVM.from_dict(_vm)

        types_compute_results_additional_property_item = cls(
            instance_pricing=instance_pricing,
            savings=savings,
            vm=vm,
        )

        types_compute_results_additional_property_item.additional_properties = d
        return types_compute_results_additional_property_item

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
