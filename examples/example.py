import os
import logging
import math

from kubernetes import client as k8s_client, config as k8s_config
import pricing_api_client
from pricing_api_client.models.github_com_baselinehq_golang_shared_types_instance import GithubComBaselinehqGolangSharedTypesInstance
from pricing_api_client.models.schema_compute_pricings_row import SchemaComputePricingsRow
from pricing_api_client.rest import ApiException
from pprint import pprint
from pricing_api_client.models.github_com_baselinehq_golang_shared_types_instance import GithubComBaselinehqGolangSharedTypesInstance
from pricing_api_client.models.github_com_baselinehq_golang_shared_types_provider import  GithubComBaselinehqGolangSharedTypesProvider
from pricing_api_client.models.github_com_baselinehq_golang_shared_types_service import  GithubComBaselinehqGolangSharedTypesService
from pricing_api_client.models.github_com_baselinehq_golang_shared_types_usage_type import  GithubComBaselinehqGolangSharedTypesUsageType
from pricing_api_client.models.github_com_baselinehq_golang_shared_types_vm import  GithubComBaselinehqGolangSharedTypesVM
from typing import Any


logger = logging.getLogger(__name__)


def _parse_cpu(value: str) -> float:
    # k8s CPU might be "1000m" or "2"
    v = str(value).strip()
    if v.endswith("m"):
        try:
            return float(v[:-1]) / 1000.0
        except ValueError:
            return 0.0
    try:
        return float(v)
    except ValueError:
        return 0.0


def _parse_memory_gb(value: str) -> float:
    # Accept k8s formats like "17179869184", "16Gi", "16384Mi"
    v = str(value).strip()
    units = {"Ki": 1 / 1024 / 1024 / 1024, "Mi": 1 / 1024 / 1024, "Gi": 1 / 1024, "Ti": 1}
    for suffix, factor in units.items():
        if v.endswith(suffix):
            try:
                num = float(v[:-len(suffix)])
                return math.ceil(num * factor)
            except ValueError:
                return 0.0
    # assume raw bytes if purely numeric
    try:
        num = float(v)
        # if it's bytes convert to GB
        return math.ceil(num / 1024 / 1024 / 1024)
    except ValueError:
        return 0.0


def get_provider_instance(node: Any) -> GithubComBaselinehqGolangSharedTypesInstance:
    provider_id = ""
    try:
        provider_id = str(node.spec.provider_id).lower()
    except Exception:
        # try alternative shapes
        provider_id = str(getattr(node, "provider_id", "")).lower()

    if provider_id.startswith("gce") or provider_id.startswith("gce://"):
        return GithubComBaselinehqGolangSharedTypesInstance(provider=GithubComBaselinehqGolangSharedTypesProvider.GCP, service=GithubComBaselinehqGolangSharedTypesService.ComputeEngine)
    if provider_id.startswith("aws") or provider_id.startswith("aws://"):
        return GithubComBaselinehqGolangSharedTypesInstance(provider=GithubComBaselinehqGolangSharedTypesProvider.AWS, service=GithubComBaselinehqGolangSharedTypesService.AmazonEC2)
    if provider_id.startswith("azure") or provider_id.startswith("azure://"):
        return GithubComBaselinehqGolangSharedTypesInstance(provider=GithubComBaselinehqGolangSharedTypesProvider.Azure, service=GithubComBaselinehqGolangSharedTypesService.AzureCompute)
    if provider_id.startswith("digitalocean") or provider_id.startswith("do://"):
        return GithubComBaselinehqGolangSharedTypesInstance(provider=GithubComBaselinehqGolangSharedTypesProvider.DigitalOcean, service=GithubComBaselinehqGolangSharedTypesService.Droplet)
    return GithubComBaselinehqGolangSharedTypesInstance(provider=GithubComBaselinehqGolangSharedTypesProvider.Base, service=GithubComBaselinehqGolangSharedTypesService.BaseCompute)


