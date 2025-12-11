from enum import Enum


class GithubComBaselinehqGolangSharedTypesService(str, Enum):
    AMAZONEC2 = "AmazonEC2"
    AZURECOMPUTE = "AzureCompute"
    AZUREMANAGEDDISKS = "AzureManagedDisks"
    BASECOMPUTE = "BaseCompute"
    COMPUTEENGINE = "ComputeEngine"
    DROPLET = "Droplet"
    HETZNERCOMPUTE = "HetznerCompute"
    OVHPUBLICCLOUD = "OVHPublicCloud"

    def __str__(self) -> str:
        return str(self.value)
