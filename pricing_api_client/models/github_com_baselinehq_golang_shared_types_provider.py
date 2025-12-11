from enum import Enum


class GithubComBaselinehqGolangSharedTypesProvider(str, Enum):
    AWS = "AWS"
    AZURE = "Azure"
    BASE = "Base"
    DIGITALOCEAN = "DigitalOcean"
    GCP = "GCP"
    HETZNER = "Hetzner"
    OVHCLOUD = "OVHCloud"

    def __str__(self) -> str:
        return str(self.value)
