from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesSavings")


@_attrs_define
class TypesSavings:
    """
    Attributes:
        amount_per_hour (float | Unset):
        amount_per_month (float | Unset):
        amount_per_year (float | Unset):
        percentage (float | Unset):
    """

    amount_per_hour: float | Unset = UNSET
    amount_per_month: float | Unset = UNSET
    amount_per_year: float | Unset = UNSET
    percentage: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_per_hour = self.amount_per_hour

        amount_per_month = self.amount_per_month

        amount_per_year = self.amount_per_year

        percentage = self.percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_per_hour is not UNSET:
            field_dict["amount_per_hour"] = amount_per_hour
        if amount_per_month is not UNSET:
            field_dict["amount_per_month"] = amount_per_month
        if amount_per_year is not UNSET:
            field_dict["amount_per_year"] = amount_per_year
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_per_hour = d.pop("amount_per_hour", UNSET)

        amount_per_month = d.pop("amount_per_month", UNSET)

        amount_per_year = d.pop("amount_per_year", UNSET)

        percentage = d.pop("percentage", UNSET)

        types_savings = cls(
            amount_per_hour=amount_per_hour,
            amount_per_month=amount_per_month,
            amount_per_year=amount_per_year,
            percentage=percentage,
        )

        types_savings.additional_properties = d
        return types_savings

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
