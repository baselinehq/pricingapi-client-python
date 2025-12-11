from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_com_baselinehq_pricingapi_pkg_types_status import GithubComBaselinehqPricingapiPkgTypesStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_compute_pricings_row import SchemaComputePricingsRow


T = TypeVar("T", bound="TypesCustomPricingResponse")


@_attrs_define
class TypesCustomPricingResponse:
    """
    Attributes:
        entries (list[SchemaComputePricingsRow] | Unset):
        status (GithubComBaselinehqPricingapiPkgTypesStatus | Unset):
    """

    entries: list[SchemaComputePricingsRow] | Unset = UNSET
    status: GithubComBaselinehqPricingapiPkgTypesStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_compute_pricings_row import SchemaComputePricingsRow

        d = dict(src_dict)
        _entries = d.pop("entries", UNSET)
        entries: list[SchemaComputePricingsRow] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = SchemaComputePricingsRow.from_dict(entries_item_data)

                entries.append(entries_item)

        _status = d.pop("status", UNSET)
        status: GithubComBaselinehqPricingapiPkgTypesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GithubComBaselinehqPricingapiPkgTypesStatus(_status)

        types_custom_pricing_response = cls(
            entries=entries,
            status=status,
        )

        types_custom_pricing_response.additional_properties = d
        return types_custom_pricing_response

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
