from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_disk_pricings_row import SchemaDiskPricingsRow
    from ..models.types_savings import TypesSavings


T = TypeVar("T", bound="TypesDiskResultsAdditionalPropertyItem")


@_attrs_define
class TypesDiskResultsAdditionalPropertyItem:
    """
    Attributes:
        disk (SchemaDiskPricingsRow | Unset):
        disk_pricing (SchemaDiskPricingsRow | Unset):
        savings (TypesSavings | Unset):
    """

    disk: SchemaDiskPricingsRow | Unset = UNSET
    disk_pricing: SchemaDiskPricingsRow | Unset = UNSET
    savings: TypesSavings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disk: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disk, Unset):
            disk = self.disk.to_dict()

        disk_pricing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disk_pricing, Unset):
            disk_pricing = self.disk_pricing.to_dict()

        savings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.savings, Unset):
            savings = self.savings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disk is not UNSET:
            field_dict["disk"] = disk
        if disk_pricing is not UNSET:
            field_dict["disk_pricing"] = disk_pricing
        if savings is not UNSET:
            field_dict["savings"] = savings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_disk_pricings_row import SchemaDiskPricingsRow
        from ..models.types_savings import TypesSavings

        d = dict(src_dict)
        _disk = d.pop("disk", UNSET)
        disk: SchemaDiskPricingsRow | Unset
        if isinstance(_disk, Unset):
            disk = UNSET
        else:
            disk = SchemaDiskPricingsRow.from_dict(_disk)

        _disk_pricing = d.pop("disk_pricing", UNSET)
        disk_pricing: SchemaDiskPricingsRow | Unset
        if isinstance(_disk_pricing, Unset):
            disk_pricing = UNSET
        else:
            disk_pricing = SchemaDiskPricingsRow.from_dict(_disk_pricing)

        _savings = d.pop("savings", UNSET)
        savings: TypesSavings | Unset
        if isinstance(_savings, Unset):
            savings = UNSET
        else:
            savings = TypesSavings.from_dict(_savings)

        types_disk_results_additional_property_item = cls(
            disk=disk,
            disk_pricing=disk_pricing,
            savings=savings,
        )

        types_disk_results_additional_property_item.additional_properties = d
        return types_disk_results_additional_property_item

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