def get_usage_type(node: Any) -> GithubComBaselinehqGolangSharedTypesUsageType:
    # ctx can be unused; mimic logger extraction
    node_usage = GithubComBaselinehqGolangSharedTypesUsageType.ONDEMAND
    labels = {}
    try:
        labels = node.metadata.labels or {}
    except Exception:
        labels = getattr(node, "labels", {}) or {}

    for k, v in labels.items():
        for usage_candidate in (k, v):
            if "spot" in usage_candidate.lower() or "preemptible" in usage_candidate.lower():
                logger.info("Detected spot or preemptible label: %s=%s", k, v)
                node_usage = GithubComBaselinehqGolangSharedTypesUsageType.SPOT_PREEMPTIBLE

    instance_type_label = labels.get("beta.kubernetes.io/instance-type") or labels.get("node.kubernetes.io/instance-type", "")
    if "custom" in instance_type_label.lower():
        logger.info("Detected custom instance type: %s", instance_type_label)
        node_usage = node_usage.append(UsageType.CUSTOM.value)  # type: ignore

    return node_usage


def get_instance_from_node(node: Any) -> GithubComBaselinehqGolangSharedTypesInstance:
    labels = {}
    try:
        labels = node.metadata.labels or {}
    except Exception:
        labels = getattr(node, "labels", {}) or {}

    labels_to_verify = {
        "topology.kubernetes.io/region": True,
        "node.kubernetes.io/instance-type": True,
        "kubernetes.io/os": True,
        "topology.kubernetes.io/zone": False,
    }

    node_name = (node.metadata.name if node.metadata else "<unknown>")
    for label, required in labels_to_verify.items():
        if label not in labels:
            logger.info("missing label %s for node %s", label, node_name)
            if required:
                raise ValueError(f"required label {label}, add in manually to continue: kubectl label node/{node_name} {label}=<value>")

    instance = get_provider_instance(node)
    instance.region = labels.get("topology.kubernetes.io/region", "")
    instance.instance_type = labels.get("node.kubernetes.io/instance-type", "")
    instance.operating_system = labels.get("kubernetes.io/os", "")
    instance.availability_zone = labels.get("topology.kubernetes.io/zone", "")
    instance.usage_type = get_usage_type(node)

    if instance.usage_type.lower() == GithubComBaselinehqGolangSharedTypesUsageType.SPOT_PREEMPTIBLE.lower() and instance.availability_zone == "" and instance.provider.value == GithubComBaselinehqGolangSharedTypesVM.AWS.value:
        raise ValueError(f"required label topology.kubernetes.io/zone for {GithubComBaselinehqGolangSharedTypesUsageType.SPOT_PREEMPTIBLE} instances, add in manually to continue: kubectl label node/{getattr(node, 'metadata', {}).get('name', '<node>')} topology.kubernetes.io/zone=<value>")

    # parse capacities
    capacity = {}
    try:
        capacity = node.status.capacity or {}
    except Exception:
        capacity = getattr(node, "status", {}).get("capacity", {}) or {}

    cpu_raw = capacity.get("cpu", capacity.get("CPU", "0"))
    mem_raw = capacity.get("memory", capacity.get("Memory", "0"))

    cpu = _parse_cpu(cpu_raw)
    ram_gb = _parse_memory_gb(mem_raw)

    instance.vm = GithubComBaselinehqGolangSharedTypesVM(cpu_cores=cpu, ram_gb=ram_gb)
    return instance


token = os.getenv("BASELINEHQ_CLOUD_API_KEY")
if token is None:
    raise ValueError("BASELINEHQ_CLOUD_API_KEY environment variable not set")

configuration = pricing_api_client.Configuration(
    host = "https://pricing.baselinehq.cloud"
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = token
configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

try:
    k8s_config.load_kube_config()
except Exception:
    try:
        k8s_config.load_incluster_config()
    except Exception as e:
        logger.warning("Could not load kube config: %s", e)

v1 = k8s_client.CoreV1Api()
nodes = v1.list_node().items
for node in nodes:
    print("-" * 20)
    print(
        f"Node: {node.metadata.name} ({node.metadata.uid})"
    )
    print(get_instance_from_node(node))
    with pricing_api_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = pricing_api_client.DefaultApi(api_client)

        try:
            # Get  pricing for an instance
            api_response = api_instance.pricing_compute_post(get_instance_from_node(node))
            pprint(api_response)
        except Exception as e:
            print("Exception when calling DefaultApi->pricing_compute_post: %s\n" % e)
