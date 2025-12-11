from enum import Enum


class GithubComBaselinehqPricingapiPkgTypesStatus(str, Enum):
    DELETED = "Deleted"
    REGISTERED = "Registered"

    def __str__(self) -> str:
        return str(self.value)
