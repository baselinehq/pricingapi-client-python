from enum import Enum


class GithubComBaselinehqGolangSharedTypesUsageType(str, Enum):
    CUSTOM = "CUSTOM"
    EXTENDED = "EXTENDED"
    ONDEMAND = "ONDEMAND"
    ONDEMAND_CUSTOM = "ONDEMAND_CUSTOM"
    RESERVED = "RESERVED"
    RESERVED_CUSTOM = "RESERVED_CUSTOM"
    SOLE_TENANCY = "SOLE_TENANCY"
    SPOT_PREEMPTIBLE = "SPOT_PREEMPTIBLE"
    SPOT_PREEMPTIBLE_CUSTOM = "SPOT_PREEMPTIBLE_CUSTOM"

    def __str__(self) -> str:
        return str(self.value)
